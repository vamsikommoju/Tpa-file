import requests
URL = 'http://127.0.0.1:8000/app1/details'

req1  =  requests.get(url=URL)

data = req1.json()

print(data)