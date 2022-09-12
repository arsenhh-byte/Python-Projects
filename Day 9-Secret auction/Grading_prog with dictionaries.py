student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    # You can access the values in a dictionary with a variable that holds the dictionary_name[and the key ] 
    score = student_scores[student]
    if score > 90 :
        student_grades[student] = "Outstanding"
    elif score > 80 :
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)