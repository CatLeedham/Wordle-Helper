"""

Unit tests for the functions in Module file 'Wordle_functions.py'


"""

import numpy as np
import Wordle_functions as wf



words=np.loadtxt("./OrderedWords12953.txt",dtype="str") 
word_list = list(words)


def test_tile_colours():
    assert(wf.tile_colours('scare','aback') == ['b','b','g','y','b'])
    
    
def test_better_reduced():
    reduced_list = list(wf.better_reduce_list(words,['g','b','g','g','g'],'scare'))
    for word in reduced_list:
        word_list.remove(word) #Excluded words
    for word in word_list:
        assert(wf.tile_colours(word,'scare') != ['g','b','g','g','g']) #Checking that none of the excluded words could've produced the desired tile colours



