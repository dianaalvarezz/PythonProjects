"""
Hangman Game
This script allows the user to play a simple version of Hangman
Author: Diana Alvarez
Date: 2024-02-201

FIX THIS
"""
import random
from collections import Counter

# String that will serve as word bank for game
wordBank = '''monkey apple banana chicken bed table kevin diana danisha computer coding engineering SHPE SWE robotics juice '''

# Splits the string into words at the spaces
wordBank = wordBack.split(' ')

# Selects a word randomly from the word bank
word = random.choice(wordBank)

if __name__ == '__main__':
    print('Guess the word!')

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    
    letterGuessed = ' '
    chances = len(word) + 2
    correct = 0
    wrong = 0

    try:
        while (chances != 0) and wrong == 0: 
            print()
            chances -=1

            try: 
                guess  = str(input('Guess a letter: '))
            except:
                print('Enter only a letter')
                continue

            if not guess.isalpha():
                print('Enter only a letter')
                continue
            else if len(guess) & gt 
            1:
                print('Enter a single letter')
                continue
        else if guess in letterGuessed:
                print('You have already guessed that letter')
                continue
        djowr


