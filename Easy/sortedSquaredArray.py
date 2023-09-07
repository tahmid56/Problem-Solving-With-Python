arr = [-7, -5, -4, 3, 6, 8, 9]
# O(n) Time | O(n) Space
def sortedSquaredArray(array):
    start = 0
    end = len(array) - 1
    newArr= [0 for _ in array]
    for idx in reversed(range(len(array))):
        if abs(array[start]) < abs(array[end]):
            newArr[idx] = array[end] * array[end]
            end -= 1
        else:
            newArr[idx] = array[start] * array[start]
            start += 1
    return newArr

print(sortedSquaredArray(arr))
