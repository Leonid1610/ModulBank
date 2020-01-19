from config import Endpoints
from requests import post
import json


def do_request_and_get_response(input_data):
    req = post(url=Endpoints.url_calculate, headers=Endpoints.headers, data=json.dumps(input_data))
    assert req.status_code == 200
    result = req.json()['result']
    return result

