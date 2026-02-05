# 10. Frequency-Based Word Filter

# Problem:
# Given a list of words (strings), create a dictionary storing word frequencies and return only those words whose frequency is greater than 1.

# Input:
# ["python", "java", "python", "c", "java"]

# Output:
# {"python": 2, "java": 2}

words = ["python", "java", "python", "c", "java"]
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

result = {}
for word, count in freq.items():
    if count > 1:
        result[word] = count

print(result)
