class Restaurant:
    def __init__(self, restaurant_name, cousine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cousine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cousine_type) -> None:
        super().__init__(restaurant_name, cousine_type)
        self.flavors = ["Chocolate", "Hazelnut", "Strawberry", "Yogurt"]

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand("Grom", "Ice cream stand")
ice_cream_stand.display_flavors()
