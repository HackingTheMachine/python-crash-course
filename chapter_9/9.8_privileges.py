class User:
    def __init__(self, first_name, last_name, age, email, location) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
    def describe_user(self):
        print("User informations:")
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"age: {self.age}")
        print(f"email: {self.email}")
        print(f"location: {self.location}")
    def greet_user(self):
        print(f"Hello {self.first_name}")

class Privileges():
    def __init__(self) -> None:
        self.privileges = ["can add posts", "can delete posts", "can ban users", "can add users"]
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(Privileges):
    def __init__(self) -> None:
        super().__init__()
         

user = User("Lisa", "Smith", 45, "lisa.smith@email.com", "Buffalo")
admin = Admin()

admin.show_privileges()
