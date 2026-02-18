"""
Module to interact with the News API and retrieve news articles.
"""

from typing import Optional, Any
import requests
from src.article import Article


class SearchNews:
    """
    Class to interact with the News API and retrieve news articles.
    """

    def __init__(self, api_key_file: str):
        """
        Initialize SearchNews by reading API key from file.

        Args:
            api_key_file (str): Path to file containing the API key
        
        Raises:
            FileNotFoundError: If the API key file does not exist
        """
        pass

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
        # TODO: Implement API call to /top-headlines endpoint
        # Base URL: https://newsapi.org/v2/top-headlines
        # Remember to include your API key in the request parameters
        # Parse JSON response and create Article objects
        pass

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
        # TODO: Implement API call to /everything endpoint
        # Base URL: https://newsapi.org/v2/everything
        # Remember to include your API key in the request parameters
        # Parse JSON response and create Article objects
        pass

    def _make_request(self, endpoint: str, params: dict[str, str]) -> Any:
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
        # TODO: Implement helper method for making API requests
        # This can reduce code duplication between get_top_headlines and get_everything
        pass
        

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
        # TODO: Parse the 'articles' field from response and create Article objects
        pass
