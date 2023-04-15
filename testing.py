import requests

URL = "http://localhost:8000/quotes"

data = {
    "text": "this is a test quote for testing web application",
    "author": "ali ahmadi"
}

response = requests.post(URL, json=data)

print(str(response.status_code) + " " + response.text)