favorite_languages = {"Mark" : "C++",
                      "Lisa" : "Python",
                      "Joy" : "Java",
                      "Andrew" : "Java",
                      "Richard" : "C",
                      "Rose" : "Haskell"}
pooling_list = ["Mark", "Nami", "Andrew", "Masha", "Plum"]
for name in favorite_languages.items():
    if name in pooling_list:
        print("You already took the pool")
    else:
        print("Please take the pool")
