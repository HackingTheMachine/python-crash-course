user_info = {}
def build_profile(name, surname, **user_info):
    user_info['first name'] = name
    user_info['last name'] = surname
    return user_info

user_profile = build_profile("Michael", "Smith", location = "Caltec", age = 29, occupation = "Nuclear physicist")

print(user_profile)
