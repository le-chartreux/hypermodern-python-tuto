"""WikipediaArticle class declaration."""
import dataclasses


@dataclasses.dataclass
class WikipediaArticle:
    """Representation of the information needed about a Wikipedia article.

    Attributes:
        title: The title of the Wikipedia page.
        summary: A plain text summary.
    """

    title: str
    summary: str
