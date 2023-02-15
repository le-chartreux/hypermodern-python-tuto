import typing

import requests

from hypermodern_python.wikipedia.article import WikipediaArticle
from hypermodern_python.language import Language


class WikipediaRequester:
    def __init__(self) -> None:
        self.__base_url = 'https://{language}.wikipedia.org/api/rest_v1/page/random/summary'
        self.__language = 'en'

    def get_random_article(self) -> WikipediaArticle:
        article_dict = self._request_random_article_dict()
        return self._article_dict_to_article(article_dict)

    def _request_random_article_dict(self) -> dict[typing.Any, typing.Any]:
        with requests.get(self._get_url()) as response:
            response.raise_for_status()
            article = response.json()
        return article

    def _get_url(self) -> str:
        return self.__base_url.format(language=self.__language)

    @staticmethod
    def _article_dict_to_article(
            article_dict: dict[typing.Any, typing.Any]
    ) -> WikipediaArticle:
        title = article_dict['title']
        summary = article_dict['extract']
        return WikipediaArticle(title, summary)

    def set_language(self, language: Language) -> None:
        if language is Language.FRENCH:
            self.__language = 'fr'
        else:
            self.__language = 'en'
