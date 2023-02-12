import hypermodern_python.wikipedia.article


def test_init() -> None:
    title = 'title'
    summary = 'summary'
    article = hypermodern_python.wikipedia.article.WikipediaArticle(title, summary)
    assert article.title == title
    assert article.summary == summary
