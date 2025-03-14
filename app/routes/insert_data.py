from flask import request, jsonify, Blueprint, current_app
from app.repositories.search_result_repository import SearchResultRepository
from flask_cors import CORS
from app.utils.database import get_flask_database_connection
import json

insert_data_route = Blueprint('insert_data', __name__)  # Name the blueprint properly
CORS(insert_data_route)

@insert_data_route.route('/insert_data', methods=['POST'])
def insert_data():
    connection = get_flask_database_connection(current_app)  # Correctly use the connection
    data = request.json  # Get the JSON data from the request

    # Extract the fields from the incoming request data
    search_term = data.get('search_term')
    mean_sentiment = data.get('mean_sentiment')
    positive_article_count = data.get('positive_article_count')
    negative_article_count = data.get('negative_article_count')
    total_article_count = data.get('total_article_count')
    ratio_positive_vs_negative = data.get('ratio_positive_vs_negative')
    main_headline = data.get('main_headline')
    top_3_articles = data.get('top_3_articles')
    bottom_3_articles = data.get('bottom_3_articles')
    created_at = data.get('created_at')

    # Make sure `top_3_articles` and `bottom_3_articles` are properly serialized to JSON strings
    top_3_articles = json.dumps(top_3_articles)
    bottom_3_articles = json.dumps(bottom_3_articles)

    # Prepare the search result data
    search_result = {
        "search_term": search_term,
        "mean_sentiment": mean_sentiment,
        "positive_article_count": positive_article_count,
        "negative_article_count": negative_article_count,
        "total_article_count": total_article_count,
        "ratio_positive_vs_negative": ratio_positive_vs_negative,
        "main_headline": main_headline,
        "top_3_articles": top_3_articles,
        "bottom_3_articles": bottom_3_articles,
        "created_at": created_at
    }

    # Insert into the database (call the repository's create method)
    try:
        search_result_repository = SearchResultRepository(connection)
        result = search_result_repository.create(search_result)  # Pass the data to the create method

        # Return a success response
        return jsonify({"message": "Data inserted successfully", "search_result_id": result.search_result_id}), 200

    except Exception as e:
        # Handle any errors that occur during the insertion
        return jsonify({"message": f"Error inserting data: {str(e)}"}), 500
