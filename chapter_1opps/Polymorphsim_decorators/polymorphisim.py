'''polymorphism is the ability of an object to take on many forms. 
It allows us to use a single interface to represent different types of objects. 
In Python, polymorphism is achieved through method overriding and duck typing.'''

class api_fetcher:
    def fetch_data(self):
        print("The data is fetching from api")
class db_fetch:
    def fetch_data(self):
        print("The data is fetching from data base")
class az_fetch:
    def fetch_data(self):
        print("The data is fetching from azure cloud")

obj1 = api_fetcher()
obj1.fetch_data()
obj2 = db_fetch()
obj2.fetch_data()
obj3 = az_fetch()
obj3.fetch_data()

    