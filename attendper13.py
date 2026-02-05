# 13. Attendance Percentage
# Problem:
# Given a dictionary mapping employee names to a list of attendance strings ("P" or "A"), return a dictionary of employee names and their attendance percentage.
# Input:
# {"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}
# Output:
# {"Ravi": 66.67, "Neha": 100.0}

attendance = {"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}
result = {}

for name, records in attendance.items():
    present = records.count("P")
    total = len(records)
    percentage = (present / total) * 100
    result[name] = round(percentage, 2)

print(result)
