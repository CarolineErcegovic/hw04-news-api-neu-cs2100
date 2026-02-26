"""
Tests for the SearchNews class
"""

# pylint: disable=protected-access
import unittest
from typing import Any
from unittest.mock import patch, Mock

from src.search_news import SearchNews
from src.article import Article


class TestSearchNews(unittest.TestCase):
    """Tests for the SearchNews class"""

    def setUp(self) -> None:
        """Create a temporary API key file for testing."""
        with open("test_key.txt", "w", encoding="utf-8") as file:
            file.write("fake_api_key")

        self.search = SearchNews("test_key.txt")

    def tearDown(self) -> None:
        """Remove temporary API key file."""
        import os
        if os.path.exists("test_key.txt"):
            os.remove("test_key.txt")

    def test_create_articles_from_response(self) -> None:
        """Test that Article objects are correctly created from API response."""
        fake_response: dict[str, Any] = {
            "articles": [
                {
                    "url": "http://example.com",
                    "source": {"name": "Example Source"},
                    "author": "John Doe",
                    "title": "Test Title",
                    "description": "Test Description",
                    "publishedAt": "2023-10-01T10:00:00Z",
                    "content": "Test Content"
                }
            ]
        }

        articles = self.search._create_articles_from_response(fake_response)

        self.assertEqual(len(articles), 1)
        article = articles[0]

        self.assertIsInstance(article, Article)
        self.assertEqual(article.url, "http://example.com")
        self.assertEqual(article.source, "Example Source")
        self.assertEqual(article.author, "John Doe")
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.description, "Test Description")
        self.assertEqual(article.published_at, "2023-10-01T10:00:00Z")
        self.assertEqual(article.content, "Test Content")

    @patch("src.search_news.requests.get")
    def test_get_top_headlines_calls_api(self, mock_get: Mock) -> None:
        """Test that get_top_headlines makes a request and returns Article objects."""
        fake_json: dict[str, Any] = {
            "articles": [
                {
                    "url": "http://example.com",
                    "source": {"name": "Example Source"},
                    "author": "John Doe",
                    "title": "Headline Title",
                    "description": "Headline Description",
                    "publishedAt": "2023-10-01T10:00:00Z",
                    "content": "Headline Content"
                }
            ]
        }

        mock_response = Mock()
        mock_response.json.return_value = fake_json
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        articles = self.search.get_top_headlines("python")

        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, "Headline Title")

    @patch("src.search_news.requests.get")
    def test_get_everything_with_optional_params(self, mock_get: Mock) -> None:
        """Test get_everything includes optional parameters."""
        fake_json: dict[str, Any] = {"articles": []}

        mock_response = Mock()
        mock_response.json.return_value = fake_json
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        self.search.get_everything(
            "python",
            date="2023-01-01",
            domains=["example.com"],
            language="en"
        )

        args, kwargs = mock_get.call_args
        params = kwargs["params"]

        self.assertEqual(params["q"], "python")
        self.assertEqual(params["from"], "2023-01-01")
        self.assertEqual(params["domains"], "example.com")
        self.assertEqual(params["language"], "en")