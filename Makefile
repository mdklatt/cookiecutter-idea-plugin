# Project management tasks.

VENV = .venv

$(VENV)/.make-update: requirements-dev.txt
	python -m venv $(VENV)
	. $(VENV)/bin/activate && pip install -U pip && for req in $^; do pip install -r "$$req"; done
	touch $@


.PHONY: dev
dev: $(VENV)/.make-update


.PHONY: test
test: dev
	. $(VENV)/bin/activate && python tests/test_template.py
