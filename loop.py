def factorialLoop(n):
    result = 1
    for i in range(2, n+1):
        result *= i #This multiplies the i with result from number 2 up to n
        return result
    