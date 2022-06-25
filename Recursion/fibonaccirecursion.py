#using iterator
"""
def fibo(n):
    a=0
    b=1
    if n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    elif n>=3:
        print(a)
        print(b)
        for x in range(2,n+1):
            c=a+b
            print(c)
            a=b
            b=c
        
fibo(10)       
"""

#using recursion
def fibonacci(n):
    assert n >=0 and int(n) == n, 'input must be a positive integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


print(fibonacci(7))