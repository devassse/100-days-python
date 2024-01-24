#Blackjack Game
"""Black jack is a a Game played using cards and must not pass over 21"""

from art import logo
import random
import os

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    def dealer_card():
        card = random.choice(cards)
        return card

    def calculate_scores(cards):
        """Take a list of Cards and Calculate Score"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        
        if 11 in cards and sum(cards) == 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw :-)"
        elif computer_score == 0:
            return "Lose, Oponent has a Blackjac :-("
        elif user_score == 0:
            return "Win with a Blackjack"
        elif user_score > 21:
            return "You went over, you lose"
        elif computer_score > 21:
            return "Opponent went over, you win!"
        elif user_score > computer_score:
            return "You Won"
        else:
            return "You lose"


    for _ in range(2):
        user_cards.append(dealer_card)
        computer_cards.append(dealer_card)

    while not is_game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)

        print(f"Your Cards are {user_cards} and you get scored {user_score}")
        print(f"Computers first Card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another Card, Type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(dealer_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealer_card())
        computer_score = calculate_scores(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computurs final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wnat to play the Game of BlackJack? type 'y' or 'n': ") == 'y':
    play_game()
    os.system("clear")