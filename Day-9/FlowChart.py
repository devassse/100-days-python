#Flow Chart Application

from art import logo
import os
    
print(logo)

bids = {}
binding_finish = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner}, with a bid of ${highest_bid}")

while not binding_finish:
    name = input("What is your name? ")
    price = int(input("What is you bid? $"))

    bids[name] = price

    should_continue = input("Are there any bidders? type 'yes' or 'no'. ").lower()
    if should_continue == 'no':
        binding_finish = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        binding_finish = False
        os.system('clear')
        print(logo)
