import requests

base_url="https://reqres.in/"

resp=requests.get(base_url)
code=resp.status_code
code=resp.status_code
print(code)

assert code==200, "Response code doesn't pass"

