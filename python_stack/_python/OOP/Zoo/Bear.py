from Animal import Animal

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.strength = 200
        
    def feed(self):
        self.health += 15  
        self.happiness += 10
        return self
