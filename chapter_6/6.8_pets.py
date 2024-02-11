pets = {
    "Gengis" : {
        "Species" : "cat",
        "Owner" : "Letitia"
    },
    "Basco" : {
        "Species" : "dog",
        "Owner" : "Frank"
    },
    "Mia" : {
        "Species" : "cat",
        "Owner" : "Frank"
    }
}
for name, info in pets.items():
    for species, owner in info.items():
        print(f"name: {name}, \n{species} \n{owner}")
