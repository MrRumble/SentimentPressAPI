import datetime
from typing import List


class SearchResult:
    def __init__(
        self, 
        search_term=None, 
        mean_sentiment=None, 
        positive_article_count=None,
        negative_article_count=None, 
        total_article_count=None, 
        ratio_positive_vs_negative=None, 
        main_headline=None, 
        top_3_articles=None, 
        bottom_3_articles=None, 
        search_date=None, 
        search_time=None
    ):
        self.search_term = search_term
        self.mean_sentiment = mean_sentiment
        self.positive_article_count = positive_article_count
        self.negative_article_count = negative_article_count
        self.total_article_count = total_article_count
        self.ratio_positive_vs_negative = ratio_positive_vs_negative
        self.main_headline = main_headline
        self.top_3_articles = top_3_articles or []
        self.bottom_3_articles = bottom_3_articles or []
        self.search_date = search_date or datetime.datetime.now().strftime('%d-%m-%Y')
        self.search_time = search_time or datetime.datetime.now().strftime('%H:%M:%S')

    def __eq__(self, other):
        if not isinstance(other, SearchResult):
            return False
        return (
            self.search_term == other.search_term and
            self.mean_sentiment == other.mean_sentiment and
            self.positive_article_count == other.positive_article_count and
            self.negative_article_count == other.negative_article_count and
            self.total_article_count == other.total_article_count and
            self.ratio_positive_vs_negative == other.ratio_positive_vs_negative and
            self.main_headline == other.main_headline and
            self.top_3_articles == other.top_3_articles and
            self.bottom_3_articles == other.bottom_3_articles and
            self.search_date == other.search_date and
            self.search_time == other.search_time
        )

    def __repr__(self):
        return (
            f"SearchResult(search_term={self.search_term}, mean_sentiment={self.mean_sentiment}, "
            f"positive_article_count={self.positive_article_count}, negative_article_count={self.negative_article_count}, "
            f"total_article_count={self.total_article_count}, ratio_positive_vs_negative={self.ratio_positive_vs_negative}, "
            f"main_headline={self.main_headline}, top_3_articles={self.top_3_articles}, bottom_3_articles={self.bottom_3_articles}, "
            f"search_date={self.search_date}, search_time={self.search_time})"
        )

    def to_dict(self):
        return {
            "search_term": self.search_term,
            "mean_sentiment": self.mean_sentiment,
            "positive_article_count": self.positive_article_count,
            "negative_article_count": self.negative_article_count,
            "total_article_count": self.total_article_count,
            "ratio_positive_vs_negative": self.ratio_positive_vs_negative,
            "main_headline": self.main_headline,
            "top_3_articles": self.top_3_articles,
            "bottom_3_articles": self.bottom_3_articles,
            "search_date": self.search_date,
            "search_time": self.search_time,
        }
