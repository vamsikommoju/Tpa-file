import requests
import json
# from itertools import count
URL = 'http://127.0.0.1:8000/app1/courses'

# id = count(1000,9999)

data = {
    'id': 2,
    'cname':'Django3.2',
    'dur':150,
    'fee':12000
}

json_data = json.dumps(data)
req1  =  requests.put(url=URL,data=json_data)
data = req1.json()
print(data)