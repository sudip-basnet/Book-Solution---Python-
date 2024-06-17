message = input("Enter your name.")

with open('guest.txt','w') as file_obj:
    file_obj.write(message)
