from art import logo
from game_data import data
import random

print(logo)

def game():
    person_A = random.choice(data)
    person_B = random.choice(data)
    while (person_A["name"] == person_B["name"]):
        person_B = random.choice(data)

    print("Compare A: {}, {}, from {}.".format(person_A["name"], person_A["description"],person_A["country"]))
    print("Compare B: {}, {}, from {}.".format(person_B["name"], person_B["description"],person_B["country"]))

    choice = input("Who has more followers? Type \'A\' or \'B\': ")
    if ((choice=='A' or choice =='a' )== (int(person_A["follower_count"]) > int(person_B["follower_count"]))):
        return True
    else:
        return False


point = 0
while(game()):
    point+=1
    print("You are right! Current score: {}".format(point))
    
print("Sorry, that's wrong. Final score: {}".format(point))
    
