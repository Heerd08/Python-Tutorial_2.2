# 5. Sum of Tuples
# Problem:
# Given a list of tuples containing two integers each, return a list of their sums.
# Input:
# [(1, 2), (3, 4), (5, 6)]
# Output:
# [3, 7, 11]

pairs = [(1, 2), (3, 4), (5, 6)]
sums = []

for item in pairs:
    total = item[0] + item[1]
    sums.append(total)

print(sums)
