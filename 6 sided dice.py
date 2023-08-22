import random

num = input(' press 1 to roll dice: ')
num = int(num)
x=0
while x != 1:
    if num == 1:
        x =+ 1
        dice_num = random.randint(1,6)
        print(dice_num)

    else:
        print('you didn\'t press one.......')