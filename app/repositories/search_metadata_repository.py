import json
from app.models.search_metadata_model import SearchMetadata

class SearchMetadataRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, search_metadata):
        query = """
            INSERT INTO search_metadata (user_id, search_term, searched_at)
            VALUES (%s, %s, %s)
            RETURNING search_metadata_id
        """
        params = (
            search_metadata.user_id,
            search_metadata.search_term,
            search_metadata.searched_at
        )
        result = self._connection.execute(query, params)
        search_metadata.search_metadata_id = result[0]['search_metadata_id']
        return search_metadata

    def get_todays_top_search_term(self):
        query = """
        SELECT search_term, COUNT(*) as search_count
        FROM search_metadata
        WHERE DATE(searched_at) = CURRENT_DATE
        GROUP BY search_term
        ORDER BY search_count DESC
        LIMIT 1;
        """
        result = self._connection.execute(query)
        
        if result:
            top_search_term = result[0]
            return top_search_term['search_term'], top_search_term['search_count']
        else:
            return None, 0

