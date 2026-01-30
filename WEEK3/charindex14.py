# 14. Character Index Map
# Problem:
# Given a string, return a dictionary mapping each character to a tuple of all its indices.
# Input:
# "banana"
# Output:
# {"b": (0,), "a": (1,3,5), "n": (2,4)}

text = "banana"
index_map = {}

for index in range(len(text)):
    char = text[index]
    if char in index_map:
        index_map[char].append(index)
    else:
        index_map[char] = [index]

# convert lists to tuples
for char in index_map:
    index_map[char] = tuple(index_map[char])

print(index_map)
