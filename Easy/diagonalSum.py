def diagonalSum(arr):
    sum = 0
    left = 0
    right = len(arr)-1
    for i in range(len(arr)):
        sum += arr[left][left]
        sum += arr[right][right]
        left+=1
        right-=1
    print(sum)

arr= [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

diagonalSum(arr)
