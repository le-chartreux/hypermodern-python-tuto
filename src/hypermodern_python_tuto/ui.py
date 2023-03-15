"""Utilities to show content to the user."""
import textwrap

import click

import hypermodern_python_tuto.wikipedia.article


def print_wikipedia_article(
    wikipedia_article: hypermodern_python_tuto.wikipedia.article.WikipediaArticle,
) -> None:
    """Show an article on the standard text output.

    Prints in green the title, followed by the summary.

    Args:
        wikipedia_article: the article to print.

    Examples:
        >>> article = hypermodern_python_tuto.wikipedia.article.WikipediaArticle("a", "b")
        >>> print_wikipedia_article(article)
        a
        b
    """
    click.secho(wikipedia_article.title, fg="green")
    click.echo(textwrap.fill(wikipedia_article.summary))
