def longestPrefix(words):
    # Start with the first word as prefix
    prefix = words[0]

    # Compare prefix with each word in the list
    for word in words:
        # Keep removing last character until prefix matches the start of word
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # remove last character
            if prefix == "":
                return ""  # no common prefix

    return prefix


def main():
    words = ['flower', 'flow', 'flight']
    result = longestPrefix(words)
    print("Longest prefix:", result)


if __name__ == "__main__":
    main()
