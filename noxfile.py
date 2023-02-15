import nox

nox.options.sessions = "lint", "tests"

code_locations = "src", "test", "noxfile.py"
python_versions = "3.10", "3.11"
latest_python = python_versions[-1]


@nox.session(python=python_versions)
def tests(session: nox.sessions.Session) -> None:
    """Runs all the tests"""
    runner = "poetry"
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run(runner, "install", "--with", "dev", external=True)
    session.run(runner, "run", "pytest", *args, external=True)


@nox.session(python=latest_python)
def lint(session: nox.sessions.Session) -> None:
    """Runs linting"""
    linter = "flake8"
    linter_plugins = "flake8-black"
    args = session.posargs or code_locations
    session.install(linter, linter_plugins)
    session.run(linter, *args)


@nox.session(python=latest_python)
def reformat(session: nox.sessions.Session) -> None:
    """Runs code formatting"""
    formatter = "black"
    args = session.posargs or code_locations
    session.install(formatter)
    session.run(formatter, *args)
