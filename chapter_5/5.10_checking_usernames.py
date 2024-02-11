current_users = ["Andrew", "Mark", "Bella", "Joy", "Luca"]
new_users = ["Lisa", "Raj", "Andrew", "Manuel", "Joy"]

for n_user in new_users:
    for c_user in current_users:
        if n_user.lower() == c_user.lower():
            print("The username is already in use")
        else:
            print("The username is available")
