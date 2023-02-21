import tempfile

import nox

nox.options.sessions = "lint", "tests", "safety", "mypy", "pytype"

code_locations = "src", "test", "./noxfile.py"
python_versions = "3.10", "3.11"
latest_python = python_versions[-1]
python_versions_under_3_11 = [
    python_version for python_version in python_versions if python_version < "3.11"
]

runner = "poetry"


@nox.session(python=python_versions)
def tests(session: nox.Session) -> None:
    tester = "pytest"
    args = session.posargs or ["--cov", "-m", "not e2e"]
    install_with(session, tester)
    run(session, tester, *args)


@nox.session(python=latest_python)
def lint(session: nox.Session) -> None:
    linter = "flake8"
    args = session.posargs or code_locations
    install_only(session, linter)
    run(session, linter, *args)


@nox.session(python=latest_python)
def reformat(session: nox.Session) -> None:
    formatter = "black"
    args = session.posargs or code_locations
    install_only(session, formatter)
    run(session, formatter, *args)


@nox.session(python=latest_python)
def safety(session: nox.Session) -> None:
    # not with poetry because it conflicts with blake
    # (+ since its safety there is no reason to not take the latest)
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
    target = "mypy"
    args = session.posargs or code_locations
    install_with(session, target)
    run(session, target, *args)


@nox.session(python=python_versions_under_3_11)
def pytype(session: nox.Session) -> None:
    target = "pytype"
    args = session.posargs or ["--disable=import-error", *code_locations]
    install_with(session, target)
    run(session, target, *args)


# everything after this line is utils
def install_with(session: nox.Session, group: str) -> None:
    install(session, "--with", group)


def install_only(session: nox.Session, group: str) -> None:
    install(session, f"--only={group}")


def install(session: nox.Session, *args) -> None:
    session.run(runner, "install", *args, external=True)


def run(session: nox.Session, target: str, *args) -> None:
    session.run(runner, "run", target, *args, external=True)
