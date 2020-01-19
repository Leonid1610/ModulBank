from random import choice
from string import ascii_uppercase


class SymbolGenerator(object):
    def __init__(self, count):
        self.count = count

    def generate_random_symbol(self):
        return ''.join(choice(ascii_uppercase) for i in range(self.count))


random_symbol = SymbolGenerator(1).generate_random_symbol()
