

print( """       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
""")

print("Welcome to Eye_spy")

print("The year is 1945 and you have been assigned a very crucial mission by The Queen herself. \n  In front of you is a door. ")
print("You have opened the door and it leads into a hallway with two paths")
way = input("Do you choose to go left or right? \n")

choice1 = way.lower()
if choice1 == "left":
    choice2 = input('You have evaded the Nazi soldiers and you have stumbled across a secret door. \n "open door" or "go ahead" ').lower()
    if choice2 == "open door":
        choice3 = input(" There is a control center with 3 buttons \n red, green and blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("You have stopped a missle attack. \n Congratulations you are a HERO!")
        elif choice3 == "blue":
            print("You have initiated a self-distruct sequence. \n GAME OVER!!")
        elif choice3 == "green":
            print("Friendly fire. \n GAME OVER!!")
        else:
            print("Incorrect choice \n GAME OVER!!")
    else:
        print("The Nazi have caught up to you GAME OVER!!!")
else:
  print( "Nazi soldiers are approaching and you have been killed. GAME OVER!!" )