.PHONY: validate extract-instructions release-zip clean

validate:
	python3 scripts/validate_workspace.py

extract-instructions:
	python3 scripts/extract_instructions.py

release-zip:
	python3 scripts/build_release_zip.py

clean:
	rm -rf dist .release
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
