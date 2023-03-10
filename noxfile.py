"""Nox sessions."""
import tempfile

import nox

nox.options.sessions = "lint", "test", "safety", "mypy", "doctest"
nox.options.reuse_existing_virtualenvs = True

package_location = "./src/hypermodern_python"
code_locations = package_location, "./test", "./noxfile.py"
python_versions = "3.10", "3.11"
latest_python = python_versions[-1]
python_versions_under_3_11 = [
    python_version for python_version in python_versions if python_version < "3.11"
]

runner = "poetry"


@nox.session(python=python_versions)
def test(session: nox.Session) -> None:
    """Run the test suite with pytest."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    _install(session)
    _run(session, "pytest", *args)


@nox.session(python=latest_python)
def lint(session: nox.Session) -> None:
    """Lint with flake8."""
    args = session.posargs or code_locations
    _install(session)
    _run(session, "flake8", *args)


@nox.session(python=latest_python)
def reformat(session: nox.Session) -> None:
    """Reformat with black."""
    formatter = "black"
    args = session.posargs or code_locations
    _install_only(session, formatter)
    _run(session, formatter, *args)


@nox.session(python=latest_python)
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
        )
        session.install("safety")
        session.run(
            "safety",
            "check",
            f"--file={requirements.name}",
            "--full-report",
        )


@nox.session(python=python_versions)
def mypy(session: nox.Session) -> None:
    """Static type-check using mypy."""
    args = session.posargs or code_locations
    _install(session)
    _run(session, "mypy", *args)


@nox.session(python=python_versions_under_3_11)
def pytype(session: nox.Session) -> None:
    """Static type-check using pytype."""
    args = session.posargs or ["--disable=import-error", *code_locations]
    _install(session)
    _run(session, "pytype", *args)


@nox.session(python=latest_python)
def typeguard(session: nox.Session) -> None:
    """Runtime type-check using typeguard (inside pytest)."""
    args = session.posargs or ["-m", "not e2e"]
    args.append("--typeguard-packages=hypermodern_python")
    _install(session)
    _run(session, "pytest", *args)


@nox.session(python=python_versions)
def doctest(session: nox.Session) -> None:
    """Run doctests with pytest."""
    args = session.posargs or [package_location]
    args.append("--doctest-modules")
    _install(session)
    _run(session, "pytest", *args)


@nox.session(python=python_versions)
def xdoctest(session: nox.Session) -> None:
    """Run doctests with xdoctest."""
    args = session.posargs or [package_location]
    _install(session)
    _run(session, "xdoctest", *args)


@nox.session(python=latest_python)
def docs(session: nox.Session) -> None:
    """Build the documentation."""
    _install(session)
    _run(session, "sphinx-build", "docs", "docs/_build")


@nox.session(python=latest_python)
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


def _install_only(session: nox.Session, group: str) -> None:
    _install(session, f"--only={group}")


def _install(session: nox.Session, *args: str) -> None:
    session.run(runner, "install", *args, external=True)


def _run(session: nox.Session, target: str, *args: str) -> None:
    session.run(runner, "run", target, *args, external=True)
