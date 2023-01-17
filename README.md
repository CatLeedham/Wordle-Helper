# Wordle-Helper

Wordle-Helper can compare a guess and its corresponding tile colours to exclude words as possible solutions. The remaining list of words can help users decide their next guess.

There is also a solver feature that will run until it finds a given correct word.

All scripts are written in Python.

# How Does Wordle-Helper Work?

Wordle helper compares the guess and corresponding tile colours inputted by the user to exclude words from the list of accepted Wordle words. Initially, it only used the tile colours separately, but was improved to consider all letters of the guess together. For example, without considering the other letters, a grey tile only means you can exclude any words with that letter in that position. If you knew there was only one of that letter in the guess, you could then exclude all words without that letter anywhere as it would otherwise be yellow. The diagram below shows the actions taken by the program for different circumstances:

![Tile Flowchart](https://github.com/CatLeedham/Wordle-Helper/Excluding_words.png)

The Wordle solver also uses a function to work out the tile colours based on the guess and correct word using the algorithm below:

![Tile Flowchart](https://github.com/CatLeedham/Wordle-Helper/Tile_colours.png)

# Wordle Helper Usage

The file Wordle_helper.py should be used alongside online Wordle. It asks the user for their guess and the tile colours at each stage of the game.
It will reduce the list of words based on this and suggest the next word to guess. The user also has the option of seeing all remaining words.

# Wordle Solver Usage

The file Wordle_solver.py takes the correct word as an input and will make guesses and reduce the list until it solves it.
