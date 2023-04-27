import requests
import json
# from itertools import count
URL = 'http://127.0.0.1:8000/app1/details'

# id = count(1000,9999)

data = {
    # 'id': next(id),
    'name':'Revi',
    'age':22,
    'city':'Bangolore'
}

json_data = json.dumps(data)
req1  =  requests.post(url=URL,data=json_data)
data = req1.json()
print(data)