#!/usr/bin/python3
import requests
import json

URL = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(URL)
# json_response = response.json()

# print(response.text)