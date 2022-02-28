import random 

# random.seed(123)
# randomInteger = random.randint(1, 10)
# print(randomInteger)

# randomFloat = random.random()
# print(randomFloat)

test_seed = int(input("create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side:
    print("Heads")
else:
    print("Tails")
    
