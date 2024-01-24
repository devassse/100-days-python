#Higher vs Lower game
from arts import logo, vs
from data import data
import random
import os

print(logo)
score = 0
game_over = True

account_b = random.choice(data)

def format_account(account):
    """ Formats Accounts data into Printable info """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name} is a {account_desc} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """ Compare The Followers and Return TRUE or FALSE """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

while game_over:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    #Print Question
    print("Who as More Instagram Followers?\n")
    print(f"A - {format_account(account_a)}.")

    #Print VS
    print(vs)

    print(f"B - {format_account(account_b)}.")

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    #Collect the answer from user
    print()
    guess = input("Insert 'A' ou 'B' to Guess: ").lower()



    #Checking the Answer
    is_correct = check_answer(guess, a_followers_count, b_followers_count)


    os.system("clear")
    print(logo)

    if is_correct:
        score += 1
        print(f"You are Write, current Score {score}")
    else:
        print(f"Sorry, You are Wrong, the final score is {score}")
        game_over = False