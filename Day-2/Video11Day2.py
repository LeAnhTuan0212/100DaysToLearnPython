# Bill
print("Welcome to the tip calculator!")

bill = input("What was total bill? $")
bill_as_float= float(bill)

tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
tip_as_int = int(tip)

people = input("How many people split the bill? ")
people_as_int = int(people)

tip_as_percent = tip_as_int/100
total_tip_amount = bill_as_float * tip_as_percent
bill_total = total_tip_amount + bill_as_float
bill_per_person = bill_total / people_as_int
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")