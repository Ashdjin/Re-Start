import random

isGuessRight = False
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
#print game instructions
#generate random number by importing the random library and calling the randit command
#while or as long as the inputted number doesn't match the randomly generated number, display the "try again" prompt and return to the input promt for the player to input another number
#when the inputted number matches the randomly generated number, display the "You win" prompt and break/end the loop



