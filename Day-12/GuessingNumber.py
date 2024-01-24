#Guess a Number Game
from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def guess_game():
    # Printing Logo and Welcome message
    print(logo)
    print("Welcome to GUESSING NUMBER game")


    #Checking Answer
    def check_answer(guess, answer, turns):
        """ Checks Answers Aganst Guess and Answers """
        if guess > answer:
            if (guess - 5) > answer:
                print("Guess is Too Higher")
            else:
                print("Guess is Higher")
            return turns - 1
        elif guess < answer:
            if (guess + 5) < answer:
                print("Guess is Too Lower")
            else:
                print("Guess is Lower")
            return turns - 1
        else:
            print(f"You got it, Your Guess was {guess} and the Answer is {answer}")

    #Set Dificulty
    def set_dificulty():
        level = input("Chosse a Dificulty, 'easy' or 'hard': ").lower()
        # if level != "easy" or level != "hard":
        #     print(f"Wrong Answer {level}")
        #     level = input("Chosse a Dificulty, 'easy' or 'hard'").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS


    #Guess the Number
    answer = randint(1,100)

    print(answer)

    turns = set_dificulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the Number")
        guess = int(input("I am thinkink on a Number Between 1 and 100, witch one?: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of Guesses, You Loose")
            return
        elif guess != answer:
            print("Guess Again ..")

guess_game()