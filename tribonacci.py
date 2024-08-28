def tribonacci(n):

    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    dp = [0, 1, 1]

    for i in range(3, n+1):
        dp.append(dp[-1] + dp[-2] + dp[-3])
    
    return dp[-1]

for i in range(10):
    print(tribonacci(i), end=",")