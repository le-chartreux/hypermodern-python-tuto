"""Command-line interface."""
import click
import marshmallow
import requests

from hypermodern_python_tuto import __version__
from hypermodern_python_tuto.ui import print_wikipedia_article
from hypermodern_python_tuto.wikipedia.language import Language
from hypermodern_python_tuto.wikipedia.requester import WikipediaRequester


@click.command()
@click.version_option(version=__version__)
@click.option(
    "--language",
    type=click.Choice(list(Language), case_sensitive=False),
    help="Set the language of the page",
    default=Language.from_preferences(),
)
def main(language: Language) -> None:
    """Display the title and the summary of a random Wikipedia article."""
    wikipedia_requester = WikipediaRequester()
    wikipedia_requester.set_language(language)
    try:
        wikipedia_article = wikipedia_requester.get_random_article()
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message = str(error)
        raise click.ClickException(message) from error

    print_wikipedia_article(wikipedia_article)
