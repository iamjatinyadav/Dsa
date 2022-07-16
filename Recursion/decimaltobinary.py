# Using Iteration 
# Using bin function
"""
def dectobin(a):
    return(bin(a)[2:])
        

print(dectobin(34567))
"""

#using recursion

def decimaltobinary(n):
    assert int(n)== n , "the vale must be a integer value"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimaltobinary(int(n/2))

print(decimaltobinary(10))
