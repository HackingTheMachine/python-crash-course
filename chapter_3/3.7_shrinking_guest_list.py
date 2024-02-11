guests = ["Albert Einstein", "Nikola Tesla", "Robert Oppenheimer", "Alan Turing"]
print("I've found a bigger table!")
guests.insert(0, "Alexander the Great")
guests.insert(2, "Winston Churchill")
guests.append("Gengis Khan")

guest_one = guests.pop()
print(f"I'm sorry {guest_one}, I can't invite you anymore")

guest_two = guests.pop()
print(f"I'm sorry {guest_two}, I can't invite you anymore")

guest_three = guests.pop()
print(f"I'm sorry {guest_three}, I can't invite you anymore")

guest_four = guests.pop()
print(f"I'm sorry {guest_four}, I can't invite you anymore")

print(f"Hello {guests[0]}, you're still invited.")
print(f"Hello {guests[1]}, you're still invited.")

del guests[0]
del guests[1]
