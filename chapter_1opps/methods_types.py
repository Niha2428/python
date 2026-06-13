class my_class:
    @staticmethod
    def dummy():
        print("This is a static method")
        
obj1 = my_class()
obj1.dummy()
my_class.dummy()

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student name is {self.name}"

obj = Student("Niharika")
print(obj)