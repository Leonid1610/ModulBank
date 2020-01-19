from help_functions.generate_random_numbers import *
from help_functions.generate_random_operation import *


class Bodies(object):
    def __init__(self, left_operand, operation, right_operand):
        self.body = {"left_operand": left_operand,
                     "operation": operation,
                     "right_operand": right_operand}


# input_data для тестов на деление
body_with_positive_numbers_for_division = Bodies(left_positive_operand, "/", right_positive_operand)\
    .__dict__['body']
body_with_negative_numbers_for_division = Bodies(left_negative_operand, "/", right_negative_operand)\
    .__dict__['body']
body_with_right_negative_operand_for_division = Bodies(left_positive_operand, "/", right_negative_operand)\
    .__dict__['body']
body_with_left_negative_operand_for_division = Bodies(left_negative_operand, "/", right_positive_operand)\
    .__dict__['body']

# input_data для тестов на вычитание
body_with_positive_numbers_for_difference = Bodies(left_positive_operand, "-", right_positive_operand)\
    .__dict__['body']
body_with_negative_numbers_for_difference = Bodies(left_negative_operand / 2, "-", right_negative_operand / 2)\
    .__dict__['body']
body_with_right_negative_operand_for_difference = Bodies(left_positive_operand / 2, "-", right_negative_operand / 2)\
    .__dict__['body']
body_with_left_negative_operand_for_difference = Bodies(left_negative_operand / 2, "-", right_positive_operand / 2)\
    .__dict__['body']

# input_data для тестов на сложение
body_with_positive_numbers_for_sum = Bodies(left_positive_operand, "+", right_positive_operand_for_sum)\
    .__dict__['body']
body_with_negative_numbers_for_sum = Bodies(left_negative_operand_for_sum, "+", right_negative_operand_for_sum)\
    .__dict__['body']
body_with_right_negative_operand_for_sum = Bodies(left_positive_operand_for_sum, "+", right_negative_operand_for_sum)\
    .__dict__['body']
body_with_left_negative_operand_for_sum = Bodies(left_negative_operand_for_sum, "+", right_positive_operand_for_sum)\
    .__dict__['body']

# input_data для тестов на умножение
body_with_positive_numbers_for_product = Bodies(left_positive_operand_for_product, "*",
                                                right_positive_operand_for_product).\
    __dict__['body']
body_with_negative_numbers_for_product = Bodies(left_negative_operand_for_product, "*",
                                                right_negative_operand_for_product).\
    __dict__['body']
body_with_right_negative_operand_for_product = Bodies(left_positive_operand_for_product, "*",
                                                      right_negative_operand_for_product)\
    .__dict__['body']
body_with_left_negative_operand_for_product = Bodies(left_negative_operand_for_product, "*",
                                                     right_positive_operand_for_product)\
    .__dict__['body']

# input_data для тестов вне диапазона integer
body_with_operand_which_beyond_the_integer_max_number = Bodies(max_int+1, "*", right_positive_operand_for_product).\
    __dict__['body']
body_with_operands_which_result_more_than_integer_max_number = Bodies(max_int, "+", 1).\
    __dict__['body']
body_with_operand_which_beyond_the_integer_min_number = Bodies(min_int-1, "*", right_positive_operand_for_product).\
    __dict__['body']
body_with_operands_which_result_less_than_integer_min_number = Bodies(min_int, "-", 1).\
    __dict__['body']

# input_data для тестов вне диапазона integer
body_with_for_division_by_zero = Bodies(left_positive_operand, "/", 0).__dict__['body']

# input_data для тестов вне диапазона integer
body_with_incorrect_operation = Bodies(left_positive_operand, random_symbol, right_positive_operand).__dict__['body']
