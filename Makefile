.PHONY: validate extract-instructions release-zip labels-dry-run clean

validate:
	python3 scripts/validate_workspace.py

extract-instructions:
	python3 scripts/extract_instructions.py

release-zip:
	python3 scripts/build_release_zip.py

labels-dry-run:
	python3 scripts/sync_labels.py

clean:
	rm -rf dist .release
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
