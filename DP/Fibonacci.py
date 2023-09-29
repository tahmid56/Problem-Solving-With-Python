def fibonacci(n, memo = {}):
    if(n in memo):
        return memo[n]
    if(n <= 2):
        return 1
    memo[n] = fibonacci(n-2) + fibonacci(n-1)
    return memo[n]
print(fibonacci(17))
print(fibonacci(50))