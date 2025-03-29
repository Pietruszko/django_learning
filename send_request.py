import requests
URL = 'http://127.0.0.1:8000'
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