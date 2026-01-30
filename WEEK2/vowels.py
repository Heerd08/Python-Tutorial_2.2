# ask user to enter word without space 
# separate letterrs in vowels and consonant list
def separateVowelsConsonants(word):
    vowels = []
    consonants = []

    for ch in word.lower():
        if ch in "aeiou":
            vowels.append(ch)
        else:
            consonants.append(ch)

    return vowels, consonants


def main():
    word = input("Enter a word (without space): ")
    vowels, consonants = separateVowelsConsonants(word)
    print("Vowels:", vowels)
    print("Consonants:", consonants)


if __name__ == "__main__":
    main()
