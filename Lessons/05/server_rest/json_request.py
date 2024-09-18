import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/5"

response = requests.get(api_url)

print(f"\nResponse class instance: {type(response.json())}")

print(f"\nResponse status code: {response.status_code}")

print(f"\nResponse content type: {response.headers['Content-Type']}")

if(response.status_code==200):
    if (type(response.json()) is dict):
        print(f"\nResponse data:\n{json.dumps(response.json(), indent = 4)}")