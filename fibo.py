import numpy as np
import time

def fibo(n):
    res = np.array([[1, 0], [0, 1]])
    matrix = np.array([[1, 1], [1, 0]])

    while n > 0:
        if n % 2 == 1:
            res = res.dot(matrix)
        
        matrix = matrix.dot(matrix)
        n = n // 2
    
    return res[0][1]

def fibo2(n):
    if n <= 1:
        return n
    return fibo2(n - 1) + fibo2(n - 2)

def fibo3(n):
    if n <= 1:
        return n
    
    df = [0 for i in range(n + 1)]
    df[0] = 0
    df[1] = 1

    for i in range(2, n + 1):
        df[i] = df[i - 1] + df[i - 2]
    
    return df[n]

start = time.time()
for i in range(0, 40):
    print(fibo(i), end=' ')
end = time.time()
print(end - start)

start = time.time()
for i in range(0, 40):
    print(fibo3(i), end=' ')
end = time.time()
print(end - start)