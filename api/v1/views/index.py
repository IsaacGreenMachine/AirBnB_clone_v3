#!/usr/bin/python3
'''looks like views index'''
from api.v1.views import app_views
import flask


@app_views.route('/status', strict_slashes=False)
def okayThen():
    '''return json obj for status'''
    return flask.jsonify({'status': 'OK'})
