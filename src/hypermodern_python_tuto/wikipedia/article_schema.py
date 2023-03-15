"""WikipediaArticleSchema class declaration."""
from typing import Any

import marshmallow

from hypermodern_python_tuto.wikipedia.article import WikipediaArticle


class WikipediaArticleSchema(marshmallow.Schema):
    """Validator for WikipediaArticle."""

    title = marshmallow.fields.String(required=True)
    extract = marshmallow.fields.String(required=True, attribute="summary")

    @marshmallow.post_load
    def make_article(self, data: dict[str, Any], **_kwargs: Any) -> WikipediaArticle:
        """Create a WikipediaArticle after the validation.

        Args:
            data: Validated data.
            **_kwargs: Unused args

        Returns:
            An instance of WikipediaArticle from the validated data.
        """
        return WikipediaArticle(**data)

    class Meta(marshmallow.schema.SchemaMeta):
        """Meta-information for marshmallow."""

        unknown = marshmallow.EXCLUDE
