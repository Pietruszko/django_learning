import requests
URL = 'http://127.0.0.1:8000'

def add_task():
    try: 
        response = requests.post(URL + '/add-todo/', json={'title': 'Do laundry', 
                    'description': 'Black and color'})
        if response.status_code == 201:
            print(response.json())
        else:
            print('Failed to add task')
    except requests.exceptions.RequestException as e:
        print(f'Failed to send request: {e}')
        print('Server might be in loadign state. Please try again after some time.')

def add_category():
    try: 
        response = requests.post(URL + '/add-category/', json={'name': 'Groceries'})
        if response.status_code == 201:
            print(response.json())
        else:
            print('Failed to add category')
    except requests.exceptions.RequestException as e:
        print(f'Failed to send request: {e}')
        print('Server might be in loadign state. Please try again after some time.')

def add_todo_with_category():
    try: 
        response = requests.post(URL + '/add-todo-with-category/', json={'title': 'Buy groceries', 
                    'description': 'Need to buy milk, eggs and bread',
                    'name': 'Groceries'})
        if response.status_code == 201:
            print(response.json())
        else:
            print('Failed to add todo with category')
    except requests.exceptions.RequestException as e:
        print(f'Failed to send request: {e}')
        print('Server might be in loadign state. Please try again after some time.')

add_category()
add_todo_with_category()