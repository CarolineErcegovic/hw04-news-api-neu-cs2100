"""
Tests for the NewsProcessor class
"""

import unittest
import sys
sys.path.append(".")
from src.news_processor import NewsProcessor
from src.article import Article

class TestNewsProcessor(unittest.TestCase):
    """Example test case for the NewsProcessor class"""
    def setUp(self) -> None:
        self.processor = NewsProcessor()
        self.articles = [
            Article(
                url="http://example.com/1",
                source="Example Source",
                author="Author A",
                title="Breaking News: Python is awesome",
                description="An article about Python.",
                published_at="2023-10-01T10:00:00Z",
                content="Full content of the article."
            ),
            Article(
                url="http://example.com/2",
                source="Example Source",
                author="Author B",
                title="Latest Updates on JavaScript",
                description="An article about JavaScript.",
                published_at="2023-10-02T12:00:00Z",
                content="Full content of the article."
            ),
            Article(
                url="http://example.com/3",
                source="Another Source",
                author="Author C",
                title="Python vs JavaScript: A Comparison",
                description="Comparing Python and JavaScript.",
                published_at="2023-10-03T14:00:00Z",
                content="Full content of the article."
            )
        ]

    def test_to_df_no_sort_no_filter(self) -> None:
        """Test that to_df returns a DataFrame with the correct columns and number of 
        rows when no sorting and no filtering is applied"""
        df = self.processor.to_df(self.articles)
        self.assertEqual(len(df), 3)
        self.assertListEqual(
            list(df.columns), 
            ['url', 'source', 'author', 'title', 'description', 'published_at', 'content'])

    def test_filter(self) -> None:
        """Test filtering functionality"""
        df = self.processor.to_df(
            self.articles,
            filter_func=lambda article: "Python" in article.title
        )
        self.assertEqual(len(df), 2)

    def test_sort(self) -> None:
        """Test sorting functionality"""
        df = self.processor.to_df(
            self.articles,
            sort_by=lambda article: article.author
        )

        authors = list(df["author"])
        self.assertEqual(authors, sorted(authors))