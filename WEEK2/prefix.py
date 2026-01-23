# find longest prefix 
# inpt=['flower','flow','flight'] 
# result=f1
def decideWords():
    words = ['flower', 'flow', 'flight']
    return words

def findLongestPrefix(words):
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

def displayLongestPrefix():
    words = decideWords()
    prefix = findLongestPrefix(words)
    print("Longest prefix:", prefix)

def main():
    displayLongestPrefix()

if __name__ == "__main__":
    main()
