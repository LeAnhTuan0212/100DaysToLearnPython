enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enermies inside function: {enemies}")
    
increase_enemies()
print(f"enermies outside function: {enemies}")