from help_functions.do_request import do_request_and_get_response_for_negative_tests
from help_functions.create_bodies import body_with_for_division_by_zero
from help_functions.create_bodies import body_with_incorrect_operation
from http import HTTPStatus
import allure


@allure.suite("Тестирование калькулятора")
@allure.feature("Проверка валидации")
@allure.title("Тест на проверку валидации при передаче операндов вне диапозона integer")
def test_beyond_the_integer_range(setup, param_for_beyond_the_integer_range_tests):
    (input_data, expected_data) = param_for_beyond_the_integer_range_tests
    with allure.step(f"отправляем запрос с входными данными {input_data} и получаем ответ от сервера"):
        result = do_request_and_get_response_for_negative_tests(input_data, expected_data)
    expected_result = expected_data
    with allure.step("Проверяем, что полученный результат = ожидаемому"):
        assert result == expected_result, f"Ожидается {expected_result}, получено {result}"


@allure.suite("Тестирование калькулятора")
@allure.feature("Проверка валидации")
@allure.title("Тест на проверку валидации при делении на ноль")
def test_division_by_zero(setup):
    input_data = body_with_for_division_by_zero
    expected_data = HTTPStatus.BAD_REQUEST.value
    with allure.step(f"отправляем запрос с входными данными {input_data} и получаем ответ от сервера"):
        result = do_request_and_get_response_for_negative_tests(input_data, expected_data)
    with allure.step("Проверяем, что полученный результат = ожидаемому"):
        assert result == expected_data, f"Ожидается {expected_data}, получено {result}"


@allure.suite("Тестирование калькулятора")
@allure.feature("Проверка валидации")
@allure.title("Тест на проверку валидации при передачи неподдерживаемой операции")
def test_incorrect_operation(setup):
    input_data = body_with_incorrect_operation
    expected_data = "\"operation\" value must be one of \"['-', '+', '/', '*']\""
    with allure.step(f"отправляем запрос с входными данными {input_data} и получаем ответ от сервера"):
        result = do_request_and_get_response_for_negative_tests(input_data, HTTPStatus.BAD_REQUEST.value)
    with allure.step("Проверяем, что полученный результат = ожидаемому"):
        assert result == expected_data, f"Ожидается {expected_data}, получено {result}"

