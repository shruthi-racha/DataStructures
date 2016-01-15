def separateZerosAndOnes(array):
    low = 0
    high = len(array)-1
    while(low < high):
        while(array[low] == 0 and low<high):
            low += 1
        while(array[high] == 1 and low<high):
            high -= 1
        if(low < high):
            array[low] = 0
            array[high] = 1
            low += 1
            high -= 1
    return array
            
if __name__ == '__main__':
    array = [0,1,0,1,1,0,0]
    array_after = separateZerosAndOnes(array)
    print array_after