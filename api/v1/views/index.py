#!/usr/bin/python3
"""
Module for index route
"""
from flask import jsonify
from models import storage
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """Returns status in JSON format"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def stats():
    """Returns stats in JSON format"""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    retval = {key: storage.count(val) for key, val in classes.items()}
    return jsonify(retval)
