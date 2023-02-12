import hypermodern_python.wikipedia.requester
import hypermodern_python.language


def test_random_page_uses_given_language(mock_requests_get):
    requester = hypermodern_python.wikipedia.requester.WikipediaRequester()
    requester.set_language(hypermodern_python.language.Language.FRENCH)
    requester.get_random_article()
    args, _ = mock_requests_get.call_args
    assert 'fr.wikipedia.org' in args[0]
