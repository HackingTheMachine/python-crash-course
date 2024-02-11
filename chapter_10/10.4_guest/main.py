name = input("Enter your name: ")

f = open("guest.txt", "w")
f.write(name)

f = open("guest.txt", "r")
print(f.read())
