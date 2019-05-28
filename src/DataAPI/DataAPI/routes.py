from templates import num_sum
from flask import Blueprint, jsonify, make_response

total_route = Blueprint('total', __name__)


@total_route.route('/')
def total():
    response = num_sum(list(range(10000001)))
    return jsonify(total=response), 200
