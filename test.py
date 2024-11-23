import requests

r = requests.post("http://127.0.0.1:8000/login", json={"login": "test", "password": "test", "body": "test"})

print(r.json())
