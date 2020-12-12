# Iterative vs Recursive approach

"""
def welcome(str1):
    print("This is", str1)            # Output : This is Nitin
welcome("Nitin")
"""
"""
def welcome(str1):
    welcome(str1)         # welcome(Baar baar Nitin chalega iske andar that is recursion)
    
# Recursion occurs when we call function under declaration of function so once maximum
# recursions are done so it will give error in run console as we did not break the function
    
    print("This is", str1)
welcome("Nitin")
"""

"""
Factorial logic 

n! = n * n-1 * n-2 * n-3..............1
n! = n * (n-1)!

"""

# Iterative Approach where iteration performs in terms of loops

"""
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return(fac)
n = int(input("Enter the number"))
print(factorial_iterative(n))
"""

# Recursion approach
# Recursion occurs when function is called under declaration of function
# Recursion also understands the mathematical logic

"""
def factorial_recursive(n):
    if n == 1:
        return(1)
    else:
        return(n * factorial_recursive(n-1))
n = int(input("Enter the number"))
print(factorial_recursive(n))
"""

"""
Fibonacci logic 

0 1 1 2 3 5 8 13.........

"""

# Iterative approach1 for fibonacci

"""
def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return(a)
    elif n == 1:
        return(b)
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return(b)
n = int(input("Enter the number"))
print(fibonacci(n))
"""

# Iterative approach2 for fibonacci        (Job interview logic)

"""
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return(a)
n = int(input("Enter the number"))
print(fibonacci(n))
"""

# Recursive approach for fibonacci

"""
def fibonacci(n):
    if n == 0:
        return(0)
    elif n == 1:
        return(1)
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter the number"))
print(fibonacci(n))
"""











