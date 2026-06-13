def my_decorator(func):
    def wrapper(*args):
        print("Before calling function")
        result= func(*args)
        print("After calling function")
        return result
    return wrapper
@ my_decorator
def fetch_data(url:str,path:str):
    return f"I fetch data from {url} and save it to {path}"
response = fetch_data("https://google.com","c:/users")
print(response)
