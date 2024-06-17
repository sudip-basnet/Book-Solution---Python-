#8.12
def sandwich(*items):
    print("The sandwich contains following items:")
    for item in items:
        print(item)

sandwich('cheese')
sandwich('cheese','pepperoni','meat')
sandwich('egg','chicken')

#8.13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('sudip', 'basnet',location ='Nepal',education='Bachelors',aim='Computer Engineer')
print(user_profile)

#8.14
def car_details (manuf,name,**details):
    details['manufacture'] = manuf
    details['model name']=name
    return details

detail = car_details('Maruti','900',color = 'Red',insurance = False)
print(detail)