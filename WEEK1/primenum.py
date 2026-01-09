def decideNumber():
    number = int(input("Enter the upper limit: "))
    return number

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def printPrimes(n):
    print("Prime numbers are:")
    for number in range(2, n + 1):
        if isPrime(number):
            print(number, end=" ")

def main():
    n = decideNumber()
    printPrimes(n)

if __name__ == "__main__":
    main()
