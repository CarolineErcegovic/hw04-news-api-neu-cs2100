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
        self.__url = url
        self.__source = source
        self.__author = author 
        self.__title = title 
        self.__description = description
        self.__published_at = published_at
        self.__content = content 

    @property
    def url(self) -> str:
        """Return the URL of the article."""
        return self.__url

    @property
    def source(self) -> str:
        """Return the source of the article."""
        return self.__source

    @property
    def author(self) -> str:
        """Return the author of the article."""
        return self.__author

    @property
    def title(self) -> str:
        """Return the title of the article."""
        return self.__title

    @property
    def description(self) -> str:
        """Return the description of the article."""
        return self.__description

    @property
    def published_at(self) -> str:
        """Return the publication date of the article."""
        return self.__published_at

    @property
    def content(self) -> str:
        """Return the content of the article."""
        return self.__content
    
    def __str__(self) -> str:
        """Return a string representation of the article of the format
        'Title by Author from Source on PublishedAt' """
        return f"{self.__title} by {self.__author} from {self.__source} on {self.__published_at}"

    def __repr__(self) -> str:
        """Return a string representation of the article of the format
        "Article(title='...', author='...', source='...', publishedAt='...')" """
        return (
            f"Article(title='{self.__title}', "
            f"author='{self.__author}', "
            f"source='{self.__source}', "
            f"publishedAt='{self.__published_at}')"
        )
