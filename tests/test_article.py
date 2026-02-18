"""
Tests for the Article class
"""

import unittest
import sys
sys.path.append(".")
from src.article import Article

# You may use # type: ignore to ignore the mypy error when accessing a 
# read-only property (which should raise an AttributeError).

class TestArticle(unittest.TestCase):
    """Example test case for the Article class"""
    def test_url_is_read_only(self) -> None:
        """Test that the url property is set correctly"""
        article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="This is an example description.",
            published_at="2023-10-01T12:00:00Z",
            content="This is the content of the example article."
        )
        self.assertEqual(article.url, "https://example.com/article")
        with self.assertRaises(AttributeError):
            article.url = "https://example.com/new-article" # type: ignore
        self.assertEqual(article.url, "https://example.com/article")
