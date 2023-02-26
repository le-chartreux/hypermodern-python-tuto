"""Test cases for the __main__ module."""
import unittest.mock

import click.testing
import pytest
import requests

from hypermodern_python.__main__ import main


@pytest.fixture
def runner() -> click.testing.CliRunner:
    """Fixture for invoking command-line interfaces."""
    return click.testing.CliRunner()


def test_main_succeeds(
    runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock
) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(main)
    assert result.exit_code == 0


def test_main_prints_title(
    runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock
) -> None:
    """It prints the title of the article it gets."""
    result = runner.invoke(main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(
    runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock
) -> None:
    """It invokes requests.get."""
    runner.invoke(main)
    assert mock_requests_get.called


def test_main_uses_correct_wikipedia_for_language(
    runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock
) -> None:
    """It requests to the Wikipedia version according to the given language."""
    expected_url_and_arg_to_use = (
        ("en.wikipedia.org", "--language english"),
        ("en.wikipedia.org", "--language something"),
        ("fr.wikipedia.org", "--language french"),
    )

    for expected_url, arg_to_use_language in expected_url_and_arg_to_use:
        runner.invoke(main, arg_to_use_language)
        args, _ = mock_requests_get.call_args
        assert expected_url in args[0]


def test_main_prints_message_on_request_error(
    runner: click.testing.CliRunner, mock_requests_get: unittest.mock.Mock
) -> None:
    """It prints an error message if a request fails."""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(main)
    assert "Error" in result.output


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner: click.testing.CliRunner) -> None:
    """It exits with a status code of zero (end-to-end)."""
    result = runner.invoke(main)
    assert result.exit_code == 0
