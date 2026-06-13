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

class contractor(company):
    def __init__(self, contractor_name:str, company_name:str):
        self.contractor_name = contractor_name
        self.company_name = company_name
    
    def contractor_details(self):
        print(f"The contractor name is {self.contractor_name}")
        response =  company.info(self)

contractor1 = contractor("JOHN","Tech Solutions")
contractor1.contractor_details()
