#for list =[3,2,6,4,8,5] 
#generate cumilative addition result in 
#result=[3,5,11,15,23,28]
def decideList():
    lst = [3, 2, 6, 4, 8, 5]
    return lst

def cumulativeSum(lst):
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

def displayCumulativeSum():
    lst = decideList()
    result = cumulativeSum(lst)
    print("Result:", result)

def main():
    displayCumulativeSum()

if __name__ == "__main__":
    main()
