"""

Automatic Wordle solver

Takes a correct word as an input

Makes a guess
Calculates tile colours for that guess
Excludes words that don't fit 
Makes subsequent guesses until the correct word is found


"""

 
 

import Wordle_functions as wf
import numpy as np




full_list=np.loadtxt("./OrderedWords12953.txt",dtype="str")
short_list=np.loadtxt("./OrderedWords2315.txt",dtype="str")

print("Welcome to the Wordle solver!")
print("Choose a word and it will make guesses until it finds it")
print("This solver can operate from the full list of accepted Wordle words or the shorter list of words that Wordle selects the solution from.")
print("Which list would you like it to start with?")
print("Full - f")
print("Short - s")
choice = input("Choose list:")

while choice != 'f' and choice != 's':    
    print("I'm sorry, that input isn't accepted. Please type 'f' or 's'")
    choice = input("Choose list:")
        

print("Now choose a word for it to find")

correct_word = input("Choose a word:")

if choice == 'f':
	while correct_word not in full_list:
		print("I'm sorry, that word is not in the list of accepted Wordle words")
		correct_word = input("Choose a word:")
		
	    

	guess1 = 'crane'
	guess2 = 'slipt'






	tiles = wf.tile_colours(correct_word,guess1) 
	full_list = wf.better_reduce_list(full_list,tiles,guess1)
	words_left = np.size(full_list)

	print("Guess 1 :",guess1,"   Words left:", words_left)


	#Just in case it gets it on the first try
	if words_left == 0:
		assert(guess1 == correct_word)
		print("Solved in 1 guess!")
		
	else:
	    guess = guess2
	    for i in range(26):
    		tiles = wf.tile_colours(correct_word,guess) #Calculating tile colours
    		full_list = wf.better_reduce_list(full_list,tiles,guess) #Excluding words
    		words_left = np.size(full_list)
    	      
    		print( "Guess", i+2,":",guess,"   Words left: ", np.size(full_list))
    		if words_left == 0:
    		    assert(guess == correct_word)
    	    
    		    print("Solved in",i+2,"guesses!")
    		    break
    		else:
    		    guess = full_list[0]

elif choice == 's':
	while correct_word not in short_list:
		print("I'm sorry, that word is not in the shorter list of possible solutions")
		correct_word = input("Choose a word:")
		
	    

	guess1 = 'crane'
	guess2 = 'slipt'






	tiles = wf.tile_colours(correct_word,guess1) 
	short_list = wf.better_reduce_list(short_list,tiles,guess1)
	words_left = np.size(short_list)

	print("Guess 1 :",guess1,"   Words left:", words_left)


	#Just in case it gets it on the first try
	if words_left == 0:
		assert(guess1 == correct_word)
		print("Solved in 1 guess!")
		
	else:
	    guess = guess2
	    for i in range(26):
    		tiles = wf.tile_colours(correct_word,guess) #Calculating tile colours
    		short_list = wf.better_reduce_list(short_list,tiles,guess) #Excluding words
    		words_left = np.size(short_list)
    	      
    		print( "Guess", i+2,":",guess,"   Words left: ", np.size(short_list))
    		if words_left == 0:
    		    assert(guess == correct_word)
    	    
    		    print("Solved in",i+2,"guesses!")
    		    break
    		else:
    		    guess = short_list[0]
	    
		    


        








