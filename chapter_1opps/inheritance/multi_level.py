class company:

    def __init__(self,comp_name:str):
        self.comp_name = comp_name
    def info(self):
        return f"The company is {self.comp_name}"

class manager(company):
    def __init__(self,manager_name:str,comp_name:str):
        self.manager_name = manager_name
        self.comp_name = comp_name
    def info(self):
        res = company.info(self)
        print(res)
        return f"The manager name is {self.manager_name}"
class employee(company):
    def __init__(self, emp_name:str, manager_name:str,comp_name:str):
        self.emp_name = emp_name
        self.manager_name = manager_name
        self.comp_name = comp_name
    def info(self):
        res = manager.info(self)
        print(res)
        print(f"The employee name is {self.emp_name}")

emp1 = employee("Niharika","Sita","Epam Systems")
emp1.info()


