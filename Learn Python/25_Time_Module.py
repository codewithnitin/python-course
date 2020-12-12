import time
initial = time.time()     # It returns today time from some old day time in ticks means in seconds
# print(initial)
# How we can calculate how much time our program took to execute?

# j = 0
# while(j<10):
#     print("This is Nitin")
#     j+=1
# print("While loop ran time", time.time()-initial, "seconds")

"""
Here, time.time() is the current time which we get after program execution and initial is the time
which was recorded before program execution.

So, we can easily find out the time of program execution = time.time()-initial
"""

# initial2 = time.time()        # Time reset
# for i in range(10):
#     print("This is Nitin")
# print("For loop ran time", time.time() - initial2, "seconds")

"""
Here, time.time() is the current time which we get after program execution and initial is the time
which was recorded before program execution.

So, we can easily find out the time of program execution = time.time()-initial
"""

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

"""
Here, time.time() returns the current time from some old day time in ticks means in seconds then
return value of time.time() is changed into local time by time.localtime(time.time()) but we print
print(time.localtime(time.time())) so it gives localtime as an output in tuple form so to get the
output in presentable form time.asctime() is used as (time.asctime(time.localtime(time.time())))
then we can store it into the variable called localtime to print localtime


"""

for k in range(5):
    print("This is Nitin")
    time.sleep(2)               # time.sleep() gives pause to perform next iteration and so on

"""
Here, loop will be continuing 5 times so when k = 0 then will enter into the loop and print
This is Nitin and after that there will be a pause of 2 seconds and then k = 1 then will enter
into the loop again to print This is Nitin and it will keep continuing so on.

"""