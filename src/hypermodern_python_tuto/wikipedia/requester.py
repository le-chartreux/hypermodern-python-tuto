"""WikipediaRequester class declaration."""
from typing import Any, Final

import requests

from hypermodern_python_tuto.wikipedia.article import WikipediaArticle
from hypermodern_python_tuto.wikipedia.article_schema import WikipediaArticleSchema
from hypermodern_python_tuto.wikipedia.language import Language


class WikipediaRequester:
    """Class to get information from Wikipedia."""

    def __init__(self) -> None:
        """Set up the WikipediaRequester."""
        self.__base_url: Final = (
            "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"
        )
        self.__language = "en"

    def get_random_article(self) -> WikipediaArticle:
        """Query a random article from Wikipedia.

        Returns:
            A random article from Wikipedia (WikipediaArticle)

        Example:
            >>> requester = WikipediaRequester()
            >>> article = requester.get_random_article()
            >>> bool(article)
            True
        """
        article_dict = self._request_random_article_dict()
        return self._article_dict_to_article(article_dict)

    def _request_random_article_dict(self) -> dict[Any, Any]:
        with requests.get(self._get_url(), timeout=5) as response:
            response.raise_for_status()
            article = response.json()
        return article

    def _get_url(self) -> str:
        return self.__base_url.format(language=self.__language)

    @staticmethod
    def _article_dict_to_article(article_dict: dict[Any, Any]) -> WikipediaArticle:
        schema = WikipediaArticleSchema()
        return schema.load(article_dict)

    def set_language(self, language: Language) -> None:
        """Specify the desired language of Wikipedia.

        Args:
            language: the desired language of Wikipedia. Default is English.
        """
        if language is Language.FRENCH:
            self.__language = "fr"
        else:
            self.__language = "en"
