from hypermodern_python.wikipedia.article import WikipediaArticle


def test_init() -> None:
    title = "title"
    summary = "summary"
    article = WikipediaArticle(title, summary)
    assert article.title == title
    assert article.summary == summary
