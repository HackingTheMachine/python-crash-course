people = {
    "Andrew": {
            "first_name" : "Andrew",
            "last_name" : "Red",
            "age" : 29,
            "city" : "Milan"},
          
    "Rose": {
        "first_name" : "Rose",
        "last_name" : "Plum",
        "age" : 22,
        "city" : "Manchester"}, 
          

    "Lisa": {
        "first_name" : "Lisa",
        "last_name" : "Esposito",
        "age" : 34,
        "city" : "Naples"}, 
}

for key,value in people.items():
    for key,value in value.items():
        print(key,value)
