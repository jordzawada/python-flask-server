import pytest

from flask import json
import web

@pytest.fixture
def client():
    web.app.config['TESTING'] = True
    client = web.app.test_client()

    yield client

def test_root(client):
    rv = client.get('/')
    assert(rv.status_code == 200)
    assert(b'hello' in rv.data)