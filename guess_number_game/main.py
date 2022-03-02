from art import art
import random
print(art)

def isCorrect(number, guess):
    if (guess < number):
        print("Too low")
        return False
    elif (guess > number):
        print("Too high")
        return False
    else:
        print("Correct")
        return True

def game(mode, number):
    attemps = 1
    if(mode=='easy'):
        attemps = 5
    elif(mode=='hard'):
        attemps = 10
    else:
        attemps = 1
    print("You have {} attemps remaining to guess the number".format(attemps))

    guess = int(input("Make a guess: "))
    # in number of attemps, must make correct guess
    for i in range (attemps-1):
        if(isCorrect(number, guess)):
            return print("You got it. The number is {} :)".format(number))
        print("You have {} attempts left.".format(attemps-1-i))
        guess = int(input("Make a guess: "))
    return print("You've run out of guesses, you lose :(")


choice = input("Ready? Type \'y\' or \'n\': ") 
while (choice=='y'):
    number = random.randrange(100) 
    print("The number is {}".format(number))
    level =  input("Choose a difficulty. Type \'easy\' or \'hard\': ") 
    game(level, number)

    choice = input("Again? Type \'y\' or \'n\': ") 
