from random import randint 

class Dice():
    def __init__(self, sides = 6) -> None:
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))

dice = Dice()
for i in range(1,11):
    dice.roll_die()

dice_ten = Dice(10)
for i in range(1,11):
    dice_ten.roll_die()

dice_twenty = Dice(20)
for i in range(1,11):
    dice_twenty.roll_die()


