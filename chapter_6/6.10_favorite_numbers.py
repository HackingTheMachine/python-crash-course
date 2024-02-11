favorite_numbers = {"Anna" : [12,6,89],
                    "Mark" : [56,3,65],
                    "Max" : [7,1,34],
                    "Robert" : [98,5,3,73],
                    "Lia" : [4,9,99]}
for name, numbers in favorite_numbers.items():
    print(name.upper())
    for number in numbers:
        print(f"\t-{number}")
