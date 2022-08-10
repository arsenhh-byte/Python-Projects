import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


list_items = len(names)
random_choice = random.randint(0, list_items -1)
person_who_will_pay = names[random_choice]

# or you can use random.choice
# choice = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today")

