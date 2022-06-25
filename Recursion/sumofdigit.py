# using iterations
# using int() and str() methods
"""
def sumofdigit(n):
    assert n >=0 and int(n) == n,'value must bhe positive integer'
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

print(sumofdigit(234))
"""
# using gernal approch
"""
def sumofdigit(n):

    sum = 0

    while(n != 0 ):
        sum = sum + n%10
        n = n//10
    return sum

print(sumofdigit(24))

"""
#using recusion

def sumofdigit(n):
    assert n >=0 and int(n) == n,'value must bhe positive integer'
    if n == 0:
        return 0
    else:
        return int(n%10) +sumofdigit(int(n//10))

print(sumofdigit(11))
