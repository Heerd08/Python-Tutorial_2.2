# 15. Dictionary Value Merger
# Problem:
# Given a list of dictionaries with integer values, merge them into a single dictionary by summing values of common keys.
# Input:
# [{"a": 2, "b": 3}, {"a": 4, "c": 1}]
# Output:
# {"a": 6, "b": 3, "c": 1}

dicts = [{"a": 2, "b": 3}, {"a": 4, "c": 1}]
result = {}

for d in dicts:
    for key, value in d.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

print(result)
