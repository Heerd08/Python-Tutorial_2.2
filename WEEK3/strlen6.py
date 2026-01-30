# 6. String Length Map
# Problem:
# Given a list of strings, return a dictionary with each string and its length.
# Input:
# ["python", "ml", "ai"]
# Output:
# {"python": 6, "ml": 2, "ai": 2}

words = ["python", "ml", "ai"]
length_dict = {}

for word in words:
    length_dict[word] = len(word)

print(length_dict)
