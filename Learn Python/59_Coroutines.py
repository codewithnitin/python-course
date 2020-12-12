"""

def searcher():
    import time
    book = "This is the book which describes the nature and wild life"
    # Suppose book is of 10k pages which takes 4 secs to read or download from web
    # time.sleep(4) is 4 seconds time consuming task like book or ML module reading
    time.sleep(4)

    while(True):
        text = (yield)
        if text in book:
            print("Yes, text is in the book")
        else:
            print("Text is not in book")

search = searcher()
print(search)
print("Search started")
search.__next__()
print("Next method ran")
search.send("wild")
search.send("environment")
search.send("life")
search.send("and wild")
search.send("describes the nature")
search.close()
search.send("wild")


"""


"""

Coroutines : These are those functions which we want to execute half in initial phase
and rest to execute all the time without starting the first half again.

( Ese function jinhe hum adha chalana chahte hai intially and phr uske aage se use
krna chahte hai har baar bina first half ko dobara chalaye )

Example : If signal is going to be green in just 10 seconds so we usually not to stop
the vehicle even it drains out some fuel and we move further to reach our destination.



In above approach we created one function naming searcher which has some work to
execute like reading or downloading ML module or any file or book which has 10 to
15k pages which consumes 4 seconds to perform this operation so we used time.sleep(4)
to show the operation which takes 4 secs to perform that task that is assumption only.

Now the question is how python interpreter will understand this function is not only 
a function this is coroutine by the way.

So here we will use one infinite while loop like 

     while(True):
        text = (yield)
        if text in book:
            print("Yes, text is in the book")
        else:
            print("Text is not in book")
            
Here, text = (yield) means this is not a normal function in spite of coroutine and
then we mentioned if else statement like if text which we wish to search comes under
book so prints Yes, text is in the book else prints Text is not in book.

Now we created one instance outside function like search = searcher() then prints
Search started so it starts the coroutine now we will start up the initial phase of
coroutine which is to read or download any ML or file or book which has 10K pages
which consumes 4 seconds so that is done by method or function called by next like

next(search) or search.__next__() both are same so after applying next method or
function on instance of coroutine our first half of coroutine which is to read or
download file or book or any ML module which consumes 4 seconds will be executed.

We do not wish to execute first half again as well as not to stop it ( Matlab gadi 
start rehne do aur aage chalte raho jabtak chaho )

For this we will create one infinite while loop in which we will type text = (yield)
if text which we wish to search inside book so prints Yes, text is in the book else
prints Text is not in book

Now the question is how we will search or find out text in this coroutine so we have
one function send(self,value) here self would be the instance of the coroutine and
value would be the text which we are searching in the book like

search.send(self,value) so when we call it so value would be the text as an argument
so argument will be passed into the declaration of coroutine def searcher(value): after
that first half will not be run and value will be searched in while loop directly
and it will go on for each and every search.send(self,value) again and again.

If we wish to release the resources of coroutine so we can close it as similar as file
closing like search.close() and if we call search.send("wild") again after closing
coroutine so it will give stop iteration which we had learnt earlier in Generator
as we have closed the coroutine means released all the resources and there is nothing
to iterate so it gives this error.

So if we wish to start up the coroutine so we can do it by search = searcher() then
applied next method or function on it like next(Search) which will execute the first
half of the function which consumes 4 seconds time delay and then we can find out
or search anything with the help of search.send("wild") like this.



"""

"""
Quizz : 

Create a program of coroutine in which we have 5 letters and where we pass input name
and if names comes in letter so prints Yes, text is in letter else prints text is not
in letters ?

"""


import time

def searcher():
    l1 = "This is the letter of Suresh"
    l2 = "This is the letter of Mahesh"
    l3 = "This is the letter of Ramesh"
    l4 = "This is the letter of Nitin"
    l5 = "This is the letter of Praveen"
    List_of_letters = [l1,l2,l3,l4,l5]

    #time.sleep(5) is the time consuming task which is reading or downloading letters
    time.sleep(5)

    while(True):
        text = (yield)
        for i in List_of_letters:
            if text in i:
                print("Yes, text is in letter naming", i)
                break
        else:
            print("Text is not in letters")

print("There are five letters l1, l2, l3, l4 and l5")
search = searcher()
print("Search started")
search.__next__()
print("Next method ran")
search.send("Nitin")
search.send("Pawan")
search.close()
search.send("Nitin")



