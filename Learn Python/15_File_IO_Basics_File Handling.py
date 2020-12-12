"""
open("filename", "mode") here open() opens up the file by its name for the operation of mode

f = open("filename", "mode") here f is the file pointer which is returned by the open()

Variable = f.read()   here calling read function to return the content of pointer f and we store
it into the Variable then print variable like

print(Variable) To get the full output which is present inside our filename

Variable = f.read(5)    here pointer f returns the first 5 characters of the file and store it
into the Variable then print variable like
print(Variable)      To get output in terms of first 5 characters only

Variable = f.read(5)    here pointer f returns the second 5 characters of the file and store it
into the Variable then print variable like
print(Variable)      To get output in terms of second 5 characters only


Variable = f.read(2550)
print(Variable)  To get the full output which is present inside our filename

Variable = f.read(2550)
print("1", Variable)    To get the full output in terms of reading 2550 characters so if text
file does not have that much characters so it will display the full text file content

Variable = f.read(5)
print("2", Variable)    output 2 Blank because pointer read the full text above in
output 1 file content

To display the content of the file line by line

content = f.read()
for line in content:
     print(line)           Output character wise file content but we do not want it actually

#content = f.read()        Avoid reading the file pointer content here as we will call pointer
f directly by for loop like

for line in f:
     print(line)          Output we will get the desired output here print() gives \n new line
character itself so to avoid it we will type print(line, end="") to get the desired output

print(f.readline())      To display the one line of file content and if we type it again
print(f.readline())      so, pointer will move to next line to display it as well and so on

print(f.readlines())     To display the file content in list and it shows \n new line character
in console which is the new line character itself in file not by print()

"""
# Operation of file handling with the help of above for the file Nitin.txt
"""
f = open("Nitin.txt", "r")
content = f.read()
print(content)
f.close()
"""
"""
f = open("Nitin.txt", "rt")
content = f.read()
print(content)               #Same output as above because "r" and "t" both are default mode
f.close()
"""
"""
f = open("Nitin.txt", "rb")
content = f.read()
print(content)               #Output comes up in binary mode as we have reading mode in binary
f.close()
"""
"""
f = open("Nitin.txt", "r")
content = f.read(4)
print(content)               #Output displaying only first 4 characters
f.close()
"""
"""
f = open("Nitin.txt", "r")
content = f.read(4)
print(content)               #Output displaying only first 4 characters
content = f.read(4)
print(content)          #Output displaying only second 4 characters as pointer moves for the next 4
f.close()
"""
# To display the file content line by line
"""
f = open("Nitin.txt", "r")
content = f.read()
for line in content:
    print(line)            #Output we are getting character wise here which we do not want actually
f.close()
"""
"""
f = open("Nitin.txt", "r")
#content = f.read()        Avoid calling the file pointer return value by read() as we will call
# pointer f directly to display the desired output
for line in f:
    print(line)
f.close() 
   
#Here print() gives \n new line character itself in output to avoid it
# we will use end new line character like print(line, end= "")

"""
"""
f = open("Nitin.txt", "r")
for line in f:
    print(line, end= "") #Here new line character in terms of line which presents itself in file
f.close()
"""
"""
f = open("Nitin.txt", "r")
print(f.readline())      #Output will display first line
print(f.readline())      #Output will display second line 
f.close()
"""
#Here print() gives \n new line character itself in output to avoid it
# we will use end new line character like print(line, end= "")
"""
f = open("Nitin.txt", "r")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline())      #Desired output and here new line character comes by file itself
f.close()
"""
"""
f = open("Nitin.txt", "r")
print(f.readlines())     #Desired output will come up in list along with \n character
f.close()
"""

# Writing and appending to a file
"""
f = open("Praveen.txt", "w")
f.write("Praveen is a great musician")

# If we wish to display the count of characters in above statement so we will do
# v = f.write("Praveen is a great musician")    
print(v)
     
f.close()
"""

"""
Creating a file for writing mode and here mode is "wt" as t is a default mode, writes the statement
into f.write("Statement") then we run console so no error will come and paste the statement
into the file

Note : Here when we run console again so "w" wipes out the file and then write it with the current
f.write("statement") and it works for every run console command.
"""
"""
f = open("Praveen.txt", "a")
f.write("He is a good boy too\n")
f.close()
"""

"""
Appending a file with the mode "a", writes the statement into f.write("Statement") then we 
run console so no error will come and paste the statement at the end of the current file 
content

Note : Here when we run console again so "a" adds statement again at the end of current file
content and it works for every run console command.
"""
"""
f = open("Praveen.txt", "r+")
print(f.read())
#f.write("He will clear all the grades of guitar for sure")
f.write("He will definitely clear all the grades of guitar")
f.close()
"""

"""
"r+" if we wish to perform both the operations read and write into the file so we use this "r+"
mode
"""

# Seek() and tell() to a file :
"""
tell()           It tells position where our file pointer or handler presents in the file

Seek()           If we have read more into a file and we wish to read something 
                 again which we had read earlier so we will assign position from 
                 where we wish to read the file content again
"""
"""
f = open("Praveen.txt", "r")
print(f.readline())
print(f.readline())
f.seek(7)
print(f.readline())
print(f.tell())
f.close()
"""
# Using with block to open Python files :

# Syntax to open file using with block :

# with open("filename", "mode") as f: OR f = open("filename", "mode") both are same syntax
# Perform operation with file pointer f
# Note : with block closes the file itself so no need to type f.close() here and once the file
# content is read so if we perform further operation with file function so we do not get any
# output as there will be nothing to access further into the file

"""
with open("Praveen.txt", "r") as f:
    print(f.readlines())         # Print whole content of file in list
    print(f.readline())          # No output as file content is read completely above

with open("Praveen.txt", "r") as f:
    print(f.readline())   # Print first line of the file
    print(f.readline())   # Print new line character due to print() and then print second line
    print(f.read())       # Pointer moves and then prints further content of the file

"""
"""   
Question : Can we print something after using with block to open & perform operation with file
if Yes or No then why?

Answer : Yes, as with block closes the file itself so if we wish to open file with previous Syntax
so we will perform the same operation which we were performing earlier

Refer to below example of this which states it clearly 
"""

"""
with open("Praveen.txt", "r") as f:
    print(f.readline())
    print(f.readline())
    # print(f.read())
f = open("Praveen.txt", "r")
print(f.read())
f.close()

"""


"""
Create a pattern in which we will take input as a number from user to display
pattern 
                    *
                    **
                    ***
                    ****
                    *****
                    
if boolean user input is True and if it is False then display a pattern

                    *****
                    ****
                    ***
                    **
                    *
?


n = int(input("Enter the number of rows"))
b = bool(int(input("Type 1 for True or 0 for False")))
print(b)
if b == True:
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        print()
elif b == False:
    for i in range(1,n+1):
        for j in range((n+1)-i):
            print("*", end=" ")
        print()
"""






# Practice


n = int(input("Enter the number"))

n1 = bool(int(input("Type 1 for True 0 for False")))

if n1 == True:
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()
else:
    for i in range(1,n+1):
        for j in range((n+1)-i):
            print("*",end="")
        print()




