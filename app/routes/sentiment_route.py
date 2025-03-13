from flask import jsonify, request, current_app
from app.repositories.search_result_repository import SearchResultRepository
from app.utils.database import get_flask_database_connection
from flask import Blueprint
from flask_cors import CORS
from collections import defaultdict
from decimal import Decimal
import random

sentiment_route = Blueprint('sentiment_route', __name__)
CORS(sentiment_route)


@sentiment_route.route('/api/get_sentiment', methods=['GET'])
def get_sentiment():
    search_term = request.args.get('search_term').lower()
    if not search_term:
        return jsonify({"error": "search_term is required"}), 400

    connection = get_flask_database_connection(current_app)
    search_result_repository = SearchResultRepository(connection)

    try:
        results = search_result_repository.get_sentiment_over_time(search_term)

        organized_data = defaultdict(list)

        for row in results:
            mean_sentiment = float(row['mean_sentiment']) 
            date = row['date'].strftime('%Y-%m-%d')
            summary = row['main_headline']
            organized_data[date].append({
                'sentiment': mean_sentiment, 
                'summary': summary
            })
        
        final_data = {
            "datasets": [
                {
                    "label": search_term,
                    "data": [
                        {"x": date, "y": organized_data[date][0]['sentiment'], "summary": organized_data[date][0]['summary']}
                        for date in sorted(organized_data.keys())
                    ],  
                    "fill": False  
                }
            ]
        }

        return jsonify(final_data), 200

    except Exception as e:
        print(f"Error fetching or processing data: {e}")
        return jsonify({"error": "An error occurred while fetching sentiment data."}), 500
