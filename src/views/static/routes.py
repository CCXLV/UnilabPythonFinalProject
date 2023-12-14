from flask import Blueprint, send_from_directory


static_blueprint = Blueprint('static', __name__)

@static_blueprint.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)