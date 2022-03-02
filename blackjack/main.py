############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

############### Our Blackjack House Rules #####################

from art import logo
import random



def drawCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def printUserHand(list, score, final):
    if (final):
        print("Your final hand: {}, final score: {}".format(list, score))
    else:
        print("Your card: {}, current score: {}".format(list, score))

def printCompHand(list, score, final):
    if (final):
        print("Computer final hand: {}, final score: {}".format(list, score))
    else:
        print("Computer's first card: {}".format(list[0]))

def checkWinner(userScore, compScore):
    if (userScore == compScore):
        print("Draw")
    elif(userScore > 21 and compScore > 21 ):
        print("Both over 21.")
    else:
        if (userScore > 21):
            print("You lose")
        elif (compScore > 21):
            print("You win")
        else:
            if (userScore > compScore):
                print("You win")    
            else:
                print("You lose")    

start = input("Do you want to play a game of blackjack \'y\' or \'n\': ")
if (start == 'y'): print(logo)
while(start == 'y'):
    # Draw first two cards for user and computer
    your_card = [drawCard(), drawCard()]
    comp_card = [drawCard(), drawCard()]
   
    # Print hand
    printUserHand(your_card, sum(your_card), False)
    printCompHand(comp_card, sum(comp_card), False)
    
    if (sum(your_card) == sum(comp_card) == 21):
        print("Draw. Both of you draw Black Jack")
    elif (sum(your_card) == 21 or sum(comp_card) == 21):
        print("Black Jack")


    ## User draw card
    draw = input("Type \'y\' to get another card, type \'n\' to pass: ")
    while (draw == 'y'):
        your_card.append(drawCard())
        printUserHand(your_card, sum(your_card), False)
        printCompHand(comp_card, sum(comp_card), False)
        draw = input("Type \'y\' to get another card, type \'n\' to pass: ")
    ## Final card for user
    
    print(sum(comp_card))
    ## Computer's turn draw if in range [17, 21)
    while (sum(comp_card) < 21):
        comp_card.append(drawCard())
        if (sum(comp_card) >= 17):
            break
    
        
    
    printUserHand(your_card, sum(your_card), True)
    printCompHand(comp_card, sum(comp_card), True)

    checkWinner(sum(your_card),sum(comp_card))

    start = input("Play again? \'y\' or \'n\': ")

