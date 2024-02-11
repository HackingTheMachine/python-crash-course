favorite_places = {
                    "Mark" : ["Malta", "New York", "Lisbon"],
                    "Lisa" : ["Paris", "London", "Tokyo"],
                    "Anna" : ["Nizza", "Rome", "Wien"]
                   }
for name, cities in favorite_places.items():
    print(name)
    for city in cities:
        print(city)
