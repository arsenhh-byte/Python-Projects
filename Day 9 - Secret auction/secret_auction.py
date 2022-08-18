import os 
from secret_auction_art import logo
print(logo)

bids = {}

bidding_finished = False

def find_highest_bidders(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid amount of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? \n")
    price = int(input("What is your bid? \n $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' to continue. \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidders(bids)
    elif should_continue == "yes":
        os.system("clear")

