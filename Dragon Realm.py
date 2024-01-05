#Dragon Realm
#12/29/2023 William Richman

import random
import time


def displayIntro():
    print('''You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other cave's dragon is greedy and hungry, and will eat you on sight.''')
    print()

def choseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into to? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approch the cave... ')
    time.sleep(1)
    print('It is dark and spooky...')  
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and ...')
    time.sleep(3)
    print()
    time.sleep(2)


    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure !')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = choseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (Yes or No)')
    playAgain = input()

