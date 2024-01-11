# Habg Man Project

import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

print(logo)
print("Welcome to my Game - Guess Each letter of the Word and save the man!\n")
guess = input("Guess the Letter: ")

while guess.isnumeric():
    print("Please, insert only LETTERS")
    guess = input("Guess the Letter: ")

print(f"You chosed Letter '{guess}', now Let's Verify ...")
