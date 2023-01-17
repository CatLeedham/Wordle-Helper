"""

Automatic Wordle solver

Takes a correct word as an input

Makes a guess
Calculates tile colours for that guess
Excludes words that don't fit 
Makes subsequent guesses until the correct word is found

Making a change
"""


import Wordle_functions as wf
import numpy as np
import random


word_list=np.loadtxt("./OrderedWords12953.txt",dtype="str")


print("Welcome to the Wordle solver!")
print("Choose a word and it will make guesses until it finds it")

correct_word = input("Choose a word:")

while correct_word not in word_list:
        print("I'm sorry, that word is not in the list of accepted Wordle words")
        correct_word = input("Choose a word:")
        
    

guess1 = 'crane'
guess2 = 'slipt'






tiles = wf.tile_colours(correct_word,guess1) 
word_list = wf.better_reduce_list(word_list,tiles,guess1)
words_left = np.size(word_list)

print("Guess 1 :",guess1,"   Words left:", words_left)


#Just in case it gets it on the first try
if words_left == 0:
        assert(guess1 == correct_word)
        print("Solved in 1 guess!")
        
else:
    guess = guess2
    for i in range(26):
        tiles = wf.tile_colours(correct_word,guess) #Calculating tile colours
        word_list = wf.better_reduce_list(word_list,tiles,guess) #Excluding words
        words_left = np.size(word_list)
      
        print( "Guess", i+2,":",guess,"   Words left: ", np.size(word_list))
        if words_left == 0:
            assert(guess == correct_word)
    
            print("Solved in",i+2,"guesses!")
            break
        else:
            guess = word_list[0]
    
            
            
        








