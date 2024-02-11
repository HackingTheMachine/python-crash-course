class Restaurant:
    def __init__(self, restaurant_name, cousine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cousine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant_one = Restaurant("La tana", "Italian")
restaurant_one.describe_restaurant()

restaurant_two = Restaurant("New Dheli", "Indian")
restaurant_two.describe_restaurant()

restaurant_three = Restaurant("Bourgone", "French")
restaurant_three.describe_restaurant()
