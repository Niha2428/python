'''Create a Python class called BankAccount.

Requirements:

Use a constructor to initialize:
account holder name
private balance variable (__balance)
Create methods:
deposit(amount) → add money
withdraw(amount) → subtract money only if balance is sufficient
get_balance() → display current balance
Create an object and perform:
one deposit
one withdrawal
print final balance'''

class BankAccount:
    def __init__(self,name,balance):
        self.name=name #private
        self.__balance = balance #procted

    def deposit(self, money):
        self.__balance = self.__balance + money
        print(f"The amount deposited to the account is {money}")
        print(f"Now your account balance is {self.__balance}")
    def withdraw(self, money):
        if(money>self.__balance):
            print("No sufficient balance avaliable")
        else:
            self.__balance = self.__balance - money
            print(f"The amount withdrawn from your account is {money}")
            print(f"Now your account balance is {self.__balance}")
    def get_balance(self):
        print(f"Current balance is {self.__balance}")

acc1 = BankAccount("Niharika",1000)
acc1.deposit(500)
acc1.withdraw(20000)
acc1.get_balance()

