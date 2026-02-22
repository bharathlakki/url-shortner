from flask import Flask, render_template
from .routes import url_shortener_routes
from .config import Config
from pymongo import MongoClient
import os

# Add connection parameters with timeout
mongo_uri = Config.MONGO_URI
try:
    client = MongoClient(
        mongo_uri,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=10000,
        retryWrites=True
    )
    # Test connection without blocking
    client.admin.command('ping')
    print("✓ MongoDB Connected Successfully")
except Exception as e:
    print(f"⚠ MongoDB Connection will be retried on first request: {e}")
    client = MongoClient(mongo_uri)

db = client[Config.DB_NAME]

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )
    app.config.from_object(Config)
    app.db = db

    # Register Blueprint
    app.register_blueprint(url_shortener_routes)

    # Custom 404 Page
    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app
