# ask user to enter the no.
# seperate odd and even nos. in seperate list till input no
def decideNumber():
    n = int(input("Enter a number: "))
    return n

def separateOddEven(n):
    odd = []
    even = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even

def displayOddEven():
    n = decideNumber()
    odd, even = separateOddEven(n)
    print("Odd numbers:", odd)
    print("Even numbers:", even)

def main():
    displayOddEven()

if __name__ == "__main__":
    main()
