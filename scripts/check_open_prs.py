#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPO = "GPTsAgent/GPTsAgent"


@dataclass(frozen=True)
class PullRequest:
    number: int
    title: str
    head: str
    base: str
    html_url: str


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def detect_repo() -> str:
    try:
        remote = run_git(["remote", "get-url", "origin"])
    except Exception:
        return DEFAULT_REPO

    if remote.startswith("git@github.com:"):
        return remote.removeprefix("git@github.com:").removesuffix(".git")
    if remote.startswith("https://github.com/"):
        path = remote.removeprefix("https://github.com/").removesuffix(".git")
        return path
    return DEFAULT_REPO


def github_request(url: str) -> tuple[object, dict[str, str]]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "GPTsAgent-open-pr-check",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)
        return payload, dict(response.headers.items())


def paginate(url: str) -> list[dict]:
    items: list[dict] = []
    next_url: str | None = url
    while next_url:
        payload, headers = github_request(next_url)
        if isinstance(payload, list):
            items.extend(payload)
        else:
            raise RuntimeError("unexpected GitHub API payload")
        next_url = None
        link = headers.get("Link", "")
        for part in link.split(","):
            if 'rel="next"' in part:
                start = part.find("<")
                end = part.find(">", start + 1)
                if start != -1 and end != -1:
                    next_url = part[start + 1 : end]
                break
    return items


def failure_status(exc: Exception) -> str:
    text = str(exc).lower()
    if isinstance(exc, TimeoutError) or "timed out" in text:
        return "TIMEOUT"
    return "NOT RUN"


def fetch_open_prs(repo: str, base: str) -> list[PullRequest]:
    url = (
        f"https://api.github.com/repos/{quote(repo, safe='/')}/pulls"
        f"?state=open&base={quote(base)}&per_page=100"
    )
    prs: list[PullRequest] = []
    for item in paginate(url):
        prs.append(
            PullRequest(
                number=int(item["number"]),
                title=str(item.get("title", "")),
                head=str(item.get("head", {}).get("ref", "")),
                base=str(item.get("base", {}).get("ref", "")),
                html_url=str(item.get("html_url", "")),
            )
        )
    return prs


def fetch_pr_files(repo: str, number: int) -> list[str]:
    url = (
        f"https://api.github.com/repos/{quote(repo, safe='/')}/pulls/{number}/files"
        "?per_page=100"
    )
    paths: list[str] = []
    for item in paginate(url):
        name = item.get("filename")
        if isinstance(name, str):
            paths.append(name)
    return paths


def local_changed_paths() -> set[str]:
    paths: set[str] = set()
    for args in (
        ["diff", "--name-only", "HEAD"],
        ["diff", "--name-only", "--cached"],
        ["ls-files", "--others", "--exclude-standard"],
    ):
        try:
            output = run_git(args)
        except Exception:
            continue
        for line in output.splitlines():
            line = line.strip()
            if line:
                paths.add(line)
    return paths


def status_line(overlap: bool, prs: list[PullRequest]) -> str:
    if not prs:
        return "PASS"
    if overlap:
        return "FAILED"
    return "PASS"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check open PRs and warn about overlap with local edits.")
    parser.add_argument("--repo", default=detect_repo(), help="GitHub repository in owner/name form")
    parser.add_argument("--base", default="main", help="Base branch to inspect")
    parser.add_argument("--soft", action="store_true", help="Do not exit non-zero on network failure")
    args = parser.parse_args()

    try:
        prs = fetch_open_prs(args.repo, args.base)
    except (HTTPError, URLError, TimeoutError, OSError, RuntimeError) as exc:
        print("# GPTsAgent Open PR Check")
        print(f"Repository: {args.repo}")
        print(f"Base: {args.base}")
        print(f"Status: {failure_status(exc)}")
        print(f"Detail: {exc.__class__.__name__}: {exc}")
        return 0 if args.soft else 2

    local_paths = local_changed_paths()
    open_pr_paths: set[str] = set()
    pr_file_map: dict[int, list[str]] = {}
    for pr in prs:
        try:
            files = fetch_pr_files(args.repo, pr.number)
        except (HTTPError, URLError, TimeoutError, OSError, RuntimeError) as exc:
            print("# GPTsAgent Open PR Check")
            print(f"Repository: {args.repo}")
            print(f"Base: {args.base}")
            print(f"Status: {failure_status(exc)}")
            print(f"Detail: failed to fetch files for PR #{pr.number}: {exc.__class__.__name__}: {exc}")
            return 0 if args.soft else 2
        pr_file_map[pr.number] = files
        open_pr_paths.update(files)

    overlap = sorted(local_paths.intersection(open_pr_paths))
    print("# GPTsAgent Open PR Check")
    print(f"Repository: {args.repo}")
    print(f"Base: {args.base}")
    print(f"Status: {status_line(bool(overlap), prs)}")
    print(f"OPEN_PRS {len(prs)}")
    if not prs:
        print("No open PRs found.")
    for pr in prs:
        print(f"#{pr.number} {pr.head} -> {pr.base}: {pr.title}")
        files = pr_file_map.get(pr.number, [])
        if files:
            print(f"  files: {', '.join(files[:12])}")
            if len(files) > 12:
                print(f"  files_truncated: {len(files) - 12} more")
        else:
            print("  files: none reported")
        if overlap:
            pr_overlap = sorted(set(files).intersection(local_paths))
            if pr_overlap:
                print(f"  overlap: {', '.join(pr_overlap[:12])}")
                if len(pr_overlap) > 12:
                    print(f"  overlap_truncated: {len(pr_overlap) - 12} more")
            else:
                print("  overlap: none")
        else:
            print("  overlap: none")
        if pr.html_url:
            print(f"  url: {pr.html_url}")
    if local_paths:
        print(f"Local changed files: {len(local_paths)}")
        if overlap:
            print(f"Overlap with local changes: {', '.join(overlap[:12])}")
            if len(overlap) > 12:
                print(f"Overlap truncated: {len(overlap) - 12} more")
        else:
            print("Overlap with local changes: none")
    else:
        print("Local changed files: 0")
        print("Overlap with local changes: none")
    print("Rule: If overlap exists, stop or narrow the work before editing.")
    return 1 if overlap else 0


if __name__ == "__main__":
    raise SystemExit(main())
