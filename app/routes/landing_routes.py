from flask import Blueprint, jsonify, current_app
from flask_cors import CORS
from app.utils.database import get_flask_database_connection
from app.repositories.search_result_repository import SearchResultRepository
from app.repositories.search_metadata_repository import SearchMetadataRepository

landing_route = Blueprint('landing_routes', __name__)
CORS(landing_route)

@landing_route.route('/api/get-headlines', methods=['GET'])
def get_random_headlines():
    """
    API endpoint to fetch random search terms and their main headlines for the current day.
    """
    connection = get_flask_database_connection(current_app)
    repository = SearchResultRepository(connection)

    try:
        headlines = repository.get_queries_and_headlines()
        return jsonify({"headlines": headlines}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@landing_route.route('/api/get-todays-top-search', methods=['GET'])
def get_todays_top_search_term():
    connection = get_flask_database_connection(current_app)
    repository = SearchMetadataRepository(connection)

    try:
        top_term, count = repository.get_todays_top_search_term()
        if top_term:
            return jsonify({"term": top_term, "count": count}), 200
        else:
            return jsonify({"message": "No searches today"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@landing_route.route('/api/get-highest-sentiment-today', methods=['GET'])
def get_highest_sentiment_today():
    connection = get_flask_database_connection(current_app)
    repository = SearchResultRepository(connection)

    try:
        highest_sentiment = repository.get_highest_sentiment_today()
        if highest_sentiment:
            return jsonify({
                "term": highest_sentiment.search_term,
                "sentiment_score": highest_sentiment.mean_sentiment,
                "summary": highest_sentiment.main_headline
            }), 200
        else:
            return jsonify({"message": "No results found for today"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@landing_route.route('/api/get-lowest-sentiment-today', methods=['GET'])
def get_lowest_sentiment_today():
    connection = get_flask_database_connection(current_app)
    repository = SearchResultRepository(connection)

    try:
        lowest_sentiment = repository.get_lowest_sentiment_today()
        if lowest_sentiment:
            return jsonify({
                "term": lowest_sentiment.search_term,
                "sentiment_score": lowest_sentiment.mean_sentiment,
                "summary": lowest_sentiment.main_headline
            }), 200
        else:
            return jsonify({"message": "No results found for today"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
