#!/usr/bin/python3
'''Index of views'''
from api.v1.views import app_views
from flask import jsonify
from models import storage
import inflect
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    ''' Status of Response '''
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def count_objects():
    ''' Retrieves the count of objects by type '''
    classes = [Amenity, City, Place, Review, State, User]
    p = inflect.engine()
    num_objs = {}
    for c in classes:
        key = p.plural(c.__name__.lower())
        num_objs[key] = storage.count(c)
    return jsonify(num_objs)
