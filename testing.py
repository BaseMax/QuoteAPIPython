import requests

URL = "http://localhost:8000/quotes/1"

data = {
    "text": "this is a test quote for testing web application (edited)",
    "author": "ali ahmadi (edited)"
}

response = requests.put(URL, json=data)

print(str(response.status_code) + " " + response.text)