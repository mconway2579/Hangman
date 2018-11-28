"""Functions"""
import os
def clear():
    os.system('clear')

def board(word, guessedLetters):
    """create a way to see whats going on"""
    clear()
    print("="* 10)
    """go through the word, if the letter has been guessed, print the letter.
    if it has yet to be guessed print a blank space"""
    for letter in guessedLetters:
        if letter in word:.............
        else.......

    """print the letters that have yet to be guessed, make sure it is clear that
    they are not part of the word"""



    return (" a string with the spaces/correct words" + ("\n") +
    "a string with the letters not in the word that have been guessed")

def guess():
    """take an input letter as a guess"""
    return letter

def checkCorrect(word, guessedLetters):
    """compare the guessed letters to the letters in the word.
    if all the letters in the word have been guessed return True
    otherwise return false"""
    #return True or False
