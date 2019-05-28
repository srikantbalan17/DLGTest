"""Contains the routes, business logic contained within templates.py"""
from flask import Blueprint, jsonify, make_response

from .templates import num_sum

total_route = Blueprint('total', __name__)


# Single route with prefix defined in run.py
@total_route.route('/')
def total():
    response = num_sum(list(range(10000001)))
    return jsonify(total=response), 200
