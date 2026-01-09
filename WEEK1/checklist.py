def decideNumber():
    number = int(input("Enter a number: "))
    return number

def numcheck(number):
    return number % 2 == 1  

def checkOddEven(number): 
    # number = decideNumber()   
    
    if numcheck(number):
        print(f"{number} - odd")
    else:
        print(f"{number} - even")
        
def checkOddEvenList():
    upper_limit = int (input("Enter a number :"))
    for number in range(1,upper_limit +1):
        checkOddEven(number)
    
def main():
    checkOddEvenList()

if __name__ == "__main__":
    main()
