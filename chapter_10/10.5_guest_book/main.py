import os
flag = True
guests = []
while flag:
    name = input("Enter the guests name or 'q' to quit: ")
    if name.lower() != 'q': 
        guests.append(name)
    else:
        flag = False

with open('guest_book.txt', 'w') as f:
    for guest in guests:
        f.write(f'{guest}\n')


