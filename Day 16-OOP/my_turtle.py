from turtle import Turtle, Screen

# Declaring an object that has been imported from a class
timmy = Turtle()
print(timmy)

# Using methods
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

# Printing or accessing the attributes of the screen using (object.canvheight) attribute
my_screen = Screen()
print(my_screen.canvheight)
#  Tapping into the method associated with an object in the my_sceen object
my_screen.exitonclick() 