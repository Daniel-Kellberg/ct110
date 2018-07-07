# Python Guessing Game
# CTI 110
# July 1, 2018
# Daniel Kellberg
#


import random

def generateRandomNumber():
    randomNumber = random.randint(1, 100) 
    return randomNumber

def askUserForNumber(message = "Guess the number: " ):
    userNumber = int(input(message))
    return userNumber

def checkUserNumber( userNumber, randomNumber):
    if userNumber > randomNumber:
        return "Too high, try again"
    elif userNumber < randomNumber:
        return "Too low, try again"
    else:
        return "Congratulations!"
        


def main():
    userCongratulated = False
    letsStart = True
    
    while userCongratulated or letsStart:
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        # The print statement on the next line is meant to make finding the correct number easier 
        print( "For testing purposes, random number: ", randomNumber)
        userNumber = askUserForNumber()
        userNumberOfGuesses = userNumberOfGuesses + 1
        message = checkUserNumber(userNumber, randomNumber)

        while message != "Congratulations!":
            print(message)
            userNumber = askUserForNumber( "Try again: ")
            userNumberOfGuesses = userNumberOfGuesses + 1
            
            message = checkUserNumber(userNumber, randomNumber)


        if message == "Congratulations!":
            print("It took you", userNumberOfGuesses, "tries to guess the correct number")
            print("Congratulations!")
            user_input = input(str("Would you like to guess again?: "))

        while user_input == "y":
            userNumberOfGuesses = 0
            randomNumber = generateRandomNumber()
            print( "For testing purposes, random number: ", randomNumber)
            userNumber = askUserForNumber()
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkUserNumber(userNumber, randomNumber)
            while message != "Congratulations!":
                 print(message)
                 userNumber = askUserForNumber( "Try again: ")
                 userNumberOfGuesses = userNumberOfGuesses + 1
                 message = checkUserNumber(userNumber, randomNumber)
            if message == "Congratulations!":
                print("It took you", userNumberOfGuesses, "tries to guess the correct number")
                print("Congratulations!")


                user_input = input(str("Would you like to guess again?: "))

        if user_input == "n":
            print("See you next time!")
            break 
                
           
        print(message)
        userCongratulate = True

main()

        

        
        

