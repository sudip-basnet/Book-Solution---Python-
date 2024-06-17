import json

number = input("Enter your favorite number.")

file_name = 'number.json'

with open(file_name,'w') as f:
    json.dump(number,f)
