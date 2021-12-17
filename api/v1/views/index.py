#!/usr/bin/python3
'''looks like views index'''
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import flask


@app_views.route('/status', strict_slashes=False)
def okayThen():
    '''return json obj for status'''
    return flask.jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def stats():
    '''print out stats using count'''
    return flask.jsonify(
        {'amenities': storage.count(Amenity),
         'cities': storage.count(City),
         'places': storage.count(Place),
         'reviews': storage.count(Review),
         'states': storage.count(State),
         'users': storage.count(User)}
    )
