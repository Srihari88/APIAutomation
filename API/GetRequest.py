import requests
p={"page":2}

responses=requests.get("https://reqres.in/api/users?",params=p)
page_json=responses.json()
assert page_json['page']==2, 'Pages not match'
assert page_json['total']==12, 'Total Pages not match'
assert page_json['data'][0]['email']=='michael.lawson@reqres.in', 'Email not matched'
