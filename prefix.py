# find longest prefix 
# inpt=['flower','flow','flight'] 
# result=f1
def longestPrefix(words):
    prefix = ""

    for i in range(len(words[0])):
        ch = words[0][i]

        for word in words:
            if i >= len(word) or word[i] != ch:
                return prefix

        prefix = prefix + ch

    return prefix


def main():
    words = ['flower', 'flow', 'flight']
    result = longestPrefix(words)
    print("Longest prefix:", result)


if __name__ == "__main__":
    main()
