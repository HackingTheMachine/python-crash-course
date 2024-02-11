flag = True
while flag:
    topping = input("Enter the topping you want to add on your pizza: ")
    if topping.lower() != "quit":
        print(f"We are adding {topping} to your pizza.")
    elif topping.lower() == "quit":
        flag = False
