import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = nameAsCSV.split(", ")

print(names)

#Get the total number of items in list
num_items = len(names)
# Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items - 1)
# print(random_choice)
# person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)
print(person_who_will_pay)