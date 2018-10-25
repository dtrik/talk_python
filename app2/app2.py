# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:50:25 2018

@author: damodara
"""

import random

print('---------------------------------------')
print('       GUESS THE NUMBER APP')
print('---------------------------------------')
print()

num = random.randint(0,100)

guess = -1
while guess != num:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if int(guess) > num:
        print('Sorry but {} is higher than the number'.format(guess_text))
    elif int(guess) < num:
        print('Sorry but {} is lower than the number'.format(guess_text))
    else:
        print('Yes! You\'ve got it, {} is the correct number'.format(guess_text))
