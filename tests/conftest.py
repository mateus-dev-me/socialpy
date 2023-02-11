import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import IntegrityError

from socialpy.app import app
from socialpy.cli import create_user

os.environ[
    'socialpy_DB__uri'
] = 'postgresql://postgres:postgres@db:5432/socialpy_test'


@pytest.fixture(scope='function')
def api_client():
    return TestClient(app)


def create_api_client_authenticated(username):

    try:
        create_user(f'{username}@socialpy.com', username, username)
    except IntegrityError:
        pass

    client = TestClient(app)
    token = client.post(
        '/token',
        data={'username': username, 'password': username},
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    ).json()['access_token']
    client.headers['Authorization'] = f'Bearer {token}'
    return client


@pytest.fixture(scope='function')
def api_client_user1():
    return create_api_client_authenticated('user1')


@pytest.fixture(scope='function')
def api_client_user2():
    return create_api_client_authenticated('user2')
