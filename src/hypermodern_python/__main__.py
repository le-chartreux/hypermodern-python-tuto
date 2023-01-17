import click

import hypermodern_python
import hypermodern_python.ui
import hypermodern_python.wikipedia.requester


@click.command()
@click.version_option(version=hypermodern_python.__version__)
@click.option("--french/--english", is_flag=True, default=False,  help="Set the language of the page")
def main(french: bool) -> None:
    """
    Displays the title and the summary of a random Wikipedia article

    :param french: whether the language of the Wikipedia page should be French, else English
    """
    wikipedia_requester = hypermodern_python.wikipedia.requester.WikipediaRequester()
    if french:
        wikipedia_requester.set_language_to_french()
    wikipedia_article = wikipedia_requester.get_random_article()

    hypermodern_python.ui.print_wikipedia_article(wikipedia_article)
