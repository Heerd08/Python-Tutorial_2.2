def decideNumber():
    number = int(input("Enter a number: "))
    return number

def countDigits(number):
    count = 0
    if number == 0:
        return 1
    while number > 0:
        count += 1
        number //= 10
    return count

def displayDigitCount():
    number = decideNumber()
    digit_count = countDigits(number)
    print(f"Number of digits: {digit_count}")

def main():
    displayDigitCount()

if __name__ == "__main__":
    main()
