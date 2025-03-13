from app.models.search_result_model import SearchResult
import json
from datetime import date, timedelta

class SearchResultRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, search_result):
        query = """
            INSERT INTO search_results (search_term, mean_sentiment, positive_article_count, 
                                       negative_article_count, total_article_count, 
                                       ratio_positive_vs_negative, main_headline, 
                                       top_3_articles, bottom_3_articles, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING search_result_id
        """
        params = (
            search_result.search_term,
            search_result.mean_sentiment,
            search_result.positive_article_count,
            search_result.negative_article_count,
            search_result.total_article_count,
            search_result.ratio_positive_vs_negative,
            search_result.main_headline,
            json.dumps(search_result.top_3_articles),
            json.dumps(search_result.bottom_3_articles),
            search_result.created_at
        )
        result = self._connection.execute(query, params)
        search_result.search_result_id = result[0]['search_result_id']
        return search_result

    def find(self, search_result_id):
        query = 'SELECT * FROM search_results WHERE search_result_id = %s'
        rows = self._connection.execute(query, [search_result_id])
        if not rows:
            raise ValueError("SearchResult not found")
        row = rows[0]
        return SearchResult(
            search_result_id=row['search_result_id'],
            search_term=row['search_term'],
            mean_sentiment=row['mean_sentiment'],
            positive_article_count=row['positive_article_count'],
            negative_article_count=row['negative_article_count'],
            total_article_count=row['total_article_count'],
            ratio_positive_vs_negative=row['ratio_positive_vs_negative'],
            main_headline=row['main_headline'],
            top_3_articles=row['top_3_articles'],
            bottom_3_articles=row['bottom_3_articles'],
            created_at=row['created_at']
        )

    def get_query_result_if_it_exists_today(self, query):
        today = date.today().strftime('%Y-%m-%d')

        query_str = """
                SELECT *
                FROM search_results
                WHERE search_term = %s AND created_at::date = %s
            """
            
        rows = self._connection.execute(query_str, [query.lower().strip(), today])
        if rows:
            row = rows[0]
            return SearchResult(
                search_result_id=row['search_result_id'],
                search_term=row['search_term'],
                mean_sentiment=row['mean_sentiment'],
                positive_article_count=row['positive_article_count'],
                negative_article_count=row['negative_article_count'],
                total_article_count=row['total_article_count'],
                ratio_positive_vs_negative=row['ratio_positive_vs_negative'],
                main_headline=row['main_headline'],
                top_3_articles=row['top_3_articles'],
                bottom_3_articles=row['bottom_3_articles'],
                created_at=row['created_at']
            )
        else:
            return None
        
    def get_sentiment_over_time(self, search_term):
        """
        Retrieves the sentiment data for a single search term over the last 30 days,
        with distinct entries per search term per day.
        """

        query = """
            SELECT DISTINCT ON (created_at::date)
                search_term, 
                mean_sentiment, 
                created_at::date AS date, 
                main_headline
            FROM search_results
            WHERE search_term = %s
            AND created_at >= CURRENT_DATE - INTERVAL '30 days'
            ORDER BY created_at::date, created_at ASC;
        """
        
        rows = self._connection.execute(query, [search_term])

        if not rows:
            return []


        results = []
        for row in rows:

            adjusted_date = row['date'] - timedelta(days=1)
        
            results.append({
                "search_term": row['search_term'],
                "mean_sentiment": row['mean_sentiment'],
                "date": adjusted_date, 
                "main_headline": row['main_headline'],
            })

        return results

    def get_queries_and_headlines(self):
        """
        Fetches search terms and their main headlines for the current day.
        If no articles exist for a category, they are omitted.
        """
        today = date.today().strftime('%Y-%m-%d')

        news_categories = [
            "world", "politics", "business", "science", "health", "sports",
            "entertainment", "education", "environment", "uk", 
            "finance", "music", "technology", "stock market", "cryptocurrency", 
            "weather", "crime", "starmer", "war", "trump", "ai", 
            "rugby", "gaza", "israel", "russia", "ukraine"
        ]


        query_str = """
            SELECT search_term, main_headline
            FROM search_results
            WHERE search_term = ANY(%s) AND created_at::date = %s
        """
        
        rows = self._connection.execute(query_str, [news_categories, today])

        if not rows:
            return []

        results = [{"search_term": row["search_term"].capitalize(), "main_headline": row["main_headline"]} for row in rows]

        return results
    
    def get_highest_sentiment_today(self):
        """
        Retrieves the search result with the highest sentiment from today.
        """
        today = date.today().strftime('%Y-%m-%d')

        query = """
            SELECT *
            FROM search_results
            WHERE created_at::date = %s
            ORDER BY mean_sentiment DESC
            LIMIT 1;
        """

        rows = self._connection.execute(query, [today])

        if not rows:
            return None 

        row = rows[0]
        return SearchResult(
            search_result_id=row['search_result_id'],
            search_term=row['search_term'],
            mean_sentiment=row['mean_sentiment'],
            positive_article_count=row['positive_article_count'],
            negative_article_count=row['negative_article_count'],
            total_article_count=row['total_article_count'],
            ratio_positive_vs_negative=row['ratio_positive_vs_negative'],
            main_headline=row['main_headline'],
            top_3_articles=row['top_3_articles'],
            bottom_3_articles=row['bottom_3_articles'],
            created_at=row['created_at']
        )

    def get_lowest_sentiment_today(self):
        """
        Retrieves the search result with the lowest sentiment from today.
        """
        today = date.today().strftime('%Y-%m-%d')

        query = """
            SELECT *
            FROM search_results
            WHERE created_at::date = %s
            ORDER BY mean_sentiment ASC
            LIMIT 1;
        """

        rows = self._connection.execute(query, [today])

        if not rows:
            return None

        row = rows[0]
        return SearchResult(
            search_result_id=row['search_result_id'],
            search_term=row['search_term'],
            mean_sentiment=row['mean_sentiment'],
            positive_article_count=row['positive_article_count'],
            negative_article_count=row['negative_article_count'],
            total_article_count=row['total_article_count'],
            ratio_positive_vs_negative=row['ratio_positive_vs_negative'],
            main_headline=row['main_headline'],
            top_3_articles=row['top_3_articles'],
            bottom_3_articles=row['bottom_3_articles'],
            created_at=row['created_at']
        )
