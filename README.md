# hypermodern-python-tuto

Repo to follow the Claudio Jolowicz's [tutorial about Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).

[![Tests](https://github.com/le-chartreux/hypermodern-python-tuto/workflows/Tests/badge.svg)](https://github.com/le-chartreux/hypermodern-python-tuto/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/le-chartreux/hypermodern-python-tuto/branch/master/graph/badge.svg)](https://codecov.io/gh/le-chartreux/hypermodern-python-tuto)
[![PyPI](https://img.shields.io/pypi/v/hypermodern-python-tuto.svg)](https://pypi.org/project/hypermodern-python-tuto/)

## Table of contents

- [Description of the application](#description-of-the-application)
- [Install](#install)
- [Use](#use)
- [Tools used](#tools-used)
  - [Generic tools](#generic-tools)
  - [Generic Python tools](#generic-python-tools)
    - [Multi-purpose](#multi-purpose)
    - [Setup](#setup)
    - [Test](#test)
    - [Linting](#linting)
    - [Security](#security)
    - [Formatting](#formatting)
    - [Type checking](#type-checking)
    - [Documentation](#documentation)
  - [Specific Python tools](#specific-python-tools)
    - [UI](#ui)
    - [Communication](#communication)
    - [Data validation](#data-validation)

## Description of the application

The app created is a CLI application that queries a random Wikipedia page and displays its title and summary.

## Install

TODO

## Use

TODO

## Tools used

### Generic tools

Tools that can be used in every development project, no matter if it's a Python project or not.

- [git](https://git-scm.com/), to manage versions of the source code
- [GitHub](https://github.com/le-chartreux/hypermodern-python-tuto), to host the git repository and execute Actions
- [pre-commit](https://pre-commit.com/), to manage pre-commit hooks
- [Codecov](https://about.codecov.io/), to mesure code coverage on repos
- [PyPI](https://pypi.org/), to publish packages

### Generic Python tools

Tools that can be used in every Python project, no matter its content.

#### Multi-purpose

- [poetry](https://python-poetry.org/), to make development and distribution easy (packaging, virtualization, dependencies, launching and publishing)
- [nox](https://nox.thea.codes/en/stable/), to run tasks in multiple Python environments (like tests, linting, reformatting, etc.)

#### Setup

- [pyenv](https://github.com/pyenv/pyenv), to manage Python versions

#### Test

- [pytest](https://docs.pytest.org/en/latest/), a framework to write unit tests. Also used to run doctests
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/), to mesure the code coverage (degree to which the source code of a program is executed while running its test suite)
- [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/), to use the [unittest](https://docs.python.org/3/library/unittest.html) mocking in the pytest way
- [xdoctest](https://pypi.org/project/xdoctest/), to execute the doctests (tests in documentation strings)

#### Linting

- [flake8](https://flake8.pycqa.org/en/latest/), a linter aggregator
- [flake8-import-order](https://github.com/PyCQA/flake8-import-order), to verify that imports are grouped and ordered in a consistent way
- [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear), to find bugs and design problems
- [flake8-annotations](https://pypi.org/project/flake8-annotations/), to detect the absence of type annotations
- [flake8-black](https://pypi.org/project/flake8-black/), to check if the code follows [black](https://black.readthedocs.io/en/stable/) formatting
- [flake8-docstrings](https://pypi.org/project/flake8-docstrings/), to check that the code is correctly documented
- [darglint](https://pypi.org/project/darglint/), to check that docstrings match function definitions

#### Security

- [Bandit](https://bandit.readthedocs.io/en/latest/), to find security issues (used inside linting with [flake8-bandit](https://pypi.org/project/flake8-bandit/))
- [Safety](https://pyup.io/safety/), to check if some packages are insecure

#### Formatting

- [black](https://black.readthedocs.io/en/stable/), to format the code

#### Type checking

- [mypy](https://mypy-lang.org/), the classic type checker
- [pytype](https://google.github.io/pytype/), a static type checker
- [typeguard](https://typeguard.readthedocs.io/en/latest/), a runtime type check

#### Documentation

- [Sphinx](https://www.sphinx-doc.org/en/master/), the documentation tool used by the official Python documentation.
- [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html), Sphinx official plugin to generate API documentation from the docstrings.
- [napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html), Sphinx official plugin to allow compatibility with Google-style docstrings.
- [sphinx-autodoc-typehints](https://pypi.org/project/sphinx-autodoc-typehints/), Sphinx plugin to detect type hints in generated documentation.

### Specific Python tools

Tools to match specific needs of the projet.

#### UI

- [click](https://click.palletsprojects.com/en/8.1.x/), to create CLI applications

#### Communication

- [requests](https://requests.readthedocs.io/en/latest/), to make HTTP requests

#### Data validation

- [marshmallow](https://marshmallow.readthedocs.io/en/stable/), to serialize, deserialize and validate data
- ~~[dessert](https://desert.readthedocs.io/en/stable/), to generate marshmallow serialization schemas~~ → not used because too limited (can't work with data where fields names are different from the ones of the target dataclass)

I used [marshmallow](https://marshmallow.readthedocs.io/en/stable/) to follow the tutorial, but  [pydantic](https://docs.pydantic.dev/) is more known, and I find it easier to use.
