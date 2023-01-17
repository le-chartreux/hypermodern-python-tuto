import typing

import requests

import hypermodern_python.wikipedia.article


class WikipediaRequester:
    def __init__(self) -> None:
        self.__base_url = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"
        self.__language = "en"

    def get_random_article(self) -> hypermodern_python.wikipedia.article.WikipediaArticle:
        article_dict = self.__request_random_article_dict()
        return self.__article_dict_to_article(article_dict)

    def __request_random_article_dict(self) -> dict[typing.Any, typing.Any]:
        with requests.get(self.__get_url()) as response:
            response.raise_for_status()
            article = response.json()
        return article

    def __get_url(self) -> str:
        return self.__base_url.format(language=self.__language)

    @staticmethod
    def __article_dict_to_article(
            article_dict: dict[typing.Any, typing.Any]
    ) -> hypermodern_python.wikipedia.article.WikipediaArticle:
        title = article_dict["title"]
        summary = article_dict["extract"]
        return hypermodern_python.wikipedia.article.WikipediaArticle(title, summary)

    def set_language_to_french(self) -> None:
        self.__language = "fr"

    def set_language_to_english(self) -> None:
        self.__language = "en"
