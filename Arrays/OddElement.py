def oddElement(array):
    temp = 0
    for element in array:
        temp = temp ^ element
    return temp

if __name__ == '__main__':
    arr = [1,1,2,2,2,2,-3,10,10,10,10]
    print oddElement(arr)

#O(n)