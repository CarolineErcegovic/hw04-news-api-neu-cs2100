"""
Module to interact with the News API and retrieve news articles.
"""

from typing import Optional, Any, cast
import requests
from src.article import Article


class SearchNews:
    """
    Class to interact with the News API and retrieve news articles.
    """

    def __init__(self, api_key_file: str) -> None:
        """
        Initialize SearchNews by reading API key from file.

        Args:
            api_key_file (str): Path to file containing the API key

        Raises:
            FileNotFoundError: If the API key file does not exist
        """
        with open(api_key_file, "r", encoding="utf-8") as file:
            self.__api_key: str = file.read().strip()

    def get_top_headlines(self, *terms: str) -> list[Article]:
        """
        Get top headlines from the News API.

        Args:
            *terms (str): Variable number of search terms

        Returns:
            list[Article]: List of Article objects
        
        Raises:
            requests.exceptions.RequestException: If the API request fails
            KeyError: If expected keys are missing in the API response data
        """
        
        query = " ".join(terms)

        params: dict[str, str] = {
            "q": query,
            "apiKey": self.__api_key
        }

        response_data = self._make_request("top-headlines", params)
        return self._create_articles_from_response(response_data)

    def get_everything(
        self,
        *terms: str,
        date: Optional[str] = None,
        domains: Optional[list[str]] = None,
        language: Optional[str] = None
    ) -> list[Article]:
        """
        Get everything from the News API.

        Args:
            date (Optional[str]): Optional date filter (YYYY-MM-DD format)
            domains (Optional[list[str]]): Optional domain filter (e.g., 'bbc.co.uk')
            language (Optional[str]): Optional language filter (e.g., 'en')
            *terms (str): Variable number of search terms

        Returns:
            list[Article]: List of Article objects
        
        Raises:
            requests.exceptions.RequestException: If the API request fails
            KeyError: If expected keys are missing in the API response data
        """
        query = " ".join(terms)

        params: dict[str, str] = {
            "q": query,
            "apiKey": self.__api_key
        }

        if date is not None:
            params["from"] = date

        if domains is not None:
            params["domains"] = ",".join(domains)

        if language is not None:
            params["language"] = language

        response_data = self._make_request("everything", params)
        return self._create_articles_from_response(response_data)

    def _make_request(self, endpoint: str, params: dict[str, str]) -> dict[str, Any]:
        """
        Helper method to make API requests.

        Args:
            endpoint (str): API endpoint (e.g., 'top-headlines')
            params (dict[str, str]): Query parameters for the request

        Returns:
            dict[str, Any]: Dictionary of JSON response

        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        base_url = "https://newsapi.org/v2/"
        url = base_url + endpoint

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        return cast(dict[str, Any], response.json())
        

    def _create_articles_from_response(self, response_data: dict[str, Any]) -> list[Article]:
        """
        Helper method to create Article objects from API response.

        Args:
            response_data (dict[str, Any]): JSON response from API

        Returns:
            list[Article]: List of Article objects
        
        Raises:
            KeyError: If expected keys are missing in the response data
        """
        articles: list[Article] = []

        for item in response_data["articles"]:
            article = Article(
                url=item["url"],
                source=item["source"]["name"],
                author=item["author"],
                title=item["title"],
                description=item["description"],
                published_at=item["publishedAt"],
                content=item["content"]
            )
            articles.append(article)

        return articles
