from classes.mammal import Mammal


class Dog(Mammal):

    def __init__(self, name, rested, is_good=True):
        self.name = name
        self.rested = rested
        self.is_good = is_good

    def __repr__(self):
        return f"Dog(name={self.name}, rested={self.rested}, is_good={self.is_good})"

    def make_sound(self):
        return "generic mammal sound"

    def sleep(self):
        self.rested = True

    def run_around(self):
        self.rested = False