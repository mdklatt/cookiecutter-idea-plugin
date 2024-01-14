# Project management tasks.

VENV = .venv
PYTHON = source $(VENV)/bin/activate && python
PYTEST = $(PYTHON) -m pytest


# Create local virtualenv.
$(VENV)/.make-update: requirements-dev.txt requirements.txt
	python -m venv $(VENV)
	$(PYTHON) -m pip install -U pip  # needs to be updated first
	$(PYTHON) -m pip install -r $<
	touch $@


# Set up the local development environment.
.PHONY: dev
dev: $(VENV)/.make-update


# Run template tests.
.PHONY: test
test: dev
	$(PYTEST) tests/
