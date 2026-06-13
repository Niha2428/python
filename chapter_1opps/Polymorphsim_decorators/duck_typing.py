'''duck typing is a programming concept that allows us to use 
an object of any type as long as it has the required methods or attributes.'''

class Duck:
    def sound(self):
        print("Quack Quack")

class Dog:
    def sound(self):
        print("Bark Bark")

# Function using duck typing
def make_sound(animal):
    animal.sound()

# Objects
d = Duck()
g = Dog()

make_sound(d)
make_sound(g)