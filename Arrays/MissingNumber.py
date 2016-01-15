def findMissingNumber(array):
    temp1 = 0
    for element in array:
        temp1 = temp1^element
    temp2 = 0
    for item in range(1,len(array)+2):
        temp2 = temp2^item
    return temp1^temp2

if __name__ == '__main__':
    array = [1,2,4,5,6]
    print findMissingNumber(array)