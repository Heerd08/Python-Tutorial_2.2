# 4. Student Score Analyzer

# Problem:
# You are given a list of tuples where each tuple contains a student name (string) and a list of marks (integers). Create a dictionary that stores each student’s name as the key and their average marks (int) as the value.

# Input:
# [("Amit", [70, 80, 90]), ("Neha", [85, 90, 95])]

# Output:
# {"Amit": 80, "Neha": 90}



students = [("Amit", [70, 80, 90]), ("Neha", [85, 90, 95])]
average_marks = {}

for name, marks in students:
    avg = sum(marks) // len(marks)
    average_marks[name] = avg

print(average_marks)
