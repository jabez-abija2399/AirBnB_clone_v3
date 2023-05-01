#!/usr/bin/python3
"""Index views module."""
from api.v1.views import app_views
from flask import jsonify
from models import storage


# Create a route for status
@app_views.route('/status')
def status():
    """Return status OK."""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    Retrieves the number of each objects by type.

    Returns:
        JSON representation of the statistics.
    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
