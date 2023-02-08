import nox


@nox.session(python=["3.10", "3.11"])
def tests(session: nox.sessions.Session) -> None:
    """Runs all the tests"""
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("poetry", "run", "pytest", *args, external=True)
