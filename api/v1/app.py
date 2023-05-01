#!/usr/bin/python3
"""Create and configure the Flask application."""
from flask import Flask
from api.v1.views import app_views
from models import storage


# Create Flask application instance
app = Flask(__name__)

# Register blueprint
app.register_blueprint(app_views)

# Define teardown function to close storage
@app.teardown_appcontext
def teardown(exception):
    """Closes the storage connection."""
    storage.close()

# Run Flask application
if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
