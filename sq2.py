# 2. Square Number Dictionary

# Problem:
# Given a list of integers, create a dictionary where the key is the number and the value is its square.

# Input:
# [1, 2, 3, 4]

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16}


numbers = [1, 2, 3, 4]
square_dict = {}

for num in numbers:
    square_dict[num] = num * num

print(square_dict)
