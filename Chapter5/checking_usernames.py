current_users = ['Sudip','Sandip','Safal','admin','Hira']
lower_users =[]
for users in current_users :
    lower_users.append(users.lower())

print(lower_users)
    
new_users = ['Rohan','Hira','Sudip','Sagar','Susan']

for users in new_users:
    if users.lower() in lower_users:
        print("You will need to enter a new username.")
    else:
        print("The username is available.")
