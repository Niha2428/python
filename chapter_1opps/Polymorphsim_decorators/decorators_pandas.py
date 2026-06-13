def pandas_datafram(func):

    def wrapper(*args):
        response = func(*args)

        print("I am converting the csv to parquet format")

        response.to_parquet(
            "c:/Users/RaaviNiharika/Downloads/python_learn/chapter_1opps/Polymorphsim_decorators/data.parquet"
        )

        return response

    return wrapper


@pandas_datafram
def csv_to_parquest(file_path: str):

    import pandas as pd

    df = pd.read_csv(file_path)

    return df


result = csv_to_parquest(
    r"C:\Users\RaaviNiharika\Downloads\python_learn\chapter_1opps\Polymorphsim_decorators\oders.csv"
)

print(result.head())