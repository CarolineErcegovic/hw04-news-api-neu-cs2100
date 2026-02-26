"""
Tests for the NewsProcessor class
"""

# pylint: disable=protected-access
import unittest
import sys
sys.path.append(".")

from src.news_processor import NewsProcessor
from src.article import Article


class TestNewsProcessor(unittest.TestCase):
    """Tests for the NewsProcessor class"""

    def setUp(self) -> None:
        """Create a NewsProcessor instance and sample articles."""
        self.processor = NewsProcessor()
        self.articles = [
            Article(
                url="http://example.com/1",
                source="Example Source",
                author="ZZZ Author",
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
                author="AAA Author",
                title="Python vs JavaScript: A Comparison",
                description="Comparing Python and JavaScript.",
                published_at="2023-10-03T14:00:00Z",
                content="Full content of the article."
            )
        ]

    def test_to_df_no_sort_no_filter(self) -> None:
        """Test to_df without sorting or filtering."""
        df = self.processor.to_df(self.articles)
        self.assertEqual(len(df), 3)
        self.assertListEqual(
            list(df.columns),
            ["url", "source", "author", "title", "description", "published_at", "content"]
        )

    def test_filter(self) -> None:
        """Test filtering functionality."""
        df = self.processor.to_df(
            self.articles,
            filter_func=lambda article: "Python" in article.title
        )

        titles = list(df["title"])
        self.assertEqual(
            titles,
            [
                "Breaking News: Python is awesome",
                "Python vs JavaScript: A Comparison"
            ]
        )

    def test_sort(self) -> None:
        """Test sorting functionality."""
        df = self.processor.to_df(
            self.articles,
            sort_by=lambda article: article.author
        )

        authors = list(df["author"])
        self.assertEqual(authors, ["AAA Author", "Author B", "ZZZ Author"])

    def test_sort_and_filter(self) -> None:
        """Test sorting and filtering together."""
        df = self.processor.to_df(
            self.articles,
            sort_by=lambda article: article.author,
            filter_func=lambda article: "Python" in article.title
        )

        authors = list(df["author"])
        self.assertEqual(authors, ["AAA Author", "ZZZ Author"])

    def test_filter_no_matches(self) -> None:
        """Test filtering when no matches exist."""
        df = self.processor.to_df(
            self.articles,
            filter_func=lambda article: "Ruby" in article.title
        )
        self.assertEqual(len(df), 0)

    def test_filter_and_sort_both_applied(self) -> None:
        """Ensure both filtering and sorting are applied."""
        articles = [
            Article("1", "S", "B Author", "Match", "", "2023-01-01T00:00:00Z", ""),
            Article("2", "S", "A Author", "Match", "", "2023-01-02T00:00:00Z", ""),
            Article("3", "S", "C Author", "No Match", "", "2023-01-03T00:00:00Z", ""),
        ]

        df = self.processor.to_df(
            articles,
            sort_by=lambda a: a.author,
            filter_func=lambda a: a.title == "Match"
        )

        self.assertEqual(len(df), 2)
        self.assertListEqual(
            list(df["author"]),
            ["A Author", "B Author"]
        )

    def test_sort_with_filter_none_explicit(self) -> None:
        """Test sorting when filter_func is explicitly None."""
        df = self.processor.to_df(
            self.articles,
            sort_by=lambda article: article.author,
            filter_func=None
        )

        authors = list(df["author"])
        self.assertEqual(authors, ["AAA Author", "Author B", "ZZZ Author"])

    def test_filter_with_sort_none_explicit(self) -> None:
        """Test filtering when sort_by is explicitly None."""
        df = self.processor.to_df(
            self.articles,
            sort_by=None,
            filter_func=lambda article: "Python" in article.title
        )

        titles = list(df["title"])
        self.assertEqual(
            titles,
            [
                "Breaking News: Python is awesome",
                "Python vs JavaScript: A Comparison"
            ]
        )
    
    def test_dataframe_values_match_article(self) -> None:
        """Ensure DataFrame values match Article attributes logically."""
        df = self.processor.to_df(self.articles)

        first_row = df.iloc[0]

        self.assertEqual(first_row["url"], self.articles[0].url)
        self.assertEqual(first_row["source"], self.articles[0].source)
        self.assertEqual(first_row["author"], self.articles[0].author)
        self.assertEqual(first_row["title"], self.articles[0].title)
        self.assertEqual(first_row["description"], self.articles[0].description)
        self.assertTrue(str(first_row["published_at"]).startswith("2023-10-01"))
        self.assertEqual(first_row["content"], self.articles[0].content)