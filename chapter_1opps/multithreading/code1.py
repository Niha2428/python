''' multithreading is a technique in which multiple threads are created within a 
single process to execute tasks concurrently. Each thread runs independently 
and can perform different tasks simultaneously, allowing for improved performance 
 and responsiveness in applications. Multithreading is commonly used in scenarios 
where tasks can be executed in parallel, such as handling user input, 
performing background operations, or processing large datasets.
It can help to optimize resource utilization and enhance the overall efficiency 
of an application.'''

# Thread pool executor is modern way to create and manage threads in python
import time
from concurrent.futures import ThreadPoolExecutor

def data_fetch(url:str):
    print(f"Data is fetching from {url} ")
    time.sleep(5)
    print(f"Data fetched from {url} ")
list_of_urls = ["https://data1",
                "https://data2",
                "https://data3",
                "https://data4",
                "https://data5",]
results = []
with ThreadPoolExecutor(max_workers=len(list_of_urls)) as executor:
    futures = executor.map(data_fetch, list_of_urls)
    results.extend(futures)


