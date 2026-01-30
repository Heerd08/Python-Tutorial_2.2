#1.Given a list of integers, return a dictionary with each number and its count.
# Input:  
# [1, 2, 2, 3, 3, 3]
# Output:
# {1: 1, 2: 2, 3:2}


numbers = [1, 2, 2, 3, 3, 3]
count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(count_dict)