cities = {
    "Rome" : {
        "country" : "Italy",
        "population" : 2800000,
        "foundation's year" : "753 B.C."
    },
    "Berlin" : {
        "country" : "Germany",
        "population" : 3600000,
        "foundation's year" : "1237 C.E."
    },
    "London" : {

        "country" : "Great britain",
        "population" : 9000000,
        "foundation's year" : "47 C.E."
    },
}

for name,value in cities.items():
    print(f"{name}:")
    for label,data in value.items():
        print(f"{label}: {data}")
