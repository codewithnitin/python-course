import time

from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    """Here, time.sleep(3) could be some work which takes 3 seconds to perform
     like data fetching from web or from any big file"""
    time.sleep(3)
    return(n)


print("Now we will call some_work function")
print(some_work.__doc__)
some_work(4)
print("Done..calling again")
some_work(1)
print("Called argument 1")
some_work(5)
print("Called argument 5")
some_work(7)
print("Called argument 7")
some_work(4)
print("We called argument 4 again")
some_work(5)
print("We called argument 5 quickly again")



"""
 
Function_Caching : Suppose our function performs some task by providing known input and
return known output due to which it takes n seconds to perform and if we call the same
function with same input(argument) to get the same output so it will same delay to perform
the task which we do not want actually so we have one decorator lru_cache of functools
module which creates cache of input and output.

lru_cache(maxsize = n) maxsize means how many last calls of function we want to execute 
in a quickly manner.


Example :

Our function can bring the date like :

1)
Function is fetching some data from web like we opened our chrome browser and typed 
www.youtube.com in url and then searched some of the video content to display so due to
which that content is stored in our disk so if play the same content again so our system
displays the content from the storage of disk that is cache memory in spite of running the
whole process which we did first time to access that content over youtube.com it saves our
time but yes it consumes our space for sure.

2) 
Function is fetching some relevant data from the big file so it may also take some delay
to display the content in first attempt and we know what is the output of the content
if we call the function with same input which we had passed earlier but this time we 
do not want that delay.



"""



"""

In above approach we imported two module time and functools and in functools we imported
decorator lru_cache then applied it over the function some_work like

    @lru_cache(maxsize=3)
    def some_work(n):
        Here, time.sleep(3) could be some work which takes 3 seconds to perform
        like data fetching from web or from any big file
        time.sleep(3)
        return(n)


Here we applied decorator lry_cache on function some_work which has one docstring and
time.sleep(3) to show delay of 3 seconds which could be delay of anything like data
retriving by this function from file or web then return n

After that we came out from the function and printed like

    print("Now we will call some_work function")
    print(some_work.__doc__)
    some_work(4)
    print("Done..calling again")
    some_work(1)
    print("Called argument 1")
    some_work(5)
    print("Called argument 5")
    some_work(7)
    print("Called argument 7")
    some_work(4)
    print("We called argument 4 again")
    some_work(5)
    print("We called argument 5 quickly again")
    
Output :

First line will be printed like Now we will call some_work function then docstring will
print then some_work(4) will be called so there will be a pause or delay of 3 seconds then
return 4 which is replaced by some_work(4) then printed Done..calling again then called
some_work(1) so it will also delay for 3 seconds and then return 1 which is replaced by
some_work(1) then printed Called argument 1 then we called some_work(5) there will be 3
seconds delay as well and then return 5 which is replaced by some_work(5) then printed
Called argument 5 then we called some_work(7) which will also get a delay of 3 seconds
then return 7 which is replaced by some_work(7) then printed Called argument 7 then we
called some_work(4) again which will also take delay of 3 seconds because here cache of
last 3 calls would be some_work(1), some_work(5) and some_work(7) that is the reason there
is a delay as we have lru_cache(maxsize = 3) means it creates cache of last 3 calls and
some_work(4) was not present in last 3 calls so it does not come up quickly and takes
same delay of 3 seconds and then we return 4 which is replaced by some_work(4) then
printed We called argument 4 again then we called some_work(5) which is the call which
presents in last three calls by this function so its output will come up quickly
We called argument 5 quickly again just after We called argument 4 again as last 3 calls
would some_work(5), some_work(7) and some_work(4) this time that is the reason some_work(5)
displays quickly this time as lru_cache have cache of this some_work(5).


"""

