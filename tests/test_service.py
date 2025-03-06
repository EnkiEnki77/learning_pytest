import pytest
import requests

import Source.service as service
import unittest.mock as mock

from Source import shapes


# @mock.patch("Source.service.get_user_from_db")
# def test_get_user_from_db(mock_get_user_from_db):
#     mock_get_user_from_db.return_value = "Mocked Bob"
#     user_name = service.get_user_from_db(1)
#     assert user_name == "Mocked Bob"

# When youre testing a function that fetches from an API or db we want to test the functionality of the function
# given specific responses from that API or db, but since the API or db is an external dependency we have less
# control of what the response will actually be. So we want to mock these dependencies so that for the tests
# we do have control of the response. We want to test that our function handles specific responses correctly.
@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = service.get_users_from_api()
    assert data == {"id": 1, "name": "John Doe"}

# You should use mocks when the functionality youre testing relies on external dependencies that cannot guarantee
# the same return value every time. The mock gives you control over the return value. For example, with an API
# You cannot guarantee if you give it certain inputs youll get the same output each time, because an API can crash,
# have down time, take some time to give a response, or maybe the authors even just altered it
@mock.patch("requests.get")
def test_get_user_400_status_code(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users_from_api()