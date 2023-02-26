"""Command-line interface."""
import click
import marshmallow
import requests

import hypermodern_python
import hypermodern_python.ui
import hypermodern_python.wikipedia.language
import hypermodern_python.wikipedia.requester


@click.command()
@click.version_option(version=hypermodern_python.__version__)
@click.option(
    "--language",
    type=click.Choice(
        list(hypermodern_python.wikipedia.language.Language), case_sensitive=False
    ),
    help="Set the language of the page",
    default=hypermodern_python.wikipedia.language.Language.from_preferences(),
)
def main(language: hypermodern_python.wikipedia.language.Language) -> None:
    """Display the title and the summary of a random Wikipedia article."""
    wikipedia_requester = hypermodern_python.wikipedia.requester.WikipediaRequester()
    wikipedia_requester.set_language(language)
    try:
        wikipedia_article = wikipedia_requester.get_random_article()
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message = str(error)
        raise click.ClickException(message) from error

    hypermodern_python.ui.print_wikipedia_article(wikipedia_article)
