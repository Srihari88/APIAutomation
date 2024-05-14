import json

import requests

mydata=open("data.json","r").read()
response_object=requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(response_object.status_code)
print(response_object.json())