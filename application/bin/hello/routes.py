from flask import Blueprint, make_response, jsonify

hello_blueprint = Blueprint('home', __name__)


@hello_blueprint.route('/hello_world', methods=('GET', 'POST'))
def hello_world():

    response = make_response(
        jsonify(
            {'message': 'Hello World'}
        ), 200
    )

    return response
