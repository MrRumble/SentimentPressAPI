import datetime


class SearchResult:
    def __init__(
        self,
        search_result_id=None,  # Add search_result_id as a parameter
        search_term=None,
        mean_sentiment=None,
        positive_article_count=None,
        negative_article_count=None,
        total_article_count=None,
        ratio_positive_vs_negative=None,
        main_headline=None,
        top_3_articles=None,
        bottom_3_articles=None,
        created_at=None  # Single timestamp parameter
    ):
        self.search_result_id = search_result_id  # Set the search_result_id
        self.search_term = search_term
        self.mean_sentiment = mean_sentiment
        self.positive_article_count = positive_article_count
        self.negative_article_count = negative_article_count
        self.total_article_count = total_article_count
        self.ratio_positive_vs_negative = ratio_positive_vs_negative
        self.main_headline = main_headline
        self.top_3_articles = top_3_articles or []
        self.bottom_3_articles = bottom_3_articles or []
        self.created_at = created_at or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Default to current timestamp

    def __eq__(self, other):
        if not isinstance(other, SearchResult):
            return False
        return (
            self.search_result_id == other.search_result_id and
            self.search_term == other.search_term and
            self.mean_sentiment == other.mean_sentiment and
            self.positive_article_count == other.positive_article_count and
            self.negative_article_count == other.negative_article_count and
            self.total_article_count == other.total_article_count and
            self.ratio_positive_vs_negative == other.ratio_positive_vs_negative and
            self.main_headline == other.main_headline and
            self.top_3_articles == other.top_3_articles and
            self.bottom_3_articles == other.bottom_3_articles and
            self.created_at == other.created_at  # Compare the single timestamp
        )

    def __repr__(self):
        return (
            f"SearchResult(search_result_id={self.search_result_id}, search_term={self.search_term}, mean_sentiment={self.mean_sentiment}, "
            f"positive_article_count={self.positive_article_count}, negative_article_count={self.negative_article_count}, "
            f"total_article_count={self.total_article_count}, ratio_positive_vs_negative={self.ratio_positive_vs_negative}, "
            f"main_headline={self.main_headline}, top_3_articles={self.top_3_articles}, bottom_3_articles={self.bottom_3_articles}, "
            f"created_at={self.created_at})"
        )

    def to_dict(self):
        return {
            "search_result_id": self.search_result_id,  # Include search_result_id here as well
            "search_term": self.search_term,
            "mean_sentiment": self.mean_sentiment,
            "positive_article_count": self.positive_article_count,
            "negative_article_count": self.negative_article_count,
            "total_article_count": self.total_article_count,
            "ratio_positive_vs_negative": self.ratio_positive_vs_negative,
            "main_headline": self.main_headline,
            "top_3_articles": self.top_3_articles,
            "bottom_3_articles": self.bottom_3_articles,
            "created_at": self.created_at  # Include the single timestamp field
        }
