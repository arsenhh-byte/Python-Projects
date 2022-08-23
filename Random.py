def format_name(f_name, l_name):
    f_name.title()
    return f_name.title()
print(format_name("Arsen" ,  "arsen"))


# Local Scope
def drink_potion():
    potion_strenght = 21
    print(potion_strenght)

drink_potion()


# Global Scope
player_health = 10

def fortnite():
    player_strength = 2
    print(player_health)
fortnite()

#  Pyhthon does not have a block scope. We can call (if..else and other blocks that have : and have the output outside the block scope)
# But for functions, the concept of block scope applies as shown above
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# Modifying a Global scope

enemies_global_scope = 10

def increment_enemy():
    # Use the global environmental variable
    global enemies_global_scope
    enemies_global_scope += 1
    print (enemies_global_scope)

increment_enemy()