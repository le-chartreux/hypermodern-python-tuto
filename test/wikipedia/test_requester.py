"""Test cases for the requester module."""
import unittest.mock

import marshmallow
import pytest

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
