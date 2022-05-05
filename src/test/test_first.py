"""
Unit tests for first end-point
"""

import json
from .fixture import client


def test_first_status_code(client):
    """
    Test the api HTTP status code
    :param client: An app test client from the fixture
    :return: None
    """
    response = client.get('/api/v1.0/first')
    assert response.status_code == 200
