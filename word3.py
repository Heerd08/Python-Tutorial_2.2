# 3. Word First Letter Mapping

# Problem:
# Given a list of words (strings), create a dictionary where each word is mapped to its first character.

# Input:
# ["cat", "dog", "elephant"]

# Output:
# {"cat": "c", "dog": "d", "elephant": "e"}


words = ["cat", "dog", "elephant"]
result = {}

for word in words:
    result[word] = word[0]

print(result)
