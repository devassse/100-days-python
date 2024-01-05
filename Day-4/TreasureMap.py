#Rock, Paper or Scissors

import random

rock = '''
        .-.____
   ----/ \ )___)
      (  (/()___)
           ()__)
   ----\___()_)
'''
paper = '''
        .-.__
   ----/ \ )_)___
      (  (/()____)
           ()___)
   ----\___()_)
'''
scissors = '''
        .-.__
   ----/ \ )_)___
      (  (/()____)
           ()____)
   ----\___()_)
'''

player_choice = int(input("What do you choose? Type 0 - Rock, 1 - Paper or 2 - Scissors\n"))
computer_choice = random.randint(0, 2)

if player_choice < 0 or player_choice > 3:
    print("Wrong Choice")
    exit()

#Print Player Choice Avatar
print(f"Player Choose: {player_choice}")
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)

#Print Computer Choice Avatar
print(f"Computer Choose: {computer_choice}")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
    
#Validate Result

if player_choice > computer_choice:
    print("--------- Player Win ---------")
elif computer_choice > player_choice:
    print("--------- Computer Win ---------")
elif player_choice == computer_choice:
    print("--------- Hey, There are Draw! ---------")


