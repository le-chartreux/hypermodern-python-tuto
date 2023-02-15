import nox

code_locations = "src", "test", "noxfile.py"
python_versions = "3.10", "3.11"


@nox.session(python=python_versions)
def tests(session: nox.sessions.Session) -> None:
    """Runs all the tests"""
    runner = "poetry"
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run(runner, "install", "--with", "dev", external=True)
    session.run(runner, "run", "pytest", *args, external=True)


@nox.session(python=python_versions)
def lint(session: nox.sessions.Session) -> None:
    """Runs linting"""
    linter = "flake8"
    args = session.posargs or code_locations
    session.install(linter)
    session.run(linter, *args)
