#!/usr/bin/python3
"""Initialize the views module."""
from flask import Blueprint

# Create a Blueprint object
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views module to register the blueprints
from api.v1.views.index import *
