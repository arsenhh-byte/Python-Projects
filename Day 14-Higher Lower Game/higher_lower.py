from higher_lower_art import logo, vs
import random
from game_data import data
import os
# Format the account data into a printable string
""""""
def format_account(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, {account_country}"


# Use an if stmt to check if user is correct
"""Take the user guess and follower counts and returns if they got the guess right or wrong"""
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
        # The opposite is true👇🏾
    else :
        return guess == "b"

def game():
    # Display Art
    print(logo)
    score = 0
    account_b = random.choice(data)
    game_should_continue = True

    # Making the code repeateable using a while loop
    while game_should_continue:

        # Generate random accounts from game data
        # Making the accounts at Position b become A
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        # Printing just incase
        print(f"Compare A : {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")


        # Ask user for a guess 
        guess = input("Who has more followers 'A' or 'B' ? \n").lower()

        #  Check if user is correct
        # Get follower count of each account
        account_a_followers = account_a["follower_count"]
        account_b_followers = account_b["follower_count"]
        is_correct = check_answer(guess, account_a_followers, account_b_followers)

        # Clear the screen to make the game more readable
        os.system('clear')
        print(logo)
        # Feedback about the game
        """Use an if statement to check if is_correct is true"""
        if is_correct == True:
            # Score keeping
            score += 1
            print(f"😁.You're Right! Current score is: {score}" )
        else:
            # Where the game should not continue
            game_should_continue = False
            print(f"😑. Sorry that's wrong. Final score is: {score}")
           

game()