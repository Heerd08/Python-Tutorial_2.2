# ask user to enter word without space 
# separate letterrs in vowels and consonant list
def decideWord():
    word = input("Enter a word (without space): ")
    return word

def separateVowelsConsonants(word):
    vowels = []
    consonants = []
    for ch in word.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels.append(ch)
            else:
                consonants.append(ch)
    return vowels, consonants

def displayVowelsConsonants():
    word = decideWord()
    vowels, consonants = separateVowelsConsonants(word)
    print("Vowels:", vowels)
    print("Consonants:", consonants)

def main():
    displayVowelsConsonants()

if __name__ == "__main__":
    main()
