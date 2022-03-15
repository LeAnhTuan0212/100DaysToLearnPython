# There is no Block Scope


game_level = 3

def create_enemies():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemies = enemies[0]


    print(new_enemies)