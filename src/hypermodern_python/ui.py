"""Utilities to show content to the user."""
import textwrap

import click

import hypermodern_python.wikipedia.article


def print_wikipedia_article(
    wikipedia_article: hypermodern_python.wikipedia.article.WikipediaArticle,
) -> None:
    """Shows an article to the standard text output.

    Prints in green the title, followed by the summary.

    Args:
        wikipedia_article: the article to print.
    """
    click.secho(wikipedia_article.title, fg="green")
    click.echo(textwrap.fill(wikipedia_article.summary))
