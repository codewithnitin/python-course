"""
Iterable :  These are those python object which define __iter__() or __getitem__() method and if these
methods are applied on these objects so they give iterator.

Iterator : These are those objects which define __next__() means if we apply this method on iterator
so it returns the elements of Iterable which could be anything like string, list, dictionary etc.

(Iterator par  __next__() run hoga toh phela element milega iterable ka phr iterator per __next__()
dobara run hoga toh next element milega Iterable ka and so on.

Iteration : An approach to iterate an object is known as Iteration.



Now we will study about Generator :

Generator : These are those functions which yield the sequence of value ( Matlab iterate krane
 ke kabil bnana pr actual me generate ya iterate nahi karna value ko when we will need of it
 so we will use it that time ) and these are those Iterators which traverse once.

Generator : These are those functions which use yield keyword to generate on the fly
values and it traverse once ( Sone ka anda dene wali murgi jiska use tb kr skte hai
jb iski jarurat ho )

( Ye kya keh diya maine jaisa ki hum jaante hai sbhi iterator ek ek karke he traverse hote hue
 element ko return krte hai iterable ke par sbhi iterator rukte nahi woh loop me chalte hai
 jab tak iterbale ke elements khatam nhi ho jaate per hum generator bana le toh uss iterable ko
 iterate karne ke kabil ho jaate hai ese ki ek element iterbale ka access hua toh loop ruka hai
 phr iterate kre toh dusra element access hoga and so on.)

 What is the use of it?

 Suppose we have one number 50000000000000000000000 or might be thousand times of this number
 and if we iterate it like

 for i in range(50000000000000000000000):
    print(i)

Here, iteration will be performing that is for sure but we do not want to slow down our system
by storing such a big sequence of values to iterate this number so we build generator by which
we can be capable to iterate such a big number if we want to ( Matalab jarurat hogi to iterate
karenge isse number ko par abhi nhi kr rhe )

Now we will see generator in code :

"""
#
# h = "harry"
# def disp():
#     for i in h:
#         print(i)
# disp()

"""
Output :
h
a
r
r
y

here, iteration was performing in loop and print() was printing the values after each iteration.

"""


# h = "harry"
# def disp():
#     for i in h:
#         return(i)
# print(disp())


"""
Output : 

h 

This is because iteration was done and returned the value h after that loop cannot be run (Kyunki
return ho jaane ke baad kuch bhi ho woh nhi chalta yaha loop nhi chalega and print(disp()) print
karega h only.



"""


# h = "harry"
# def disp():
#     for i in h:
#         yield(i)
# g = disp()
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
#
# for i in g:
#     print(i)


"""
As we used the statement yield instead of print or return due to which disp() identity has been
changed to object from function so here g = disp() is a generator object in spite of function.

We know generators are those iterators which traverse once now I will prove it.

Iterators have __next__() when we apply this method on iterators so it gives element of iterable

(Kyunki generator hai toh loop ese nhi chalega ki iterbale ke saare elements print hote chale 
jayenge hum iterate kr payenge elements ko par ek element ko access krenge phr loop ruka rhega 
jabtak hum dusra element iterate na kare iterbale ka let us see how )

Once we print print(g.__next__()) so output would be h and if we print print(g.__next__()) again
so output would be a and so on.

Output :
h
a
r
r
y 

if we iterate print(g.__next__()) five times for iterable "Harry" but if we print one more
print print(g.__next__()) so will get an error Stop iteration ( Kyunki bhai aap harry ke baad
kya iterate kroge aapke iterbale ke element khatam)

Now question is if we use for loop like :

for i in g:
    print(i)
    
so output :

h
a
r
r
y 

Ab stop iteration kyu nhi aaya error generator object ko iterate karnge woh isliye nhi aaya
because it is a convention of for loop which handle it all so once the items or elements 
of iterable is finished so it automatically comes out without giving stop iteration error.

"""


"""


We learn the two statement in detail iterable and iterator with the help of below example.

h = "harry"
def __iter__():
    return(h)
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

Note : h.iter() or iter(h) both are same but the only difference is h.iter() will work in class
and iter(h) can be used anywhere in calling function or method.

h = 54321
ier = iter(h)
print(ier.__next__())

Output : int object is not iterable 

(Integer iterable nahi hai woh toh range() ki help se we can access sequence of numbers or values)


"""

"""

# Factorial program using generator :

def fact(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
        yield(fac)

n = int(input("Enter the number for factorial \n"))
g = fact(n)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

            # OR
            
for i in g:
    print(i)
    
    
"""


"""


# Fibonacci series ( 0,1,1,2,3,5,8,13,21.....) program using generator :

def fib(n):
    a,b = 0,1
    if n == 0:
        yield(a)
    elif n == 1:
        yield(b)
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
            yield(b)

n = int(input("Enter the place number for which you wish to get an output of Fibonacci series \n"))
g = fib(n)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

for i in g:
    print(i)


"""




