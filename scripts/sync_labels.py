#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABELS_FILE = ROOT / ".github" / "labels.json"
DEFAULT_REPOSITORY = "GPTsAgent/GPTsAgent"


def load_labels() -> list[dict[str, str]]:
    labels = json.loads(LABELS_FILE.read_text(encoding="utf-8"))
    if not isinstance(labels, list):
        raise ValueError(".github/labels.json must contain a list")
    for item in labels:
        if not isinstance(item, dict):
            raise ValueError("Each label entry must be an object")
        for key in ("name", "color", "description"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValueError(f"Label entry is missing a non-empty {key!r}")
    return labels


def request_json(url: str, token: str | None, method: str = "GET", payload: dict[str, str] | None = None) -> object:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, method=method)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    if data is not None:
        request.add_header("Content-Type", "application/json")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read()
    return json.loads(body.decode("utf-8")) if body else {}


def github_api(repository: str, path: str) -> str:
    return f"https://api.github.com/repos/{repository}{path}"


def current_labels(repository: str, token: str | None) -> dict[str, dict[str, object]]:
    data = request_json(github_api(repository, "/labels?per_page=100"), token)
    if not isinstance(data, list):
        raise RuntimeError("GitHub labels response was not a list")
    return {str(item["name"]): item for item in data if isinstance(item, dict) and "name" in item}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create missing GitHub labels from .github/labels.json.")
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPOSITORY))
    parser.add_argument("--apply", action="store_true", help="Create missing labels. Requires GH_TOKEN or GITHUB_TOKEN.")
    parser.add_argument("--update-existing", action="store_true", help="Also update existing label color and description.")
    args = parser.parse_args()

    labels = load_labels()
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")

    try:
        existing = current_labels(args.repository, token)
    except urllib.error.HTTPError as exc:
        print(f"FAILED: could not read labels from {args.repository}: HTTP {exc.code}", file=sys.stderr)
        return 1

    missing = [label for label in labels if label["name"] not in existing]
    existing_desired = [label for label in labels if label["name"] in existing]

    print(f"Repository: {args.repository}")
    print(f"Desired labels: {len(labels)}")
    print(f"Existing desired labels: {len(existing_desired)}")
    print(f"Missing labels: {len(missing)}")
    for label in missing:
        print(f"MISSING: {label['name']}")

    if not args.apply:
        print("Status: DRY RUN")
        return 0

    if not token:
        print("FAILED: --apply requires GH_TOKEN or GITHUB_TOKEN", file=sys.stderr)
        return 1

    for label in missing:
        payload = {
            "name": label["name"],
            "color": label["color"],
            "description": label["description"],
        }
        try:
            request_json(github_api(args.repository, "/labels"), token, method="POST", payload=payload)
        except urllib.error.HTTPError as exc:
            print(f"FAILED: could not create label {label['name']}: HTTP {exc.code}", file=sys.stderr)
            return 1
        print(f"CREATED: {label['name']}")

    if args.update_existing:
        for label in existing_desired:
            encoded = urllib.parse.quote(label["name"], safe="")
            payload = {
                "new_name": label["name"],
                "color": label["color"],
                "description": label["description"],
            }
            try:
                request_json(github_api(args.repository, f"/labels/{encoded}"), token, method="PATCH", payload=payload)
            except urllib.error.HTTPError as exc:
                print(f"FAILED: could not update label {label['name']}: HTTP {exc.code}", file=sys.stderr)
                return 1
            print(f"UPDATED: {label['name']}")

    print("Status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
