flag = True
places = []
while flag:
    place = input("If you could visit one place in the world, where would it be (or write 'quit' to exit)? \n")
    if place.lower() != "quit": 
        places.append(place)
    elif place.lower() == "quit":
        break
print(places)
