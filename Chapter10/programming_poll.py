key = True
with open('programming_poll.txt','w') as file_obj:
    while key:
        message = input("Why do you like programming?")
        if message == 'q':
            break
        else:
            word = f"{message}\n"
            file_obj.write(word) 