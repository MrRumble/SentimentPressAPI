from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.routes.query_route import query_route
from app.routes.sentiment_route import sentiment_route
from app.routes.landing_routes import landing_route
from app.routes.insert_data import insert_data_route
import os

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

app.register_blueprint(insert_data_route)
app.register_blueprint(query_route)
app.register_blueprint(sentiment_route)
app.register_blueprint(landing_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5002)))