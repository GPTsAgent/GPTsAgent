.PHONY: prework open-prs validate check extract-instructions release-zip release-artifacts labels-dry-run clean

prework:
	git status --short --branch
	python3 scripts/check_open_prs.py

open-prs:
	python3 scripts/check_open_prs.py

validate:
	python3 scripts/validate_workspace.py

check:
	python3 scripts/validate_workspace.py
	python3 scripts/validate_eval_fixtures.py
	python3 -m py_compile scripts/*.py
	python3 scripts/sync_labels.py
	python3 scripts/build_release_zip.py
	python3 scripts/validate_release_artifacts.py

eval-fixtures:
	python3 scripts/validate_eval_fixtures.py

extract-instructions:
	python3 scripts/extract_instructions.py

release-zip:
	python3 scripts/build_release_zip.py

release-artifacts:
	python3 scripts/build_release_zip.py
	python3 scripts/validate_release_artifacts.py

labels-dry-run:
	python3 scripts/sync_labels.py

clean:
	rm -rf dist .release
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
