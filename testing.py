import requests

URL = "http://localhost:8000/quotes"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"


headers = {
    "Authorization": f"Bearer {TOKEN}"
}


data = {
    "text": "quote quote quote",
    "author": "ali ali ali"
}

data_get = {
    
}

response = requests.get(URL)

print(str(response.status_code) + " " + response.text)