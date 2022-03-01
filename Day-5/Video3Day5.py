from numpy import number


student_heights = input("Input a list of student heights in cm: ").split()
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# total_height = 0
# number_of_students = 0
# for height in student_heights:
#     total_height += n
#     number_of_students += 1
# print(total_height)
# print(number_of_students)

total_height = sum(student_heights)
number_of_students = len(student_heights)

average_height = round(total_height / number_of_students)
print(average_height)