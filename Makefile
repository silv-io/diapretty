VENV_BIN = python3 -m venv
VENV_DIR ?= .venv
VENV_ACTIVATE = $(VENV_DIR)/bin/activate
VENV_RUN = . $(VENV_ACTIVATE)
ROOT_MODULE = diapretty

venv: $(VENV_ACTIVATE)

$(VENV_ACTIVATE): setup.py setup.cfg pyproject.toml
	test -d .venv || $(VENV_BIN) .venv
	$(VENV_RUN); pip install --upgrade pip setuptools wheel plux
	$(VENV_RUN); pip install -e .[dev]
	touch $(VENV_DIR)/bin/activate

install: venv

clean:
	rm -rf .venv
	rm -rf build/
	rm -rf .eggs/
	rm -rf *.egg-info/

format:
	$(VENV_RUN); python -m isort .; python -m black .

test: venv
	$(VENV_RUN); python -m pytest --cov $(ROOT_MODULE)

test-coverage: venv
	$(VENV_RUN); coverage run --source=$(ROOT_MODULE) -m pytest tests && coverage lcov -o .coverage.lcov

coveralls: venv
	$(VENV_RUN); coveralls

dist: venv
	$(VENV_RUN); python setup.py sdist bdist_wheel

deploy: clean-dist venv test dist
	$(VENV_RUN); pip install --upgrade twine; twine upload dist/*

clean-dist: clean
	rm -rf dist/

.PHONY: clean clean-dist
