"""Functions"""
import os
def clear():
    os.system('clear')

def board(word, guessedLetters):
    clear()
    acc = ""
    print("="* 10)
    for Letter in word:
        if Letter in guessedLetters:
            acc += " " + Letter +" "
        else:
            acc += " _ "

    notin = ""
    for Letter in guessedLetters:
        if Letter not in word:
            notin += " " + Letter + " "



    return ("\n" * 5) + acc + ("\n") + notin

def guess():
    letter = input('what is your guess: ')
    return letter

def checkCorrect(word, guessedLetters):
    wordLetters = list(word)
    for x in guessedLetters:
        if x in word:
            wordLetters.remove(x)
    if wordLetters == []:
        return True
    return False
