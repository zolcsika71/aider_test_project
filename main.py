import requests

def get_example_data():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    data = get_example_data()
    print(data)
