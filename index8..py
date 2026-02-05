# 8. Character Index Mapping

# Problem:
# Given a string, create a dictionary where each character is a key and the value is a tuple of indices at which the character appears.

# Input:
# "banana"

# Output:
# {"b": (0,), "a": (1, 3, 5), "n": (2, 4)}



text = "banana"
index_map = {}

for i in range(len(text)):
    ch = text[i]
    if ch in index_map:
        index_map[ch].append(i)
    else:
        index_map[ch] = [i]

# convert lists to tuples
for ch in index_map:
    index_map[ch] = tuple(index_map[ch])

print(index_map)
