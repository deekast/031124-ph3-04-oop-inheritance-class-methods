class Bird:
    description = "its a bird"

    all_birds = []

    def __init__(self, name):
        self.name = name
        Bird.all_birds.append(self)

    def __repr__(self):
        return f"Bird(name={self.name})"

    def tweet(self):
        return f"{self.name} is posting all their tweets... I mean X's"
    
    @classmethod
    def fly(cls):
        for bird in cls.all_birds:
            print(f"{bird.name} is taking flight")
