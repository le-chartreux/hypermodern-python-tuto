import click.testing
import pytest

import hypermodern_python.__main__


@pytest.fixture
def runner() -> click.testing.CliRunner:
    return click.testing.CliRunner()


def test_main_succeeds(runner: click.testing.CliRunner) -> None:
    result = runner.invoke(hypermodern_python.__main__.main)
    assert result.exit_code == 0
