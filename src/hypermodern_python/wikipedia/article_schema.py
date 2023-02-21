import marshmallow

from hypermodern_python.wikipedia.article import WikipediaArticle


class WikipediaArticleSchema(marshmallow.Schema):
    title = marshmallow.fields.String()
    extract = marshmallow.fields.String(attribute="summary")

    @marshmallow.post_load
    def make_article(self, data, **_kwargs) -> WikipediaArticle:
        return WikipediaArticle(**data)

    class Meta:
        unknown = marshmallow.EXCLUDE
