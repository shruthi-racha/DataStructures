def pairWithSum(arr, sum_value):
    sorted_array = sorted(arr)
    print sorted_array
    
    low = 0
    high = len(sorted_array)-1
    
    while(low <= high):
        if ((sorted_array[low] + sorted_array[high]) == sum_value):
            return ("Found", sorted_array[low],sorted_array[high])
        elif ((sorted_array[low] + sorted_array[high]) < sum_value):
            low += 1
        else:
            high -= 1
        
if __name__ == '__main__':

    arr = [1, -3, 6, 5, 10, -100]
    print arr
    print pairWithSum(arr, -80)
    