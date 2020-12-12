a = 7

def printjoke(str):
    return(f"Ye hath humka de de thakur {str}")

def add(x,y):
    return(f"Sum of x and y is {x+y}")

print("The name is", __name__) # Output : The name is __main__

if __name__ == '__main__':
    print(a)
    print(printjoke("Gabar"))
    print(add(4,5))
