def decideNumber():
    number = int(input("Enter a number: "))
    return number

def reverseNumber(number):
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10
    return reversed_number

def displayReversedNumber():
    number = decideNumber()
    reversed_number = reverseNumber(number)
    print("The reversed number is:", reversed_number)

def main():
    displayReversedNumber()

if __name__ == "__main__":
    main()
