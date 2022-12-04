student_heights = input("Input a list of student heights ").split()

# 120 140 170 160 110 70

# print(student_heights)
# ['120', '140', '170', '160', '110', '70']
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

total_height = 0
for height in student_heights:
    total_height += int(height)
# print(total_height)

total_students = 0

for student in student_heights:
    total_students += 1
# print(total_students)

average_height = round(total_height / total_students)
print(average_height)
