# 6. Word Length Grouping

# Problem:
# Given a list of words (strings), create a dictionary where the key is the word length (int) and the value is a list of words having that length.

# Input:
# ["cat", "dog", "elephant", "bat"]

# Output:
# {3: ["cat", "dog", "bat"], 8: ["elephant"]}


words = ["cat", "dog", "elephant", "bat"]
length_dict = {}

for word in words:
    length = len(word)
    if length in length_dict:
        length_dict[length].append(word)
    else:
        length_dict[length] = [word]

print(length_dict)
