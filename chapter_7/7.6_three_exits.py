flag = True
while flag:
    age = input("Tell me your age or write 'quit' to exit: ")
    if int(age) < 3:
        print("The ticket is free")
    elif int(age) >= 3 and int(age) <= 12:
        print("The ticket is $10")
    elif int(age) > 12:
        print("The ticket is $15")
    elif age.lower() == "quit":
        flag = False
