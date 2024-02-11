class Restaurant:
    def __init__(self, restaurant_name, cousine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cousine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")
    
    def set_number_served(self, new_number):
        self.number_served = new_number
    
    def increment_number_served(self):
        self.number_served += 48

restaurant = Restaurant("La tana", "Italian")

restaurant.number_served = 42
print(restaurant.number_served)
