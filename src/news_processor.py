"""
Module for processing and visualizing news articles data.
"""

from typing import Callable, Optional, Any
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from src.article import Article


class NewsProcessor:
    """
    Class to process and visualize news articles data.
    """

    def to_df(self, articles: list[Article],
              sort_by: Optional[Callable[[Article], Any]] = None,
              filter_func: Optional[Callable[[Article], bool]] = None
    ) -> pd.DataFrame:
        """
        Convert list of Article objects to a Pandas DataFrame.

        Args:
            articles (list[Article]): List of Article objects
            sort_by (Optional[Callable[[Article], Any]]): Optional function to sort rows by
            filter_func (Optional[Callable[[Article], bool]]): Optional function to filter rows 
                    (include rows where function returns True)

        Returns:
            pd.DataFrame: Pandas DataFrame with articles data
        """

        if filter_func is not None:
            articles = [a for a in articles if filter_func(a)]

        if sort_by is not None:
            articles = sorted(articles, key=sort_by)

        data = []
        for article in articles:
            data.append({
                "url": article.url,
                "source": article.source,
                "author": article.author,
                "title": article.title,
                "description": article.description,
                "published_at": article.published_at,
                "content": article.content
            })

        return pd.DataFrame(data)

    def plot_word_popularity(self, articles: list[Article], search_term: str) -> None:
        """
        Plot the frequency of a search term in article titles over time.

        Args:
            articles (list[Article]): List of Article objects
            search_term (str): The term to search for in titles
        """

        frequency_by_date: dict[datetime.date, int] = {}

        for article in articles:
            date = self._extract_date_from_published_at(article.published_at)

            if date is None:
                continue

            count = self._count_word_in_title(article.title, search_term)

            if date not in frequency_by_date:
                frequency_by_date[date] = 0

            frequency_by_date[date] += count

        sorted_dates = sorted(frequency_by_date.keys())
        counts = [frequency_by_date[d] for d in sorted_dates]

        date_strings: list[str] = [d.isoformat() for d in sorted_dates]

        plt.figure()
        plt.plot(date_strings, counts)

        plt.xlabel("Date")
        plt.ylabel("Frequency")
        plt.title(f"Frequency of '{search_term}' in Article Titles")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def _extract_date_from_published_at(
            self, published_at: Optional[str]) -> Optional[datetime.date]:
        """
        Helper method to extract date from publishedAt timestamp.

        Args:
            published_at (Optional[str]): ISO format timestamp string 
                    (e.g., '2023-10-01T12:34:56Z')

        Returns:
            Optional[datetime.date]: Date object representing the date in YYYY-MM-DD format, or 
            None if input is None
        """
        if not published_at:
            return None
        return datetime.datetime.fromisoformat(published_at.replace('Z', '+00:00')).date()

    def _count_word_in_title(self, title: str, search_term: str) -> int:
        """
        Helper method to count occurrences of search term in title.

        Args:
            title (str): Article title
            search_term (str): Term to search for

        Returns:
            int: Number of occurrences (case-insensitive)
        """
        if not title:
            return 0

        return title.lower().count(search_term.lower())
    
    def test_dataframe_values_match_article(self) -> None:
        """Ensure DataFrame values match Article attributes"""
        df = self.processor.to_df(self.articles)

        first_row = df.iloc[0]

        self.assertEqual(first_row["url"], self.articles[0].url)
        self.assertEqual(first_row["source"], self.articles[0].source)
        self.assertEqual(first_row["author"], self.articles[0].author)
        self.assertEqual(first_row["title"], self.articles[0].title)
        self.assertEqual(first_row["description"], self.articles[0].description)
        self.assertEqual(first_row["published_at"], self.articles[0].published_at)
        self.assertEqual(first_row["content"], self.articles[0].content)