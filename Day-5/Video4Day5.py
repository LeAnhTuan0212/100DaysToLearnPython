student_scores = input("Input a list of student score: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

smallest_score = student_scores[0]
highest_score = student_scores[0]
for score in student_scores:
    if smallest_score > score:
        smallest_score = score
    if highest_score < score:
        highest_score = score

print(f"The smallest score in the class is: {smallest_score}")
print(f"The highest score in the class is: {highest_score}")
