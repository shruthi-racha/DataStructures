def reverse(array, start, end):
    temp = 0
    if (start >= end):
        return
    temp = array[start]
    array[start] = array[end]
    array[end] = temp
    reverse(array, start+1, end-1)

if __name__ == '__main__':
    array = [1,2,3,4,5,6]
    print array
    reverse(array, 0, len(array)-1)
    print array