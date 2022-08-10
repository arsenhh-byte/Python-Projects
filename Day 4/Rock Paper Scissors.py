import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

visiuals = [rock, paper, scissors]

user_choice = int(input('Type 0 for "Rock", 1 for "Paper", 2 for "Scissors" \n '))
if user_choice >=3 or user_choice < 0:
    print ("Invalid choice. You loose!")
else:
    print(f" You picked {visiuals[user_choice]}")

    computer_choice = random.randint(0,2)
    print(f" The Computer picked {visiuals[computer_choice]}")

    if user_choice == computer_choice:
        print ("It's a draw.")
    elif user_choice == 2 and computer_choice == 1:
        print ("You win!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif computer_choice == 1 and user_choice == 0:
        print("You loose!")
    elif computer_choice == 0 and user_choice == 2:
        print("You loose!")
    elif computer_choice == 2 and user_choice ==1:
        print("You loose!")
