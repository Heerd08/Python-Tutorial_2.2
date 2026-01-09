def decideNumber():
    number = int(input("Enter a number: "))
    return number

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def displayFactorial():
    number = decideNumber()
    fact = factorial(number)
    print(f"Factorial of {number} is {fact}")

def main():
    displayFactorial()

if __name__ == "__main__":
    main()
