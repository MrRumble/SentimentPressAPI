from flask import request, jsonify, Blueprint, current_app
from app.repositories.search_result_repository import SearchResultRepository
from flask_cors import CORS
from app.utils.database import get_flask_database_connection
import json
from app.models.search_result_model import SearchResult  

insert_data_route = Blueprint('insert_data', __name__)  # Name the blueprint properly
CORS(insert_data_route)

@insert_data_route.route('/insert_data', methods=['POST'])
def insert_data():
    connection = get_flask_database_connection(current_app)
    data = request.json  # Get the JSON data from the request

    # Create an instance of SearchResult with the incoming data
    search_result = SearchResult(
        search_term=data.get('search_term'),
        mean_sentiment=data.get('mean_sentiment'),
        positive_article_count=data.get('positive_article_count'),
        negative_article_count=data.get('negative_article_count'),
        total_article_count=data.get('total_article_count'),
        ratio_positive_vs_negative=data.get('ratio_positive_vs_negative'),
        main_headline=data.get('main_headline'),
        top_3_articles=json.dumps(data.get('top_3_articles')),
        bottom_3_articles=json.dumps(data.get('bottom_3_articles')),
        created_at=data.get('created_at')
    )

    try:
        search_result_repository = SearchResultRepository(connection)
        result = search_result_repository.create(search_result)

        return jsonify({"message": "Data inserted successfully", "search_result_id": result.search_result_id}), 200

    except Exception as e:
        return jsonify({"message": f"Error inserting data: {str(e)}"}), 500
