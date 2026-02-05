# 3. Tuple to Dictionary
# Problem:
# Given a tuple of (key, value) pairs, convert it into a dictionary.
# Input:
# (("a", 1), ("b", 2))
# Output:
# {"a": 1, "b": 2}


pairs = (("a", 1), ("b", 2))
result = {}

for item in pairs:
    key = item[0]
    value = item[1]
    result[key] = value

print(result)