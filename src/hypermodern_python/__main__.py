import textwrap

import click

import hypermodern_python
import hypermodern_python.wikipedia.requester


@click.command()
@click.version_option(version=hypermodern_python.__version__)
@click.option("--french/--english", is_flag=True, default=False,  help="Set the language of the page")
def main(french: bool):
    """The hypermodern Python project."""
    wikipedia_requester = hypermodern_python.wikipedia.requester.WikipediaRequester()
    if french:
        wikipedia_requester.set_language_to_french()
    wikipedia_article = wikipedia_requester.get_random_article()

    click.secho(wikipedia_article.title, fg="green")
    click.echo(textwrap.fill(wikipedia_article.summary))
