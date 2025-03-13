from flask import Blueprint, jsonify, request, current_app
from flask_cors import CORS
from app.repositories.search_result_repository import SearchResultRepository    
from app.repositories.search_metadata_repository import SearchMetadataRepository
from app.models.search_metadata_model import SearchMetadata
from app.utils.database import get_flask_database_connection

query_route = Blueprint('query_route', __name__)
CORS(query_route)

@query_route.route("/query", methods=["POST"])
def query():
    connection = get_flask_database_connection(current_app)
    search_result_repository = SearchResultRepository(connection)
    search_metadata_repository = SearchMetadataRepository(connection)
    data = request.get_json()
    query_text = data.get('query', '').lower().strip()

    if not query_text:
        return jsonify({"error": "Query text cannot be empty"}), 400

    meta_data = SearchMetadata(user_id=None, search_term=query_text)
    search_metadata_repository.create(meta_data)

    existing_result = search_result_repository.get_query_result_if_it_exists_today(query_text)
    if existing_result:
        response_data_front_end = {
            'query_info': {
                'total_articles': existing_result.total_article_count,
                'positive_count': existing_result.positive_article_count,
                'negative_count': existing_result.negative_article_count,
                'mean_sentiment': existing_result.mean_sentiment,
                'summary': existing_result.main_headline
            },
            'top3': existing_result.top_3_articles,
            'bottom3': existing_result.bottom_3_articles
        }
        print("Existing result found for query:", query_text)
        return jsonify(response_data_front_end), 200

    return jsonify({
        "error": f"No data available for '{query_text}' today. Please try again later."
    }), 404