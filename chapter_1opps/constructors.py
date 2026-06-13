'''Requirements:

Use a constructor to initialize:
employee name
salary
Create a method called display() to print both values.
Create one object and call the method.'''

class Employee_details:
    var1 = "This class tells emp details"
    
    def __init__(self, emp_name, salary):
        self.emp_name = emp_name
        self.salary = salary
    def display(self):
        print(f"The employee name is {self.emp_name}")
        print(f"The employee salary is {self.salary}")
emp1 = Employee_details("Niharika",50000)
print(emp1.var1)
emp1.display()
#another wat to call function
Employee_details.display(emp1)
