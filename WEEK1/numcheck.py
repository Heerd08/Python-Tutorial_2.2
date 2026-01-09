def decideNumber():
    number = int(input("Enter a number: "))
    return number

def numcheck(number):
    return number % 2 == 1  

def main():
    number = decideNumber()
    if numcheck(number):
        print(f"{number} - odd")
    else:
        print(f"{number} - even")
        


if __name__ == "__main__":
    main()
