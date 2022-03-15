from math import sqrt
def prime_checker(number):
    check = True
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            check = False 
            break
    if check:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
prime_checker(6)