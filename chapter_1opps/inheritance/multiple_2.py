class company:
    def __init__(self, comp_name:str):
        self.comp_name = comp_name
    def info(self):
        return f"The company name is {self.comp_name}"
class client_comp:
    def __init__(self, cli_comp_name:str):
        self.cli_comp_name = cli_comp_name

    def info(self):
        return f"The Client Company name is {self.cli_comp_name}"
class employee(company, client_comp):
    def __init__(self, emp_name:str, comp_name:str, cli_comp_name:str ):
        self.emp_name = emp_name
        self.comp_name = comp_name
        self.cli_comp_name = cli_comp_name
    def info(self):
        res1 = company.info(self)
        print(res1)
        res2 = client_comp.info(self)
        print(res2)
        print(f"The Employee name is {self.emp_name}")

employee1 = employee("Niharika","EPAM SYSTEMS","AMAZON")
employee1.info()
