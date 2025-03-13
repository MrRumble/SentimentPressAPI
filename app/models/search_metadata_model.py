import datetime


class SearchMetadata:
    def __init__(
        self,
        search_metadata_id=None,  # Unique identifier for each search log entry
        user_id=None,  # Tracks which user performed the search
        search_term=None,  # The term being searched
        searched_at=None  # Timestamp of the search
    ):
        self.search_metadata_id = search_metadata_id
        self.user_id = user_id
        self.search_term = search_term
        self.searched_at = searched_at or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Default to current timestamp

    def __eq__(self, other):
        if not isinstance(other, SearchMetadata):
            return False
        return (
            self.search_metadata_id == other.search_metadata_id and
            self.user_id == other.user_id and
            self.search_term == other.search_term and
            self.searched_at == other.searched_at
        )

    def __repr__(self):
        return (
            f"SearchMetadata(search_metadata_id={self.search_metadata_id}, user_id={self.user_id}, "
            f"search_term={self.search_term}, searched_at={self.searched_at})"
        )

    def to_dict(self):
        return {
            "search_metadata_id": self.search_metadata_id,
            "user_id": self.user_id,
            "search_term": self.search_term,
            "searched_at": self.searched_at
        }
