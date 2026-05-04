.PHONY: prework open-prs validate check extract-instructions release-zip labels-dry-run clean

prework:
	git status --short --branch
	python3 scripts/check_open_prs.py

open-prs:
	python3 scripts/check_open_prs.py

validate:
	python3 scripts/validate_workspace.py

check:
	python3 scripts/validate_workspace.py
	python3 -m py_compile scripts/*.py
	python3 scripts/sync_labels.py
	python3 scripts/build_release_zip.py

extract-instructions:
	python3 scripts/extract_instructions.py

release-zip:
	python3 scripts/build_release_zip.py

labels-dry-run:
	python3 scripts/sync_labels.py

clean:
	rm -rf dist .release
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
