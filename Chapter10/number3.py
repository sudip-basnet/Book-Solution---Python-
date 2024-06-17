import json

file_name = 'number.json'

try:
    with open(file_name) as f:
        number = json.load(f)
except:
    with open(file_name,'w') as f:
        number = input("Enter your favorite number.")
        json.dump(number,f)
        print("We will remember your number next time.")
else:
    print(f"Your favorite number is {number}.")