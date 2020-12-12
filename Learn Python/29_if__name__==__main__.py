import Name_main1
print(Name_main1.add(2,3))



# When we run the above statement so we will get extra output in terms of all content which is
# present under the file Name_main1 and that is not our desired output as we just want sum of
# x and y according to arguments which we are passing here this is because import statement
# gives the output in terms of full content of file which we are importing to use its variables,
# functions etc so here we have one function __name__ = __main__ to get the desired output :

"""

if __name__ == '__main__':
    print(a)
    print(printjoke("Gabar"))
    print(add(4,5))
    
Here, we will put if __name__ == '__main__': then enter into it  along with indentation before 
the print statements of Name_main1 so it defines if __name__ == __main__ so a file Name_main2
which is importing Name_main1 can get the desired output accordingly which we want in file
Name_main2 in spite of providing extra content of Name_main1


# Output now : 

# The name is Name_main1
# Sum of x and y is 5

This is because import statement reads first print statement of Name_main1 which is
print("The name is", __name__) we will get The name is Name_main1 as we are importing
content from Name_main1 in terms of anything like function , variables etc and then got the
desired output as per computation print(Name_main1.add(2,3))
"""




