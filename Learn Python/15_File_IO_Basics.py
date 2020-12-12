"""
File Io Basics:

File : File is nothing just a memory it could be any text, audio, image etc.

There are two types of memory we have :

Hard drive memory : Non Volatile means whatever we store into it so it will remain same when we shut
down the system and restarts it again so data will be present as same as earlier.

RAM memory        : Volatile means data will vanish when we shut down the system so we will not get
these memories again when we restart it or permanent delete.
"""
"""
Real life operation of file :

Example : Image or MP3 both are the examples of binary data file so whatever we encode into the file
for image or audio file here our image viewer or audio player softwares decode the program to give
the output in terms of displaying picture or playing music.

"""

""" 

File modes :

"r" - Open a file for reading 
"w" - Open a file for writing
"x" - Create a file if file does not exist
"a" - Append the file - Add content to the end of the file
"t" - Text mode 
"b" - Binary mode 
"r+" - Update the file - Read or write the file

"""
"""
Note :

"r" - default mode which means if we write it into the open("file name", "r") or like
open("file name") we will get same output which we will see in next.
    
Similarly, "t" - default mode which means if we write it into the open("file name", "rt") or like
open("file name") we will get same output which we will see in next.
"""


