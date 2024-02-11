class Privileges():
    def __init__(self) -> None:
        self.privileges = ["can add posts", "can delete posts", "can ban users", "can add users"]
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


