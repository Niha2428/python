#single level inheritance

class company:
    title:str= "Consultancy"
    def __init__(self, company_name:str):
        self.company_name = company_name
    def info(self):
        print(f"The company name is {self.company_name}")
        return f"The company name is {self.company_name}"
class employee(company):
    def __init__(self,emp_name:str,company_name:str):
        self.emp_name = emp_name
        self.company_name = company_name
    def emp_details(self):
        response = company.info(self)
        print(f"The employee name is {self.emp_name}, {response}")
    
emp1=employee("Niharika","Epam")
emp1.emp_details()

