#!/usr/bin/python
#Various Matrix Problems implemented
def search_sorted_row_col(matrix, element):
    i = 0
    j = len(matrix[0]) - 1
    while (i < len(matrix[0]) and j >= 0):
        if (matrix_sorted_row_col[i][j] == element):
            return True
        elif (matrix_sorted_row_col[i][j] > element):
            j -= 1
        else:
            i += 1
    return False      

if __name__ == '__main__':
    #Search in a row wise and column wise sorted matrix
    matrix_sorted_row_col = [ [10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    print search_sorted_row_col(matrix_sorted_row_col, 2)