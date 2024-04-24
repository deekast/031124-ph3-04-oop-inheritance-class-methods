from classes.mammal import Mammal

class Cat(Mammal):

    def __init__(self, name, rested=True, lives_remaining=9):
        super().__init__(name = name, rested = rested)
        self.lives_remaining = lives_remaining

    def __repr__(self):
        return f"Cat(name={self.name}, rested={self.rested}, lives_remaining={self.lives_remaining})"

    def make_sound(self):
        return "MEOW"

    def sleep(self):
        super().sleep()
        self.rested = True

    def run_around(self):
        self.rested = False
        