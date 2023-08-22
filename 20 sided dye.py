import random
import tkinter


inp = input("press press any number 0-10 to roll the dice")
inp = int(inp)

if inp == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 0:
    dice_roll = random.randint(1,20)
    print(dice_roll)

else:
     print("you didn\'t press 1")