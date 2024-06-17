key = True
with open('guest_book.txt','w') as file_obj:
    while key:
        message = input("Enter the name.")
        if message == 'q':
            break
        else:
            word = f"{message}\n"
            file_obj.write(word) 