.PHONY: ruff
ruff:
	ruff format . && ruff check --fix . && isort .

.PHONY: local-run
local-run:
	python3 run.py

.PHONY: tests
tests:
	pytest