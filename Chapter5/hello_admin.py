#5.8 and 5.9
usernames = ['Sudip','Sandip','Safal','admin','Hira']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin,would you like to see a status report?")
        else :
         print(f"Hello {username},thankyou for logging in again.")
else:
   print("We have to find some users.")

