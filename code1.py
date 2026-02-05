# 1. Character Count

# Problem:
# Given a string, create a dictionary that stores each character and its frequency.

# Input:
# "apple"

# Output:
# {"a": 1, "p": 2, "l": 1, "e": 1}


text = "apple"
char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print(char_count)
