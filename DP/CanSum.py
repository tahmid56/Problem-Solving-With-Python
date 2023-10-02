def canSum(targetSum, numbers, memo={}):
    if(targetSum in memo):
        return memo[targetSum]
    if(targetSum == 0):
        return True
    if(targetSum < 0):
        return False

    for i in numbers:
        remainder = targetSum - i
        if(canSum(remainder, numbers) == True):
            memo[remainder] = True
            return True
    memo[targetSum] = False 
    return False

print(canSum(300, [2, 4]))