#!usr/bin/env python

import random
from time import sleep

#Greeting Message for the start of the program
print("-------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------")
print("   ________ ____ ______________ _________ _________.___ _______    ________    ________    _____      _____  ___________ ")
print("  /  _____/|    |   \_   _____//   _____//   _____/|   |\      \  /  _____/   /  _____/   /  _  \    /     \ \_   _____/ ")
print(" /   \  ___|    |   /|    __)_ \_____  \ \_____  \ |   |/   |   \/   \  ___  /   \  ___  /  /_\  \  /  \ /  \ |    __)_  ")
print(" \    \_\  \    |  / |        \/        \/        \|   /    |    \    \_\  \ \    \_\  \/    |    \/    Y    \|        \ ")
print("  \______  /______/ /_______  /_______  /_______  /|___\____|__  /\______  /  \______  /\____|__  /\____|__  /_______  / ")
print("         \/                 \/        \/        \/             \/        \/          \/         \/         \/        \/  ")
print("-------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------             BY: Mythical                --------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------")


MIN, MAX = 1, 100
NUMBER = random.randint(MIN, MAX)
chances = 5

while chances > 0:
    print("")
    GUESS = int(input("Guess a number between "+ str(MIN)+ " & "+ str(MAX)+ " : "))
    sleep(1)
    print("")
    

    if GUESS == NUMBER:
        print("Congradulations! You have guessed correctly")
        break

    elif GUESS < NUMBER:
        print("You were too -- LOW --, please guess again ")
        chances -= 1
        print(" [+] you have (", chances, ") left.")
        GUESS 
        

    elif GUESS > NUMBER:
        print("You were too -- HIGH --, please guess again ")
        chances -= 1
        print(" [+] you have (", chances, ") left.")
        GUESS
          
if not chances < 0:
    print("")
    print("             ______ _____ _   _ _____      ______  _____ _   _ _____          ")
    print("             | ___ \_   _| \ | |  __ \     | ___ \|  _  | \ | |  __ \         ")
    print("     ______  | |_/ / | | |  \| | |  \/     | |_/ /| | | |  \| | |  \/  ______ ")
    print("    |______| | ___ \ | | | . ` | | __      | ___ \| | | | . ` | | __  |______|")
    print("             | |_/ /_| |_| |\  | |_\ \  _  | |_/ /\ \_/ / |\  | |_\ \         ")
    print("             \____/ \___/\_| \_/\____/ ( ) \____/  \___/\_| \_/\____/         ")
    print("                                       |/                                     ")
    print("                                            ....FUCK YO LIFE!!!               ")
    print("The number was: (", NUMBER, ")... You lose bitch!.")
    