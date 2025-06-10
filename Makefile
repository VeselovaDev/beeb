.PHONY: ruff
ruff:
	ruff format . && ruff check --fix . && isort .

.PHONY: local-run
local-run:
	python3 src/main.py

.PHONY: tests
tests:
	python3 -m pytest