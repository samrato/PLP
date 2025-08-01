
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self._age} years old.")
class Superhero(Person):
    def __init__(self, name, age, superpower, alias):
        super().__init__(name, age)
        self.superpower = superpower
        self.alias = alias

    def use_power(self):
        print(f"{self.alias} uses {self.superpower}! ")

    def introduce(self): 
        print(f"I am {self.alias}, also known as {self.name}. Age: {self._age}")
hero1 = Superhero("Bruce Wayne", 35, "Martial Arts", "Batman")
hero2 = Superhero("Diana Prince", 5000, "Super Strength", "Wonder Woman")
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
