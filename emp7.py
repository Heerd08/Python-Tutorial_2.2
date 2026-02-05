# 7. Employee Attendance Summary

# Problem:
# You are given a dictionary where each key is an employee name (string) and the value is a list of attendance records ("P" or "A"). Create a new dictionary storing the total number of present days (int) for each employee.

# Input:
# {"Ravi": ["P", "A", "P"], "Neha": ["P", "P", "P"]}

# Output:
# {"Ravi": 2, "Neha": 3}

attendance = {
    "Ravi": ["P", "A", "P"],
    "Neha": ["P", "P", "P"]
}

present_days = {}

for name, records in attendance.items():
    present_days[name] = records.count("P")

print(present_days)
