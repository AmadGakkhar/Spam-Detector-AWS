# from sample_flask import app

# with app.test_client() as client:
#     response = client.get('/')
#     print(response)

import json, requests
r1 = requests.get('http://127.0.0.1:8080/')
r2 = requests.post('http://127.0.0.1:8080/home',params = {'message': "hi"})
print(r1)
print(r1.content)
print(r2)
print(r2.content)