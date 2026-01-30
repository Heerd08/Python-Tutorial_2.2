# 12. Unique Values Extractor
# Problem:
# Given a dictionary where keys are strings and values are lists of integers, return a sorted list of all unique integers across all lists.
# Input:
# {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
# Output:
# [1, 2, 3, 4, 5]

data = {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
unique_values = []

for values in data.values():
    for num in values:
        if num not in unique_values:
            unique_values.append(num)

unique_values.sort()
print(unique_values)
