# example 1
class my_class:

    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return f"my name is {self.name}"
obj1 = my_class("Niharika")
print(obj1)

# example 2

class number:

    def __init__(self,number):
        self.number = number
    
    def __add__(self,other):
        return f"The addition is {self.number+other.number}"
obj1 = number(20)
obj2 = number(30)
print(obj1+obj2)


