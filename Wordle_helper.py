#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 15:54:03 2023

@author: cscl3

Wordle solver to be used alongside the online Wordle

User tries guesses online and tells the program the output

Program uses this to reduce the list of possible words and suggest a next guess

"""

import Wordle_functions as wf
import numpy as np
import re



all_words=np.loadtxt("./OrderedWords12953.txt",dtype="str")
secret_order=np.loadtxt("./OrderedWords2315.txt",dtype="str")

new_list = secret_order

first_guess = 'crane'
answer = '-'

print("Welcome to the Wordle helper!")
print("This interactive program should be used alongisde online Wordle")
print("Just tell it your guess and the colour of the corresponding tiles")
print("It will work out the remaining list of possible words and suggest the next word to guess for you to use if you choose!")
print("Suggested first guess: ", first_guess)
print("Now try a first guess in Wordle online")

out_of_guesses = True


for i in range(6):
    
    Guess = input("Enter your guess:").strip()
    print(Guess)
    
    while Guess not in all_words:
        print("I'm sorry, Wordle won't accept that word. Please try again.")
        Guess = input("Enter your guess:")
        
    
    print()
    print("Enter the colours of the tiles for that guess as 5 letters in a row")
    print("g - green")
    print("y - yellow")
    print("b - black")
    print("e.g. ybgbb")
    
    tiles = input("Tile colours:")
    
    if tiles == 'ggggg':
        print("Well done! You found the correct word!")
        out_of_guesses = False
        break
    
    while len(tiles) != 5 or bool(re.search('^[gby]+$', tiles)) is False:
        if len(tiles) != 5:
            print("That's not the right number of tiles. Please try again.")
    
        if bool(re.search('^[gby]+$', tiles)) is False:
            print("Those aren't valid tile colours. Please use g for green, y for yellow and b for grey. For example: gbbyb")
       
        tiles = input("Tile colours:")


    Tiles = list(tiles)

    new_list = wf.better_reduce_list(new_list,Tiles,Guess)

    words_left = np.size(new_list)
    
    if words_left == 0:
        print("Hmm... there are no words left that fit")
        print("Maybe check your inputs were correct and start again...")
        out_of_guesses = False
        break
    elif words_left == 1:
        print("Only one possible word remains!")
        answer = input("See word (y/n)?: ")
        if answer == 'y'  or answer == 'Y' or answer == 'yes' or answer == 'Yes':
            print(new_list)
            if i == 5:
                print("Looks like you've run out of guesses though")
            else:
                print("Well done for getting to the final word!")
        else:
            print("Okay, you're on your own...")
            if i == 5:
                print("Looks like you've run out of guesses anyway")
        
        out_of_guesses = False
        break
    
    else:
        print("Number of possible words remaining: ",words_left)
        print("Suggestion: ",new_list[0])
        answer = input("See all words remaining (y/n)?: ")
        if answer == 'y'  or answer == 'Y' or answer == 'yes' or answer == 'Yes':
            print(new_list)
    
    
if out_of_guesses == True:
    print("Looks like you've run out of guesses")
    print("There were ",words_left," words remaning")
    
        


        
    
