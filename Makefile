# Project management tasks.

VENV = .venv
PYTHON = source $(VENV)/bin/activate && python


$(VENV)/.make-update: requirements-dev.txt
	python -m venv $(VENV)
	$(PYTHON) -m pip install -U pip && for req in $^; do pip install -r "$$req"; done
	touch $@


.PHONY: dev
dev: $(VENV)/.make-update


.PHONY: test
test: dev
	$(PYTHON) tests/test_template.py
