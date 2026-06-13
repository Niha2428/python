# example of method overriding in python
'''If a subclass has a method with the same name, same parameters, and same return 
behavior as  the parent class method, the child class method overrides the parent
 method.'''

class animal:
    def make_sound(self):
        print("Animal speaks")
class dog(animal):
    def make_sound(self):
        print("Dog barks")
class cat(animal):
    def make_sound(self):
        print("Cat meows")
obj = animal()
obj.make_sound() # parent classo/p: Animal speaks
obj1 = dog()
obj1.make_sound() # # Overridden method o/p: Dog barks
obj2 = cat()
obj2.make_sound() # Overridden method o/p: Cat meows
