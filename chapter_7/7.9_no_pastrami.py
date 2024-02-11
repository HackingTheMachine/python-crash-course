sandwich_orders = ["Tuna", "Pastrami", "Roastbeef", "Salad and tomato"]
finished_sandwich = []
print("The Deli has run out of pastrami")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich.lower() != "pastrami":
        finished_sandwich.append(sandwich)
        print(f"I made your {sandwich} sandwich")
    else:
        print("We have finished the pastrami")

