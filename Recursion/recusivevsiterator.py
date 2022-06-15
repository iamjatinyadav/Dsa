#Recusive Function

def powerOfTwo(n):
    if n ==0:
        return 1
    else:
        power=powerOfTwo(n-1)
        return power*2

value = powerOfTwo(10)
print(value)

#iterative Function

def powerOFTwoIt(n):
    i=0
    power = 1
    while i<n:
        power = power*2
        i=i+1
    return power

val1 = powerOFTwoIt(10)
print(val1)

