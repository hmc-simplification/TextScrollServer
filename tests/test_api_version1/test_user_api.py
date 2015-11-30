from __future__ import unicode_literals, print_function, absolute_import, \
    division

import json

from nose.tools import with_setup

from server import app
from server.database import mongo


old_name = None
def setup_package():
    global old_name
    app.config['MONGO_DBNAME'] = 'test'
    old_name = app.config.get('MONGO_DBNAME', None)

def teardown_package():
    if old_name is not None:
        app.config['MONGO_DBNAME'] = old_name


def insert_user(user_id, **kwargs):
    def _():
        with app.test_request_context():
            kwargs.update({'_id': user_id})
            mongo.db.users.insert(kwargs)
    return _

def remove_user(user_id):
    def _():
        with app.test_request_context():
            mongo.db.users.remove({'_id': user_id})
    return _


@with_setup(insert_user('3', name='John Doe'), remove_user('3'))
def test_get_existing_user():
    client = app.test_client()
    response = client.get('/api/v1/users/3')
    response_contents = json.loads(next(response.response).decode('utf-8'))
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response_contents['_id'] == '3'
    assert response_contents['name'] == 'John Doe'


def test_get_non_existing_user():
    client = app.test_client()
    response = client.get('/api/v1/users/42')
    assert response.status_code == 404
