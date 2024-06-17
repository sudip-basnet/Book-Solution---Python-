import json

file_name = 'number.json'

with open(file_name) as f:
    number=json.load(f)

print(f"Your favorite number is {number}.")
