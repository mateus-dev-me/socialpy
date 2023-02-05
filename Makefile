#!/bin/bash

all: clean install active test

install:
	@poetry install

active:
	@poetry shell

test:
	@pytest tests -v

format:
	@blue .
	@isort .

check:
	@blue . --check
	@isort . --check
	@mypy . --check

generate-requirements:
	@poetry export --without-hashes --format=requirements.txt > requirements.txt

sec:
	@pip-audit

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf buildrm  
	rm -rf distrm  
	rm -rf *.egg-inform  
	rm -rf htmlcovrm  
	rm -rf .tox/rm  
	rm -rf docs/_build
