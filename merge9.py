# 9. Merge Marks from Two Tests

# Problem:
# You are given two dictionaries representing marks of students in two tests. Merge them into a single dictionary where the value is a tuple of marks from both tests.

# Input:
# {"Amit": 70, "Neha": 85}
# {"Amit": 80, "Neha": 90}

# Output:
# {"Amit": (70, 80), "Neha": (85, 90)}

test1 = {"Amit": 70, "Neha": 85}
test2 = {"Amit": 80, "Neha": 90}

merged = {}

for name in test1:
    merged[name] = (test1[name], test2[name])

print(merged)
