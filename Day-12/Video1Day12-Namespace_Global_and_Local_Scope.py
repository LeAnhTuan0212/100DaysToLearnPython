# This is global scope
enemies = 1 

def increase_enemies():
    # This is local scope
    enemies = 2
    print(f"enermies inside function: {enemies}")
    
increase_enemies()
print(f"enermies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# Doesn't have any potion_strength varible
# print(potion_strength) 

