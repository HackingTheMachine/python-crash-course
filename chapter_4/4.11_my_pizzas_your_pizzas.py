pizzas = ["margherita", "sausages", "french fries"]
friend_pizzas = pizzas[::]

pizzas.append("tuna")
friend_pizzas.append("mushrooms")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")
print("MY friend's favorite pizza are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
