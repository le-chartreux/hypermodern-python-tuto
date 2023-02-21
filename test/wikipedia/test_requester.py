import unittest.mock

import marshmallow
import pytest

from hypermodern_python.wikipedia.language import Language
from hypermodern_python.wikipedia.requester import WikipediaRequester


def test_random_page_uses_given_language(mock_requests_get: unittest.mock.MagicMock):
    requester = WikipediaRequester()
    requester.set_language(Language.FRENCH)
    requester.get_random_article()
    args, _ = mock_requests_get.call_args
    assert "fr.wikipedia.org" in args[0]


def test_random_page_handles_validation_errors(
    mock_requests_get: unittest.mock.MagicMock,
) -> None:
    mock_requests_get.return_value.__enter__.return_value.json.return_value = {}
    with pytest.raises(marshmallow.ValidationError):
        WikipediaRequester().get_random_article()
