"""Test cases for the article module."""
from hypermodern_python_tuto.wikipedia.article import WikipediaArticle


def test_init() -> None:
    """It initialises without raising an error and with the given values."""
    title = "title"
    summary = "summary"
    article = WikipediaArticle(title, summary)
    assert article.title == title
    assert article.summary == summary
