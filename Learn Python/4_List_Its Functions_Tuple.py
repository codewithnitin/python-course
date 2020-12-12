mylist = ["Harpic", "Vim bar", "Deodarant", "Lady finger", "Lollypop", 56, 105.20]

"""
print(len(mylist))                    #It shows length of the list items where counting starts from 1 and so on.
print(mylist[0:5:2])
print(mylist[-1:-7:-1])
mylist.append("Pulses")                     #append() adds up the item at the last in list.
mylist.extend(["Sugar", "Salt", 200, 50.9]) #extend() adds up more than one items at last in the list.
numbers = [3,5,11,19,55,27,15,55]
numbers.sort()                              #sort() changes the original list in increasing order.
numbers.reverse()                           #reverse() reverses the list.
numbers.insert(3,14)                        #insert() adds up the item at specified indexing.
numbers.pop()                               #pop() removes the last item in the list.
numbers.clear()                             #clear() clears up the list [].
mylist.insert(2,58)
mylist.remove("Lady finger")                #remove() removes the particular item from the list.
mylist.insert(4,"Marinda")
numbers.append(77)                           # List can give the same value 77 if we type append(77) again.
numbers.append(77)
print(numbers)
print(mylist)

numbers.copy()
n1 = numbers.copy()
n1.append("Dates")
print(n1)


print(numbers.count(55))
print(max(numbers))
print(min(numbers))
print(numbers)

numbers[3] = 17
print(numbers)

"""

"""
Mutable : Can change -> List
Imutuable : Cannot change -> Tuple

"""
# tp = (1,5,8,5)
#tp[2] = 10 #tuple index value cannot be changed like List that makes it unique.
#tp = (1)
"""
It doesn't shows parentheses () which is a sign of tuple like list sign [] in output so we will add 
comma , after one element in tuple that is for only one element tuple.

Swapping of two numbers

Traditional way

a = 1
b = 10
temp = a
a = b
b = temp
print(a,b)

"""

"""
Swapping of two numbers via Python


a = 1
b = 12
a,b = b,a
print(a,b)

"""



