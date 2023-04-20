'''
In this game the user will guess letters to a word until they feel confident enough to guess the word entirely.
After each guess the progress on the word reveal will be shown.
It will continue until the user guesses the word of gives up.'''
#------------------------------------------------------------------------------------------------------------------------------------
from random import randint as selectWord
#------------------------------------------------------------------------------------------------------------------------------------
def printBeginPrompt():
    print('''Welcome to Lingo!
    The objective of the game is to guess the word.
    You can guess letter by letter or the entire word.
    After every guess the progress of the word will be shown to you.''')

def guess(correctWord):
    correctlyGuessed = []
    wordSet = set(correctWord)
    revealed = False
    while not revealed:
        print("Here is the word:")
        showWord(correctWord, correctlyGuessed)
        print("Now take a guess: ", end="")
        attempt = input()
        if attempt.__len__() > 1:
            if(attempt.lower() == correctWord.lower()):
                revealed = True
            else:
                print("I'm sorry, thats not correct.")
        else:
            if attempt in correctWord.lower() or attempt in correctWord.upper():
                print("Way to go the word contains", attempt)
                correctlyGuessed.append(attempt.lower())
                correctlyGuessed.append(attempt.upper())
            else:
                print("I'm sorry thats not correct.")
            revealed = checkCompletion(wordSet, correctlyGuessed)
    print("Congradulations, you got it!  The correct word was", correctWord, end="!\n")

def showWord(word, letters):
    for character in word:
        if(character in letters):
            print(character, end="")
        else:
            print("_", end="")
    print("")

def checkCompletion(wordSet, letters):
    result = False
    if wordSet.issubset(letters):
        result = True
    return result

def printEndPrompt():
    response = "!"
    while response != "Y" and response != "y" and response != "N" and response != "n" and response != "":
        print("Thanks for playing Lingo.  Would you like to play again? (Y/N): ",end="")
        response = input()
    return response.upper()
#------------------------------------------------------------------------------------------------------------------------------------
printBeginPrompt()

possibleWords = [
    "Amazing",
    "Terrific",
    "Fantastic",
    "Tubular",
    "Groovy",
    "Tremendous",
    "Outstanding",
    "Incredible"
]

play = "Y"

while play == "Y":
    magicWord = possibleWords[selectWord(0, possibleWords.__len__()-1)]

    guess(magicWord)

    play = printEndPrompt()