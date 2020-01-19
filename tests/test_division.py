from help_functions.do_request import do_request_and_get_response_for_positive_tests
import allure


@allure.suite("Тестирование калькулятора")
@allure.feature("Тестирование функции калькулятора - деление")
@allure.title("Тест на проверку деления с числами внутри диапазона integer")
def test_division_for_integers_within_borders(setup, param_for_division_tests):
    (input_data, expected_data) = param_for_division_tests
    with allure.step(f"отправляем запрос с входными данными {input_data} и получаем результат расчёта"):
        result = do_request_and_get_response_for_positive_tests(input_data)
    expected_result = expected_data
    with allure.step("Проверяем, что полученный результат = ожидаемому"):
        assert result == expected_result, f"Ожидается {expected_result}, получено {result}"
