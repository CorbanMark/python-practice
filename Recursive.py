def recursive(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*recursive(n-1)
    #This will compute the factorial of n recursively