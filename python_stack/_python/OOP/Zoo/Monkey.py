from Animal import Animal

class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.agility = 120

    def feed(self):
        self.health += 10
        self.happiness += 20  
        return self
