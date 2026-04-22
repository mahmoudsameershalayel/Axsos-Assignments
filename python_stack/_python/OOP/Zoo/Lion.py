from Animal import Animal

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.roar_power = 100

    def feed(self):
        self.health += 10
        self.happiness += 15  
        return self
