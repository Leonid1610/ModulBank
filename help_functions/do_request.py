from config import Endpoints
from requests import post
import json
from http import HTTPStatus


def do_request_and_get_response_for_positive_tests(input_data):
    req = post(url=Endpoints.url_calculate, headers=Endpoints.headers, data=json.dumps(input_data))
    assert req.status_code == HTTPStatus.OK.value
    result = req.json()['result']
    return result


def do_request_and_get_response_for_negative_tests(input_data, expected_result):
    req = post(url=Endpoints.url_calculate, headers=Endpoints.headers, data=json.dumps(input_data))
    assert req.status_code == expected_result, f"""Некорректный ответ от сервера: ожидается {expected_result}, получено 
                                                   {req.status_code}"""
    result = req.json()['error']
    return result
