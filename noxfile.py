import tempfile

import nox

nox.options.sessions = "lint", "tests", "safety", "mypy"

code_locations = "src", "test", "./noxfile.py"
python_versions = "3.10", "3.11"
latest_python = python_versions[-1]

runner = "poetry"


@nox.session(python=python_versions)
def tests(session: nox.sessions.Session) -> None:
    """Runs all the tests"""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run(runner, "install", "--with", "dev", external=True)
    session.run(runner, "run", "pytest", *args, external=True)


@nox.session(python=latest_python)
def lint(session: nox.sessions.Session) -> None:
    """Runs linting"""
    linter = "flake8"
    linter_plugins = (
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    args = session.posargs or code_locations
    session.install(linter, *linter_plugins)
    session.run(linter, *args)


@nox.session(python=latest_python)
def reformat(session: nox.sessions.Session) -> None:
    """Runs code formatting"""
    formatter = "black"
    args = session.posargs or code_locations
    session.install(formatter)
    session.run(formatter, *args)


@nox.session(python=latest_python)
def safety(session: nox.sessions.Session):
    """Runs Safety on the project"""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with",
            "dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=python_versions)
def mypy(session: nox.sessions.Session):
    args = session.posargs or code_locations
    session.install("mypy")
    session.install("types-requests")
    session.run("mypy", *args)
