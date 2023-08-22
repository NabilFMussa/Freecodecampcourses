from math import trunc
import random
from typing import Counter

answer = True
while answer:
     num = input(' type in the highest number you want to go to: ')

     if num.isdigit():
         print('good, lets play')
         num = int(num)
         answer = False
     else:
        print('invalid input try again')

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    guess = input('type in your guess between 1 and ' + str(num)  + ': ' )
    if guess.isdigit():
        guess = int(guess)

        if guess == secret:
         print(' correct ')
        else:
            print(' try again ')
            count += 1

print(' it took you ' + str(count)  + ' tries') 