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
    """Tests for the Article class"""

    def setUp(self) -> None:
        """Create a sample Article object"""
        self.article = Article(
            url="https://example.com/article",
            source="Example Source",
            author="John Doe",
            title="Example Title",
            description="Example description.",
            published_at="2023-10-01T12:00:00Z",
            content="Example content."
        )

    def test_properties(self) -> None:
        """Test that properties return correct values"""
        self.assertEqual(self.article.url, "https://example.com/article")
        self.assertEqual(self.article.source, "Example Source")
        self.assertEqual(self.article.author, "John Doe")
        self.assertEqual(self.article.title, "Example Title")
        self.assertEqual(self.article.description, "Example description.")
        self.assertEqual(self.article.published_at, "2023-10-01T12:00:00Z")
        self.assertEqual(self.article.content, "Example content.")

    def test_url_is_read_only(self) -> None:
        """Test that url property is read-only"""
        with self.assertRaises(AttributeError):
            self.article.url = "new_url"  # type: ignore

    def test_str(self) -> None:
        """Test __str__ format"""
        expected = "Example Title by John Doe from Example Source on 2023-10-01T12:00:00Z"
        self.assertEqual(str(self.article), expected)

    def test_repr(self) -> None:
        """Test __repr__ format"""
        expected = (
            "Article(title='Example Title', "
            "author='John Doe', "
            "source='Example Source', "
            "publishedAt='2023-10-01T12:00:00Z')"
        )
        self.assertEqual(repr(self.article), expected)
