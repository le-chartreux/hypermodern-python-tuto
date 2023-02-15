import textwrap

import click

import hypermodern_python.wikipedia.article


def print_wikipedia_article(
    wikipedia_article: hypermodern_python.wikipedia.article.WikipediaArticle,
) -> None:
    click.secho(wikipedia_article.title, fg="green")
    click.echo(textwrap.fill(wikipedia_article.summary))
