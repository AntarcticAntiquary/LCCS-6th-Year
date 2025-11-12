# Question 16(a)
# Student name: Daniel Lewis

import random as r

def roll_check(roll, guess):
    if roll == guess:
        return 'You guessed correct, well done!'
    elif roll < guess:
        return 'You guessed too high!'
    elif roll > guess:
        return 'You guessed too low!'

def dice_game():
    print('Welcome to my dice game!')
    print()
    your_name = input('Please enter your name :')
    # part (ii) follows
    lucky_number=int(input('Please enter a lucky number between 1 and 6 :'))
    computer_die_roll = r.randint(1,6) # part (i) - Initialise computer number
    # By the by, we spell it with an 's' this side of the Atlantic
     
    print(f'{your_name}\'s lucky number was: {lucky_number}') # part (iii)
    print('The computer rolled: ', computer_die_roll)
    print(roll_check(computer_die_roll, lucky_number))

# your_name = input('Please enter your name :')
# #lucky_number = 5 # part (ii) follows
# lucky_number=int(input('Please enter a lucky number between 1 and 6 :'))
# computer_die_roll = r.randint(1,6) # part (i) - Initialise computer number
# # By the by, we spell it with an 's' this side of the Atlantic
# 
# print(f'{your_name}\'s lucky number was: {lucky_number}') # part (iii)
# print('The computer rolled: ', computer_die_roll)

dice_game()
