# These projects ra einspired from 'BigBookOfSamllPythinProjects, All Rights Reserved, No copyright intentionally.

# Project 1: Deduce a secret three digit number based on clues (Practice using constants) 

"""About the game Bagels: In Bagels, a deductive logic game, you must guess a secret three-digit number 
based on clues. The game offers one of the following hints in response to your guess: 
“Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct 
digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the 
secret number."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels! A game you will love.
          I have a {} digit number in my mind. Do you want to take a guess? Here are some clues: 
          Pico means one digit is correct but in the wrong place.
          Fermi means one digit is correct and in the right place.
          Bagels means no digits are correct.
          Say the number I thought of was 248, and you said 843, the clue would be Fermi, Pico.'''.format(NUM_DIGITS))
    while True:
        secret_num = getSecretNum()
        print('Ready to Guess?')
        print('You have {} guesses to get it'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != len(secret_num) or not guess.isdecimal():
                print('Guess #{}'.format(numGuesses))
                guess = input('>')

            clues = getClues(guess, secret_num)
            print(clues)
            numGuesses += 1

            if guess == secret_num:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}'.format(secret_num))

        print('Thanks for playing. Do you want to play more?')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing! Have a good time.')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
