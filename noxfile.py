import nox


@nox.session(python=["3.10", "3.11"])
def tests(session: nox.sessions.Session) -> None:
    """Runs all the tests"""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--with", "dev", external=True)
    session.run("poetry", "run", "pytest", *args, external=True)
