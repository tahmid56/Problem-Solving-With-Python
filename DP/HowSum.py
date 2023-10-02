
def howSum(targetSum, numbers, memo={}):
    if(targetSum in memo):
        return memo[targetSum]
    if(targetSum == 0):
        return []
    if(targetSum < 0):
        return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if(remainderResult != None):
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(howSum(300, [7, 2, 14]))