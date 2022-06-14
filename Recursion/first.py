#normal function

def firstMethod():
    secondMethod()
    print("I am in First Method")
def secondMethod():
    thirdMethod()
    print("I am in second Method")
def thirdMethod():
    forthMethod()
    print("I am in third Method")
def forthMethod():
    print("I am in forth method")


#recursive method
def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

recursiveMethod(10)