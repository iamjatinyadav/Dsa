# find the GCD of two numbers

# Using Iterations
"""
def gcdofnum(a,b):
    if a<b:
        small = a
    else:
        small = b

    for i in range(1,small+1//2):
        if a%i == 0 and b%i == 0 :
            gcd = i
    return gcd

print(gcdofnum(48,60))
"""

#using recursion

def gcd(a,b):
    assert int(a)==a and int(b) == b ,'the number must be integer only'
    if a < 0:
        a = -1*a
    if b < 0:
        b = -1*b
    if b== 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(8,-12))

