from typing import Any

import marshmallow

from hypermodern_python.wikipedia.article import WikipediaArticle


class WikipediaArticleSchema(marshmallow.Schema):
    """Validator for WikipediaArticle."""

    title = marshmallow.fields.String(required=True)
    extract = marshmallow.fields.String(required=True, attribute="summary")

    @marshmallow.post_load
    def make_article(self, data: dict[str, Any], **_kwargs: Any) -> WikipediaArticle:
        return WikipediaArticle(**data)

    class Meta(marshmallow.schema.SchemaMeta):
        unknown = marshmallow.EXCLUDE
