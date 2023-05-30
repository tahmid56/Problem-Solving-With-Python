arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

# O(n^2) time | O(1) space
# using two loops
# def twoNumberSum(arr, target):
#     for i in range(len(arr) - 1):
#         firstNum = arr[i]
#         for j in range(i+1, len(arr)):
#             secondNum = arr[j]
#             if firstNum + secondNum == target:
#                 return [firstNum, secondNum]
#     return []

#using dict
#O(n) time | O(n) space
# def twoNumberSum(arr, target):
#     nums = {}
#     for num in arr:
#         if target - num in nums:
#             return [target - num, num]
#         else:
#             nums[num] = True
#     return []

#for sorted array
#O(nlogn) time | O(1) space
# def twoNumberSum(arr, target):
#     arr.sort()
#     left = 0
#     right = len(arr) - 1
#     while left< right :
#         currentSum = arr[left] + arr[right]
#         if currentSum == target:
#             return [arr[left], arr[right]]
#         elif currentSum < target:
#             left += 1
#         elif currentSum > target:
#             right -= 1
#     return []



