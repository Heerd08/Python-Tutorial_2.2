# 4. Reverse Words
# Problem:
# Given a string, return a list of words in reverse order.
# Input:
# "data science is fun"
# Output:
# ["fun", "is", "science", "data"]

text = "data science is fun"
words = text.split()
words.reverse()

print(words)