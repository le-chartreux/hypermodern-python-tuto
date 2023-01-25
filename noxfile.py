import nox


@nox.session(python=["3.10", "3.11"], reuse_venv=True)
def tests(session: nox.sessions.Session) -> None:
    """Runs all the tests"""
    args = session.posargs or ["--cov"]
    session.install("poetry")
    session.run("poetry", "install", external=True)
    session.run("pytest", *args, external=True)
