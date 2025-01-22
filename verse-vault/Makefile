PYTHON = python3
PIP = pip
SPHINX_BUILD = sphinx-build
SPHINX_SOURCE = docs/source
SPHINX_OUTPUT = docs/build

.DEFAULT_GOAL := help

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make lint         - Run Flake8 for linting"
	@echo "  make test         - Run tests with pytest"
	@echo "  make coverage     - Run tests and generate coverage report"
	@echo "  make docs         - Generate documentation with Sphinx"
	@echo "  make clean        - Clean up temporary files"

install:
	$(PIP) install -r requirements.txt

lint:
	$(PYTHON) -m flake8 --max-line-length=100 --statistics

test:
	$(PYTHON) -m pytest tests/

coverage:
	$(PYTHON) -m pytest --cov=utils --cov=library --cov-report=term --cov-report=html

docs:
	$(SPHINX_BUILD) -b html $(SPHINX_SOURCE) $(SPHINX_OUTPUT)

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov $(SPHINX_OUTPUT)
