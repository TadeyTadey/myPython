class Dog:

    def __init__ (self, name):
        self.name = name

    def voice(self):
        print("gaf gaf")
    
    def run(self):
        print(self.name + " has running")

    def trick(self):
        print(self.name + " do a trick")

Pidbull = Dog('Sharik')

class Cat(Dog):
    def voice(self):
        print("Meow")
    
    def jump(self):
        print("Jumping")
    

Pidbull.trick()
