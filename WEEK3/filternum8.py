# 8. Filter Even Numbers
# Problem:
# Given a list of numbers, return a new list containing only even numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [2, 4, 6]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
