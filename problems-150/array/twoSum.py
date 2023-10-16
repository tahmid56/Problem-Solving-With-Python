def twoSum(nums, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if (diff in prevMap):
            return [prevMap[diff], i]
        prevMap[n] = i
    return



print(twoSum([2,3,4,5,1], 7))