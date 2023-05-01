#!/usr/bin/python3
"""Index views module."""
from flask import jsonify
from api.v1.views import app_views

# Create a route for status
@app_views.route('/status')
def status():
    """Return status OK."""
    return jsonify({"status": "OK"})
