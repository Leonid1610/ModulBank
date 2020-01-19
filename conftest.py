import pytest
from requests import get
from config import Endpoints
from help_functions.create_bodies import *
from http import HTTPStatus


@pytest.yield_fixture()
def setup():
    """
        Фикстура, которая перед началом каждого из тестов проверяет наличие корректного отклика от сервера путем
        отправки GET
    """
    req = get(url=Endpoints.url_to_check_response_from_server)
    assert req.status_code == HTTPStatus.OK.value, f"""\nКод ответа:{req}. 
    Если код ответа = 404 - проверьте корректность запроса. 
    Если код ответа = 500 - сервер не доступен"""


@pytest.fixture(params=[(body_with_positive_numbers_for_division, int(left_positive_operand /
                                                                      right_positive_operand)),
                        (body_with_negative_numbers_for_division, int(left_negative_operand /
                                                                      right_negative_operand)),
                        (body_with_right_negative_operand_for_division, int(left_positive_operand /
                                                                            right_negative_operand)),
                        (body_with_left_negative_operand_for_division, int(right_positive_operand /
                                                                           left_negative_operand))],
                ids=["all_positive_operands", "all_negative_operands", "right_negative_operand",
                     "left_negative_operand"])
def param_for_division_tests(request):
    """
        Фикстура, содержащая параметры для тестирования деления
    """
    return request.param


@pytest.fixture(params=[(body_with_positive_numbers_for_difference, int(left_positive_operand -
                                                                        right_positive_operand)),
                        (body_with_negative_numbers_for_difference, int((left_negative_operand / 2) -
                                                                        (right_negative_operand / 2))),
                        (body_with_right_negative_operand_for_difference, int((left_positive_operand / 2) -
                                                                              (right_negative_operand / 2))),
                        (body_with_left_negative_operand_for_difference, int((left_negative_operand / 2) -
                                                                             (right_positive_operand / 2)))],
                ids=["all_positive_operands", "all_negative_operands", "right_negative_operand",
                     "left_negative_operand"])
def param_for_difference_tests(request):
    """
        Фикстура, содержащая параметры для тестирования вычитания
    """
    return request.param


@pytest.fixture(params=[(body_with_positive_numbers_for_sum, int(left_positive_operand_for_sum +
                                                                 right_positive_operand_for_sum)),
                        (body_with_negative_numbers_for_sum, int(left_negative_operand_for_sum
                                                                 - right_negative_operand_for_sum)),
                        (body_with_right_negative_operand_for_sum, int(left_positive_operand_for_sum +
                                                                       right_negative_operand_for_sum)),
                        (body_with_left_negative_operand_for_sum, int(left_negative_operand_for_sum +
                                                                      right_positive_operand_for_sum))],
                ids=["all_positive_operands", "all_negative_operands", "right_negative_operand",
                     "left_negative_operand"])
def param_for_sum_tests(request):
    """
        Фикстура, содержащая параметры для тестирования сложения
    """
    return request.param


@pytest.fixture(params=[(body_with_positive_numbers_for_product, int(left_positive_operand_for_product *
                                                                     right_positive_operand_for_product)),
                        (body_with_negative_numbers_for_product, int(left_negative_operand_for_product *
                                                                     right_negative_operand_for_product)),
                        (body_with_right_negative_operand_for_product, int(left_positive_operand_for_product *
                                                                           right_negative_operand_for_product)),
                        (body_with_left_negative_operand_for_product, int(left_negative_operand_for_product *
                                                                          right_positive_operand_for_product))],
                ids=["all_positive_operands", "all_negative_operands", "right_negative_operand",
                     "left_negative_operand"])
def param_for_products_tests(request):
    """
        Фикстура, содержащая параметры для тестирования умножения
    """
    return request.param


@pytest.fixture(params=[(body_with_operand_which_beyond_the_integer_max_number, HTTPStatus.BAD_REQUEST.value),
                        (body_with_operands_which_result_more_than_integer_max_number, HTTPStatus.BAD_REQUEST.value),
                        (body_with_operand_which_beyond_the_integer_min_number, HTTPStatus.BAD_REQUEST.value),
                        (body_with_operands_which_result_less_than_integer_min_number, HTTPStatus.BAD_REQUEST.value)],
                ids=["one_operand_more_than_max_int", "result_more_than_max_int", "one_operand_less_than_min_int",
                     "result_less_than_min_int"])
def param_for_beyond_the_integer_range_tests(request):
    """
        Фикстура, содержащая параметры для тестирования случаев, когда операнды или результат выходят за границы integer
    """
    return request.param
