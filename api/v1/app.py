#!/usr/bin/python3
"""Create and configure the Flask application."""
from flask import Flask
from api.v1.views import app_views
from models import storage
from flask import jsonify


# Create Flask application instance
app = Flask(__name__)

# Register blueprint
app.register_blueprint(app_views)

# Define teardown function to close storage
@app.teardown_appcontext
def teardown(exception):
    """Closes the storage connection."""
    storage.close()
    
# Your API routes and logic here...

# Error handling for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404


# Run Flask application
if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
