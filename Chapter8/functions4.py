#8.9,8.10,8.11
def show_messages(names):
    print("The list is:")
    for name in names:
        print(name)

def send_messages(names,final):
    while names:
        send = names.pop()
        print(f"{send} has been sent.")
        final.append(send)

lists = ['sudip','sandip','sankalpa']
final =[]

#printing original list
print(lists)
#sending messages into the another lists 
send_messages(lists[:],final)
#printing the original list
print(f"The final list is : {final}.")
#printing the unaffected list
show_messages(lists)