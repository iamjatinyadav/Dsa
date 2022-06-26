# using iteration
# using for loop
"""
def powerofnum(n,p):
    for i in range(1,p):
        n=n*2
    return n

print(powerofnum(2,2))
"""
#using while loop
"""
def powerofnum(n,p):
    q=1
    while(q<p):
        n=n*2
        q+=1
    return n
print(powerofnum(2,4))
"""

#using Recursion


def powerofnum(x,n):
    assert n >=0 and int(n) == n,'value must bhe positive integer'
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        return x * powerofnum(x,n-1)

print(powerofnum(2,4))
