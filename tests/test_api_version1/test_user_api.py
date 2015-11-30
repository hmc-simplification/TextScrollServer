from __future__ import unicode_literals, print_function, absolute_import, \
    division

import json

from nose.tools import with_setup

from server import app
from server.database import mongo

from ..util import expected_failure


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

@expected_failure
def test_get_invalid_user():
    client = app.test_client()
    response = client.get('/api/v1/users/1234567890123456789012345678901')
    print (response)
    assert response.status_code == 400
    client = app.test_client()
    response = client.get('/api/v1/users/12345 12345')
    assert response.status_code == 400
    response = client.get('/api/v1/users/12345%2012345')
    assert response.status_code == 400

@expected_failure
def test_get_user_not_logged_in():
    assert False

@expected_failure
def test_get_user_researcher_credentials():
    assert False

@with_setup(None, remove_user('3'))
def test_add_new_user():
    client = app.test_client()
    response = client.post('/api/v1/users/3')
    assert response.status_code == 201

@with_setup(insert_user('3', name='John Doe'), remove_user('3'))
def test_add_new_user_existing():
    client = app.test_client()
    response = client.post('/api/v1/users/3')
    assert response.status_code == 400

def test_add_invalid_user_too_long_username():
    client = app.test_client()
    response = client.post('/api/v1/users/1234567890123456789012345678901')
    assert response.status_code == 400

def test_add_invalid_user_username_contains_whitespace():
    client = app.test_client()
    response = client.post('/api/v1/users/12345 12345')
    assert response.status_code == 400
    response = client.post('/api/v1/users/12345%2012345')
    assert response.status_code == 400


# TODO: Implement request parsing.  As-is these don't have relevant
# request bodies, so they won't update, so they return 304 responses.

@expected_failure
@with_setup(insert_user('3', name='John Doe'), remove_user('3'))
def test_user_updated():
    client = app.test_client()
    response = client.put('/api/v1/users/3')
    assert response.status_code == 200

@with_setup(None, remove_user('3'))
def test_user_inserted_with_put():
    client = app.test_client()
    response = client.put('/api/v1/users/3')
    assert response.status_code == 201

@expected_failure
def test_put_invalid_user_too_long_username():
    client = app.test_client()
    response = client.put('/api/v1/users/1234567890123456789012345678901')
    assert response.status_code == 400

@expected_failure
def test_put_invalid_user_username_contains_whitespace():
    client = app.test_client()
    response = client.put('/api/v1/users/12345 12345')
    print(response)
    assert response.status_code == 400
    response = client.put('/api/v1/users/12345%2012345')
    assert response.status_code == 400
