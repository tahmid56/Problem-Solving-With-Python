def spiral(arr):
    startCol = 0
    startRow = 0
    endCol = len(arr[0]) - 1
    endRow = len(arr) - 1
    while(startCol<=endCol and startRow<=endRow):
        for i in range(startCol ,endCol+1):
            print(arr[startRow][i], end=" ")
        for i in range(startRow+1, endRow+1):
            print(arr[i][endCol],end=" ")
        for i in range(endRow-1, startRow-1, -1):
            print(arr[endCol][i], end=" ")
        for i in range(endCol-1, startCol, -1):
            print(arr[i][startRow], end=" ")
        startCol += 1
        startRow += 1
        endCol -= 1
        endRow -= 1

arr =   [[ 1, 2, 3, 4], 
         [ 5, 6, 7, 8], 
         [ 9, 10, 11, 12], 
         [ 13, 14, 15, 16]]
spiral(arr)