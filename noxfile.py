"""Nox sessions."""
import tempfile

import nox

nox.options.sessions = "pytest", "doctest", "ruff", "safety", "mypy"
nox.options.reuse_existing_virtualenvs = True
silent_default = True
silent_format = False

package_location = "./src/hypermodern_python_tuto"
code_locations = package_location, "./test", "./noxfile.py"
python_versions = "3.10", "3.11"
latest_python = python_versions[-1]

runner = "poetry"


@nox.session(python=python_versions, tags=["test"])
def pytest(session: nox.Session) -> None:
    """Run the test suite with pytest."""
    args = session.posargs or ("--cov", "-m", "not e2e")
    _install(session)
    _run(session, "pytest", *args)


@nox.session(python=python_versions, tags=["test"])
def doctest(session: nox.Session) -> None:
    """Run doctests with pytest."""
    session.notify(f"pytest-{session.python}", (package_location, "--doctest-modules"))


@nox.session(python=latest_python, tags=["lint"])
def ruff(session: nox.Session) -> None:
    """Lint with Ruff."""
    args = session.posargs or code_locations
    _install(session)
    _run(session, "ruff", "check", *args)


@nox.session(python=latest_python, tags=["format"])
def black(session: nox.Session) -> None:
    """Reformat with black."""
    args = session.posargs or code_locations
    _install(session)
    _run(session, "black", *args, silent=silent_format)


@nox.session(python=latest_python, tags=["format"])
def isort(session: nox.Session) -> None:
    """Reformat the import order with isort."""
    args = session.posargs or code_locations
    _install(session)
    _run(session, "isort", *args, silent=silent_format)


@nox.session(python=latest_python, tags=["security"])
def safety(session: nox.Session) -> None:
    """Scan dependencies for insecure packages."""
    # not within poetry because it conflicts with black
    # (and since its safety there is no reason to not use the latest)
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            runner,
            "export",
            "--with",
            "dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
            silent=silent_default,
        )
        session.install("safety")
        session.run(
            "safety",
            "check",
            f"--file={requirements.name}",
            "--full-report",
            silent=silent_default,
        )


@nox.session(python=python_versions, tags=["typecheck"])
def mypy(session: nox.Session) -> None:
    """Verify types using mypy (so it is static)."""
    args = session.posargs or code_locations
    _install(session)
    _run(session, "mypy", *args)


@nox.session(python=latest_python, tags=["documentation"])
def docs(session: nox.Session) -> None:
    """Build the documentation."""
    _install(session)
    _run(session, "sphinx-build", "docs", "docs/_build")


@nox.session(python=latest_python, tags=["ci"])
def coverage(session: nox.Session) -> None:
    """Upload coverage data."""
    args = session.posargs or [
        "--cov",
        "-m",
        "not e2e",
        "--cov-report=xml",
        "--cov-fail-under=0",
    ]
    _install(session)
    _run(session, "pytest", *args)


# everything after this line is utils
def _install(session: nox.Session, *args: str) -> None:
    session.run(runner, "install", *args, external=True, silent=silent_default)


def _run(
    session: nox.Session, target: str, *args: str, silent: bool = silent_default
) -> None:
    session.run(runner, "run", target, *args, external=True, silent=silent)
