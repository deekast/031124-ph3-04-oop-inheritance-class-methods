class Fish:

    all_fish = []

    def __init__(self, name, length_in_inches):
        self.name = name
        self.length_in_inches = length_in_inches
        Fish.all_fish.append(self)

    def __repr__(self):
        return f"Fish(name={self.name}, length_in_inches={self.length_in_inches})"

    def make_bubbles(self):
        return "bloop bloop"

    @classmethod 
    def num_fish(cls):
        return len(cls.all_fish)