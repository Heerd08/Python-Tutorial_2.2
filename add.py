#for list =[3,2,6,4,8,5] 
#generate cumilative addition result in 
#result=[3,5,11,15,23,28]
def cumulativeSum(lst):
    result = []
    total = 0

    for num in lst:
        total = total + num
        result.append(total)

    return result


def main():
    lst = [3, 2, 6, 4, 8, 5]
    result = cumulativeSum(lst)
    print("Result:", result)


if __name__ == "__main__":
    main()
