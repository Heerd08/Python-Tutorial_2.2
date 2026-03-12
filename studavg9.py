# 9. Student Average Score
# Problem:
# You are given a list of tuples where each tuple contains a student name and a list of marks. Return a dictionary mapping each student’s name (lowercase) to their average score.
# Input:
# [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
# Output:
# {"alice": 85.0, "bob": 81.67}

students = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
result = {}

for student in students:
    name = student[0].lower()
    marks = student[1]

    total = 0
    for mark in marks:
        total = total + mark

    average = total / len(marks)
    result[name] = round(average, 2)

print(result)
