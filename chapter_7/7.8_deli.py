sandwich_orders = ["Tuna", "Pastrami", "Roastbeef", "Salad and tomato"]
finished_sandwich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwich.append(sandwich)
    print(f"I made your {sandwich} sandwich")
