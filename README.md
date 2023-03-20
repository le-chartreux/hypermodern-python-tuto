# hypermodern-python-tuto

Repo to follow the Claudio Jolowicz's [tutorial about Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
It follows it until [this release](https://github.com/le-chartreux/hypermodern-python-tuto/releases/tag/v1.0.3). After this one, I started adding further tools, deleting some that I consider useless and replacing some others.

---

<table>
    <tr>
        <td>
            <b>Package</b>
        </td>
        <td>
            <a href="https://pypi.org/project/hypermodern-python-tuto/">
                <img src="https://img.shields.io/pypi/pyversions/hypermodern-python-tuto.svg" alt="Supported Python Versions">
            </a>
            <a href="https://pypi.org/project/hypermodern-python-tuto/">
                <img src="https://img.shields.io/pypi/v/hypermodern-python-tuto.svg" alt="PyPI version">
            </a>
            <a href="https://pypi.org/project/hypermodern-python-tuto/">
                <img src="https://img.shields.io/pypi/dm/hypermodern-python-tuto.svg" alt="PyPI downloads">
            </a>
        </td>
    </tr>
    <tr>
        <td>
            <b>CI</b>
        </td>
        <td>
            <a href="https://github.com/le-chartreux/hypermodern-python-tuto/actions?workflow=Tests">
                <img src="https://github.com/le-chartreux/hypermodern-python-tuto/workflows/Tests/badge.svg" alt="Tests status">
            </a>
            <a href="https://hypermodern-python-tuto.readthedocs.io/">
                <img src="https://readthedocs.org/projects/hypermodern-python-tuto/badge/" alt="Documentation status">
            </a>
            <a href="https://codecov.io/gh/le-chartreux/hypermodern-python-tuto">
                <img src="https://codecov.io/gh/le-chartreux/hypermodern-python-tuto/branch/master/graph/badge.svg" alt="Coverage status">
            </a>
        </td>
    </tr>
    <tr>
        <td>
            <b>Code</b>
        </td>
        <td>
            <a href="https://github.com/psf/black">
                <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code quality">
            </a>
            <a href="https://github.com/pre-commit/pre-commit">
                <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen" alt="pre-commit">
            </a>
        </td>
    </tr>
</table>

---

## Table of contents

- [Overview](#overview)
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

## Overview

The app created is a CLI application that queries a random Wikipedia page and displays its title and summary.

## Install

```shell
pip install hypermodern-python-tuto
```

## Use

### Basic usage

Just run the following command:

```shell
hypermodern-python-tuto
```

### Other options

Look at the [documentation](https://hypermodern-python-tuto.readthedocs.io/).

## Tools used

### Generic tools

Tools that can be used in every development project, no matter if it's a Python project or not.

- [git](https://git-scm.com/), to manage versions of the source code
- [GitHub](https://github.com/le-chartreux/hypermodern-python-tuto), to host the git repository and automate tasks with [GitHub Actions](https://docs.github.com/en/actions):
  - [Release Drafter](https://github.com/marketplace/actions/release-drafter), to create release templates
- [pre-commit](https://pre-commit.com/), to manage pre-commit hooks
- [Codecov](https://about.codecov.io/), to mesure code coverage on repos

### Generic Python tools

Tools that can be used in every Python project, no matter its content.

#### Multi-purpose

- [PyPI](https://pypi.org/), to install and publish Python packages
- [TestPyPI](https://pypi.org/), PyPI but for testing purposes
- [poetry](https://python-poetry.org/), to make development and distribution easy (packaging, virtualization, dependencies, launching and publishing)
- [nox](https://nox.thea.codes/en/stable/), to run tasks in multiple Python environments (like tests, linting, reformatting, etc.)

#### Setup

- [pyenv](https://github.com/pyenv/pyenv), to manage Python versions

#### Test

- [pytest](https://docs.pytest.org/en/latest/), a framework to write unit tests. Also used to run doctests
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/), to mesure the code coverage (degree to which the source code of a program is executed while running its test suite)
- [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/), to use the [unittest](https://docs.python.org/3/library/unittest.html) mocking in the pytest way

#### Linting

- [flake8](https://flake8.pycqa.org/en/latest/), a linter aggregator
- [flake8-isort](https://pypi.org/project/flake8-isort/), to verify that imports are grouped and ordered in a consistent way
- [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear), to find bugs and design problems
- [flake8-annotations](https://pypi.org/project/flake8-annotations/), to detect the absence of type annotations
- [flake8-black](https://pypi.org/project/flake8-black/), to check if the code follows [black](https://black.readthedocs.io/en/stable/) formatting
- [flake8-docstrings](https://pypi.org/project/flake8-docstrings/), to check that the code is correctly documented
- [flake8-pytest-style](https://pypi.org/project/flake8-pytest-style/), to check style issues with pytest-based tests
- [darglint](https://pypi.org/project/darglint/), to check that docstrings match function definitions

#### Security

- [Bandit](https://bandit.readthedocs.io/en/latest/), to find security issues (used inside linting with [flake8-bandit](https://pypi.org/project/flake8-bandit/))
- [Safety](https://pyup.io/safety/), to check if some packages are insecure

#### Formatting

- [black](https://black.readthedocs.io/en/stable/), to format the code
- [isort](https://pycqa.github.io/isort/index.html), to sort imports

#### Type checking

- [mypy](https://mypy-lang.org/), the classic type checker
- [typeguard](https://typeguard.readthedocs.io/en/latest/), a runtime type checker

#### Documentation

- [Sphinx](https://www.sphinx-doc.org/en/master/), the documentation tool used by the official Python documentation.
- [Read the Docs](https://readthedocs.org/), to host the documentation.
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

I used [marshmallow](https://marshmallow.readthedocs.io/en/stable/) to follow the tutorial, but  [pydantic](https://docs.pydantic.dev/) is more known, and I find it easier to use.
