import random
from math import fabs


class NumberGenerator(object):
    def __init__(self, left_border, right_border):
        self.right_border = right_border
        self.left_border = left_border

    def generate_random_number(self):
        random_number = random.randint(self.left_border, self.right_border)
        return random_number


max_int = 2147483647
min_int = -2147483648


# операнды для деления и вычитания
left_positive_operand = int(NumberGenerator(1, max_int).generate_random_number())
right_positive_operand = int(NumberGenerator(1, max_int).generate_random_number())
left_negative_operand = int(NumberGenerator(min_int, -1).generate_random_number())
right_negative_operand = int(NumberGenerator(min_int, -1).generate_random_number())

# операнды для умножения
left_positive_operand_for_product = int(NumberGenerator(1, 500).generate_random_number())
right_positive_operand_for_product = int(NumberGenerator(1, 500).generate_random_number())
left_negative_operand_for_product = int(NumberGenerator(-500, -1).generate_random_number())
right_negative_operand_for_product = int(NumberGenerator(-500, -1).generate_random_number())

# операнды для сложения
left_positive_operand_for_sum = int(NumberGenerator(0, max_int).generate_random_number())
right_positive_operand_for_sum = int(max_int - left_positive_operand_for_sum)
left_negative_operand_for_sum = int(NumberGenerator(min_int, 0).generate_random_number())
right_negative_operand_for_sum = int(min_int + fabs(left_negative_operand_for_sum))
