"""
    Wordle_functions.py
    
    This Module contains functions to solve Wordle
    
    Contains:
    ----------------------------------------
    tile_colours
    reduce_list
    better_reduce_list
    ----------------------------------------
    
    
    Written by Cat Leedham
    
Adding another change
"""

import numpy as np
import pandas as pd

def tile_colours(correct_word,guess):
    """
    Finds the colours of the tiles for each letter of the guess based on the correct word:
    g - correct letter and place
    y - correct letter, wrong place
    b - incorrect letter

    
    Parameters
    ----------
    correct_word: string 
        Must have a length of 5
        Correct word to be compared 
    guess: array of strings
        must have a length of 5
        
    Returns
    ----------
    array of strings
        tile colours for that guess
        5 letters from g,y or b
    """
    
    tiles = ['-','-','-','-','-']
    correct_letters = pd.Series([],index=[]) #Initialising list of letters in the correct word
    not_green_letters = [] #Initialising list of guessed letters that aren't in the correct word


    #For each letter
    for i in range(5):

	#Counting occurences of each letter in the correct word
        if correct_word[i] in correct_letters:
            correct_letters[correct_word[i]] = correct_letters[correct_word[i]] + 1
        else:
            correct_letter = pd.Series([1],index=[correct_word[i]])
            correct_letters = correct_letters.append(correct_letter)

	#If the letter in the guess matches, make that tile green and take the letter away
	#from the count of correct letters. Otherwise add to a list of non-green letters
        if guess[i] == correct_word[i]:
            tiles[i] = 'g'
            correct_letters[guess[i]] = correct_letters[guess[i]] - 1

        else:
            not_green_letters.append(i)

	#For each letter that isn't green, check if it's in the correct word and has enough 
	#that it hasn't already been accounted for by another green or yellow tile            
    for i in not_green_letters:
        if guess[i] in correct_word and correct_letters[guess[i]] > 0:
            tiles[i] = 'y'
            correct_letters[guess[i]] = correct_letters[guess[i]] - 1
        else:
            tiles[i] = 'b'


    return tiles



def reduce_list(words,tiles,guess):
    """
    Reduces current list of words based on the colour of the tiles due to the last guess
    
    Only considers each tile separately
    
    When green (g), excludes words without that letter in that position
    When yellow (y), excludes words not containing that letter and words with that letter in that position
    When black (b), excludes words with that letter in that position

    
    Parameters
    ----------
    words: array of strings
        list of current possible words
    tiles: array of strings
        must have a length of 5
        must include only g, y or b 
    guess: array of strings
        must have a length of 5
        the word corresponding to the colour of the tiles
        
    Returns
    ----------
    array of strings
        reduced list of words allowed by that tile pattern
    """
    if np.size(tiles) != 5:
        if np.size(tiles) > 5:
            raise ValueError('Too many tiles')
        if np.size(tiles) < 5:
            raise ValueError('Not enough tiles')
            
    
    index = 0

    for i in range(5):
        
        if tiles[i] == 'g':
            for word in words: 
                if word[i] != guess[i]:
                    index = np.where(words == word)
                    words = np.delete(words,index)
                    
        if tiles[i] == 'y': 
            for word in words: 
                if word[i] == guess[i]:
                    index = np.where(words == word)
                    words = np.delete(words,index)
                if guess[i] not in word:
                    index = np.where(words == word)
                    words = np.delete(words,index)
                
        if tiles[i] == 'b':
            for word in words: 
                if word[i] == guess[i]:
                    index = np.where(words == word)
                    words = np.delete(words,index)
   
    
    #Removing the guess itself
    index = np.where(words == guess)                
    words = np.delete(words,index)
                
            
    return words





def better_reduce_list(words,tiles,guess):
    """
    Improved version of the reduce_list function
    
    Takes into account the colours of other tiles when excluding words
    
    The first loop is the same as reduce_list
    
    Further actions are taken for each letter in the guess depending on whether they occur once or twice
    

    
    Parameters
    ----------
    words: array of strings
        list of current possible words
    tiles: array of strings
        must have a length of 5
        must include only g, y or b 
    guess: array of strings
        must have a length of 5
        the word corresponding to the colour of the tiles
        
    Returns
    ----------
    array of strings
        reduced list of words allowed by that tile pattern
    """
    if np.size(tiles) != 5:
        if np.size(tiles) > 5:
            raise ValueError('Too many tiles')
        if np.size(tiles) < 5:
            raise ValueError('Not enough tiles')
            
    
    index = 0
   
    
    for i in range(5):
        if tiles[i] == 'g':
            for word in words: 
                if word[i] != guess[i]:
                    index = np.where(words == word)
                    words = np.delete(words,index)
        if tiles[i] == 'y': 
            for word in words: 
                if word[i] == guess[i]:
                    index = np.where(words == word)
                    words = np.delete(words,index)
                if guess[i] not in word:
                    index = np.where(words == word)
                    words = np.delete(words,index)
                
        if tiles[i] == 'b':
            for word in words: 
                if word[i] == guess[i]:
                    index = np.where(words == word)
                    words = np.delete(words,index)
    
    #Removing the guess itself
    index = np.where(words == guess)                
    words = np.delete(words,index)
    
    #Additions to reduce_list start here
    
    
    #Count each letter in the guess
    letters =  pd.Series([],index=[])
    for i in range(5):
        if guess[i] in letters:
            letters[guess[i]] = letters[guess[i]] + 1
        else:
            new_letter = pd.Series([1],index=[guess[i]])
            letters = letters.append(new_letter)
            
    
    
    guess = np.array([*guess])
    colours1 = ['-']
    colours2 = ['-','-']
    
    
    for letter in letters.index:
        
        #Finding all the letters that appear once in the guess
        if letters[letter] == 1:
            pos = np.where(guess == letter) #Position of the letter
            colours1[0] = tiles[pos[0][0]] #Colour of the tile
            if colours1 == ['b']:
                for word in words:
                    if letter in word: 
                        index = np.where(words == word)
                        words = np.delete(words,index)
      
        
        #Finding all the letters that appear twice in the guess
        if letters[letter] == 2:
            pos = np.where(guess == letter) #Positions of the double letters in the guess
            colours2[0] = tiles[pos[0][0]] #Colours of the tiles
            colours2[1] = tiles[pos[0][1]]
            if colours2 == ['g','y'] or colours2 == ['y','g'] or colours2 == ['y','y']:
                for word in words:
                    if np.count_nonzero(np.array(list(word)) == letter) <= 1: #Counting how many of that letter in the guess
                        index = np.where(words == word)
                        words = np.delete(words,index)
            if colours2 == ['g','b'] or colours2 == ['b','g'] or colours2 == ['b','y'] or colours2 == ['y','b']:
                for word in words:
                    if np.count_nonzero(np.array(list(word)) == letter) != 1:
                        index = np.where(words == word)
                        words = np.delete(words,index)
            if colours2 == ['b','b']:
                for word in words:
                    if letter in word:
                        index = np.where(words == word)
                        words = np.delete(words,index)


            
                
            
    return words
        

