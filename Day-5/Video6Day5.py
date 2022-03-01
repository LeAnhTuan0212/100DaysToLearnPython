total = 0

for even_number in range(2, 101, 2):
    total += even_number
print(total)

total2 = 0
for number in range(1, 101):
    if not number % 2:
        total2 += number
print(total2)