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

CORS(app, resources={
    r"/api/*": {"origins": "https://d1ya212cbyxvmq.cloudfront.net"},
    r"/*": {"origins": "https://d1ya212cbyxvmq.cloudfront.net"}
})


app.register_blueprint(insert_data_route)
app.register_blueprint(query_route)
app.register_blueprint(sentiment_route)
app.register_blueprint(landing_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5002)))
