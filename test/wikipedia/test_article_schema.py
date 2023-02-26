from hypermodern_python.wikipedia.article import WikipediaArticle
from hypermodern_python.wikipedia.article_schema import WikipediaArticleSchema

title = "lorem"
extract = "ipsum"


def test_init() -> None:
    WikipediaArticleSchema()


def test_load_simple() -> None:
    schema = WikipediaArticleSchema()
    article = schema.load({"title": title, "extract": extract})
    _check_article_correct(article)


def test_load_with_unknown() -> None:
    schema = WikipediaArticleSchema()
    article = schema.load({"title": title, "extract": extract, "something": "unwanted"})
    _check_article_correct(article)


# utils part
def _check_article_correct(article: WikipediaArticle) -> None:
    assert isinstance(article, WikipediaArticle)
    assert article.title == title
    assert article.summary == extract
