#5.1
name = 'Albert'

print("Is name == 'Albert'? I predict True.")
print(name=='Albert')

print("\nIs name =='Einstien?' I predict False.")
print(name=='Einstien')

if name =='Albert':
    print(f"\nHello,{name}")

name ='Einstien'

if name!='Albert':
    print(f"Hello,{name}. I had expected you to be Albert.")