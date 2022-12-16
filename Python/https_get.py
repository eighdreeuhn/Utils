import requests

post = requests.post('https://web-space-api.herokuapp.com/users', None, {'name': 'OK... done for tonight'})
print(post)
users = requests.get('https://web-space-api.herokuapp.com/users').json()
print(users)
