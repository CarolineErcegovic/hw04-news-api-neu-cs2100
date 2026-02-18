"""
Article class which represents a news article from the News API.
"""

class Article:
    """
    Class to store details of a news article from the News API.

    Properties:
        url (str): The URL to the article
        source (str): The source of the article
        author (str): The author of the article
        title (str): The title of the article
        description (str): A brief description of the article
        published_at (str): The date and time the article was published
        content (str): The content of the article
    """

    def __init__(
            self, url: str, source: str, 
            author: str, title: str,
            description: str, published_at: str,
            content: str) -> None:
        """
        Initialize an Article object with the given attributes.

        Args:
            url (str): The URL to the article
            source (str): The source of the article
            author (str): The author of the article
            title (str): The title of the article
            description (str): A brief description of the article
            published_at (str): The date and time the article was published
            content (str): The content of the article
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the article of the format
        'Title by Author from Source on PublishedAt' """
        pass

    def __repr__(self) -> str:
        """Return a string representation of the article of the format
        "Article(title='...', author='...', source='...', publishedAt='...')" """
        pass
