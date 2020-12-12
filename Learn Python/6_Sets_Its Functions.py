"""
Sets -> It is a collection of well defined objects.
It is denoted by symbol {}

Types :

Empty set        : {}              No element present in the set.
Singleton set    : {7}             There is one element in the set.
Finite set       : {1,2,3,4,5}
Infinite set     : {5,7,11,...}    ... three dots shows so on which is infinite set.
Equal set        : If sets A and B has same elements and order does not matter.
A = {1,2,3,4,5}
B = {4,5,2,1,3}
Disjoint set     : If set A and B have no common element so set A and B are disjoint sets.
A = {1,2,3}
B = {5,6,7}
Subset           : If set A has the elements which are present in set B so set A is a subset of B.
A = {1,2,3}
B = {1,2,3,4,5}
Union            : It is a collection of elements of sets A and B without repetition.
A = {1,2,3}
B = {4,5,6}
AUB = {1,2,3,4,5,6}
A = {1,2,3}
B = {1,4,5,6}
AUB = {1,2,3,4,5,6}
Intersection      : It selects the common element from two or more sets.
A = {1,2,3}
B = {1,2,4,5,6}
Output = {1,2}
Difference        : A-B is a set which will have all the elements of set A and no element of set B.
A = {1,2,4,5,6}
B = {1,2,3}
Output = {4,5,6}
"""

s = set()
#print(type(s))
s_from_list = set([1,2,3,4])
# print(s_from_list)
# print(type(s_from_list))
s.add(1)                        # Adding element to the set.
s.add(1)                        # Output will come up with no change as set returns only unique value( No same)
#People think there must be two 1 like {1,1} as we have append () in list which gives same value again [1,1]
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.remove(5)
s2 = set([3,4,5,6])
# print(s,s2)
s3 = s.copy()
s3.remove(2)
# print(s,s2,s3)
s4 = set([6,7,8,9])
s5 = {1,2,3}
# print(s5)
# print(type(s5))
# print(s.isdisjoint(s4))
# print(s.union(s2))
# print(s.union(s4))
# print(s.intersection(s2))
# print(s5.issubset(s))
# print(s.difference(s2))
# print(len(s2))
# print(max(s4))
# print(min(s))







