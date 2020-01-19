import random


class GenerateRandomNumbers(object):
    def __init__(self, left_border, right_border):
        self.right_border = right_border
        self.left_border = left_border

    def generate_random_number(self):
        random_number = random.randint(self.left_border, self.right_border)
        return random_number

    def generate_random_positive_number_for_sum(self):
        # передаем от 1 до макс инт
        """
        :return:
        """
        number = random.randint(self.left_border, self.right_border)
        result = random.randint(1, 2147483647-number) / random.randint(2, 5)
        return result

    def generate_random_negative_number_for_sum(self):
        # передаем от 1 до макс инт
        number = random.randint(self.left_border, self.right_border)
        result = random.randint(-2147483648+number, -1) / random.randint(2, 5)
        return result


# операнды для деления и вычитания
left_positive_operand = int(GenerateRandomNumbers(1, 2147483646).generate_random_number())
right_positive_operand = int(GenerateRandomNumbers(1, 2147483646).generate_random_number())
left_negative_operand = int(GenerateRandomNumbers(-2147483647, -1).generate_random_number())
right_negative_operand = int(GenerateRandomNumbers(-2147483647, -1).generate_random_number())

# операнды для сложения
left_positive_operand_for_sum = int(GenerateRandomNumbers(1, 2147483646).generate_random_positive_number_for_sum())
right_positive_operand_for_sum = int(GenerateRandomNumbers(1, 2147483646).generate_random_positive_number_for_sum())
left_negative_operand_for_sum = int(GenerateRandomNumbers(1, 2147483646).generate_random_negative_number_for_sum())
right_negative_operand_for_sum = int(GenerateRandomNumbers(1, 2147483646).generate_random_negative_number_for_sum())

# операнды для умножения
left_positive_operand_for_product = int(GenerateRandomNumbers(1, 500).generate_random_number())
right_positive_operand_for_product = int(GenerateRandomNumbers(1, 500).generate_random_number())
left_negative_operand_for_product = int(GenerateRandomNumbers(-500, -1).generate_random_number())
right_negative_operand_for_product = int(GenerateRandomNumbers(-500, -1).generate_random_number())
