import click.testing
import pytest

import hypermodern_python.__main__


@pytest.fixture
def runner() -> click.testing.CliRunner:
    return click.testing.CliRunner()


def test_main_succeeds(runner: click.testing.CliRunner, mock_requests_get) -> None:
    result = runner.invoke(hypermodern_python.__main__.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(hypermodern_python.__main__.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(runner, mock_requests_get):
    runner.invoke(hypermodern_python.__main__.main)
    assert mock_requests_get.called


def test_main_uses_correct_wikipedia_for_language(runner, mock_requests_get):
    expected_url_and_arg_to_use = (
        ("en.wikipedia.org", "--language english"),
        ("en.wikipedia.org", "--language someting"),
        ("fr.wikipedia.org", "--language french")
    )

    for expected_url, arg_to_use_language in expected_url_and_arg_to_use:
        runner.invoke(hypermodern_python.__main__.main, arg_to_use_language)
        args, _ = mock_requests_get.call_args
        assert expected_url in args[0]


def test_main_prints_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(hypermodern_python.__main__.main)
    assert "Error" in result.output
