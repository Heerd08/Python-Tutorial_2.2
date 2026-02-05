# 2. Dictionary Key Check
# Problem:
# Given a dictionary and a key, return "Found" if the key exists, otherwise return "Not Found".
# Input:
# {"a": 1, "b": 2}, key = "b"
# Output:
# "Found"


data = {"a": 1, "b": 2}
key = "b"

if key in data:
    print("Found")
else:
    print("Not Found")