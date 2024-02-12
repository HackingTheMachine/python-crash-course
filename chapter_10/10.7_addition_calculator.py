flag = True
sum = []
total = 0
while flag:
    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        sum.append(x + y) 
    except ValueError:
        print("You need to enter a number")

for number in sum:
    total += number

print(total)
