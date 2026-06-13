class my_class:
    def __init__(self,a,b):
        self.a = a
        self.b =b
    def __SumSquare__(self):
        res = (self.a**2)+(self.b**2)
        return f"The square of 2 numbers is res"
obj1 = my_class(2,3)
result = obj1
print(result)