student_heights = input("Input a list of student heightås ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height

number_of_student = 0
for student in student_heights:
  number_of_student += 1

AverageStudentHeight = round(total_height / number_of_student)
print (AverageStudentHeight)


# total_height = sum(student_heights)
# number_of_student = len(student_heights)
# average_height = (total_height / number_of_student)





