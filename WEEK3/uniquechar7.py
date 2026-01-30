# 7. Unique Characters
# Problem:
# Given a string, return a tuple of unique characters in the order they appear.
# Input:
# "programming"
# Output:
# ("p", "r", "o", "g", "a", "m", "i", "n")


text = "programming"
unique_chars = []

for char in text:
    if char not in unique_chars:
        unique_chars.append(char)

print(tuple(unique_chars))
