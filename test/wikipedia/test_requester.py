"""Test cases for the requester module."""
import unittest.mock

import marshmallow
import pytest
import pytest_mock

from hypermodern_python_tuto.wikipedia.language import Language
from hypermodern_python_tuto.wikipedia.requester import WikipediaRequester


def test_random_page_uses_given_language(mock_requests_get: unittest.mock.Mock) -> None:
    """It selects the Wikipedia to request from the given language."""
    requester = WikipediaRequester()
    requester.set_language(Language.FRENCH)
    requester.get_random_article()
    args, _ = mock_requests_get.call_args
    assert "fr.wikipedia.org" in args[0]


def test_random_page_handles_validation_errors(
    mock_requests_get: unittest.mock.Mock,
) -> None:
    """It raises a ValidationError when the data is invalidated."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = {}
    with pytest.raises(marshmallow.ValidationError):
        WikipediaRequester().get_random_article()


def test__request_random_article_dict_handles_unexpected_response_content(
    mock_requests_get: unittest.mock.Mock,
) -> None:
    """It raises a ValueError when the response's content is not a dict."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = 13
    expected_error_message = (
        "Error when requesting an article: expecting the response to contain a "
        "dictionary, got a <class 'int'>. Content is 13."
    )
    with pytest.raises(ValueError, match=expected_error_message):
        WikipediaRequester()._request_random_article_dict()


def test__article_dict_to_article_handles_unexpected_schema_load(
    mocker: pytest_mock.MockFixture,
) -> None:
    """It raises a ValueError if WikipediaArticleSchema.load don't return a WikipediaArticle."""
    mock_schema_load = mocker.patch(
        "hypermodern_python_tuto.wikipedia.article_schema.WikipediaArticleSchema.load"
    )
    mock_schema_load.return_value = "toto"
    expected_error_message = (
        "Error when loading with WikipediaArticleSchema: expected result type "
        "is WikipediaArticle, got a <class 'str'> and result is toto."
    )
    with pytest.raises(ValueError, match=expected_error_message):
        WikipediaRequester._article_dict_to_article({})
