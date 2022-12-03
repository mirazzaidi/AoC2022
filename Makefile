.PHONY: reformat
reformat:
	black ./ -S -t py38 -l 150 --exclude='venv'

.PHONY: lint
lint:
	black ./ -S -t py38 -l 150 --check --exclude='venv'