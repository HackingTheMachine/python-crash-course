class User:
    def __init__(self, first_name, last_name, age, email, location) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempt = 0
    def describe_user(self):
        print("User informations:")
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"age: {self.age}")
        print(f"email: {self.email}")
        print(f"location: {self.location}")
    def greet_user(self):
        print(f"Hello {self.first_name}")
    def increment_login_attempt(self):
        self.login_attempt += 1
    def reset_login_attempt(self):
        self.login_attempt = 0
user = User("Lisa", "Smith", 45, "lisa.smith@email.com", "Buffalo")

user.describe_user()
user.greet_user()
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()
user.increment_login_attempt()

print(user.login_attempt)

user.reset_login_attempt()
