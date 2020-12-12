# import os
# from datetime import datetime

# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# print(os.listdir())
# os.mkdir("Movies")
# os.rmdir("Movies")
# os.makedirs("Movies/Songs/Bolly/Holly")
# os.rename("Movies", " Best Movies")
# print(os.listdir())
# os.removedirs("Movies/Songs/Bolly/Holly")
# print(os.getcwd())
# print(os.stat("Nitin.txt"))
# print(os.stat("Nitin.txt").st_size)
# print(os.stat("Nitin.txt").st_mtime)
# Mod_time = os.stat("Nitin.txt").st_mtime
# print(datetime.fromtimestamp(Mod_time))
# for dirpath, dirfolder, filenames in os.walk("C:/Users/Nitin Manali/PycharmProjects/FirstProg"):
#     print("Current path :", dirpath)
#     print("Directory Folder :", dirfolder)
#     print("File name :", filenames)
#     print()

# print(os.environ.get("path"))

# print(os.path.join("C://Users/Nitin Manali","Nitin.txt"))

# file_path = "C://Users/Nitin Manali" + "Nitin.txt"
# print(file_path)

# print(os.path.exists("C://"))
# print(os.path.isdir("C:/Users/Nitin Manali/PycharmProjects"))
# print(os.path.isfile("C:/Users/Nitin Manali/PycharmProjects/FirstProg/Nitin.txt"))

# for item in os.listdir():
#     print(os.path.join("C:/Users/Nitin Manali/PycharmProjects/FirstProg",item))

# for item in os.listdir():
#     print(os.path.splitext(item))



"""

OS : OS stands for operating system which controls all the hardware of the system like handling mouse input,
what to need to display on monitor etc.

OS is used to handle all the resources of the system in an optimal manner.

Now we will study what we can do with the help of OS module in python so we will learn some of the useful
functions of this module.

os.getcwd() : This is to get our current working directory.

os.chdir()  : This is to change the current working directory like

os.chdir("C://") so we changed the current working directory by assigning path "C://" to function os.chdir()
and if we print print(os.getcwd()) now output will become C:\  as directory has been changed.

print(os.listdir()) : It shows the list of folders and files of our current working directory and if we
assign path like this print(os.listdir("C://") so we can find out the list of folders and files of the
directory which we assigned into this function.

os.mkdir("Movies") : It creates an empty folder inside our current working directory and if we wish to remove
this folder so we have one function like os.rmdir("Movies") so it will remove this folder which we had created
inside our current working directory.

os.makedirs("Movies/Songs/Bolly/Holly") : It creates a folder Movies inside it sub folder Songs inside it
sub folder Bolly and inside it sub folder Holly and if we wish to remove this complete folder and its sub
folders so we have one function like os.removedirs("Movies/Songs/Bolly/Holly")

os.rename("Movies", "Best movies"): It is used to rename the folder or any file inside the current working
directory.

print(os.stat("Nitin.txt")): It gives all the details st_size means size of the file in bytes and when it
was modified or created last by st_mtime like

print(os.stat("Nitin.txt").st_size) : Output would be 94 that is size of the file in bytes.
print(os.stat("Nitin.txt").st_mtime) : Output would be time 1595591384.142078 so to make it human
readable format we will import datetime function of module datetime and then we will store this time like

Mod_time = os.stat("Nitin.txt").st_mtime 

then print print(datetime.fromtimestamp(Mod_time)) to get an output in human readable format : 

2020-07-24 17:19:44.142078



Suppose we have current working directory "C:/Users/Nitin Manali/PycharmProjects/FirstProg and we wish to
find out all the folders, sub folders and files I mean tree like structure of the directory as listdir()
gives only folder and files not sub folders and its files due to which we have one function called os.walk()

os.walk() : Basically it is a generator that yields a tuple of three values as path, directories or folders
and files.

So syntax would be like 

for dirpath, dirfolder, filenames in os.walk("C:/Users/Nitin Manali/PycharmProjects/FirstProg):
    print("Current path :", dirpath)
    print("Directory Folder :", dirfolder)
    print("File name :", filenames)
    print()
    
Output :

Current path : C:/Users/Nitin Manali/PycharmProjects/FirstProg
Directory Folder : ['.idea', 'Movies', '__pycache__']
File name : ['24_Args_Kwargs.py', '10_While Loop_Break and Continue.py', 'Contacts', '59_Coroutines.py', '33_Decorators.py', '58_Else & Finally In Try Except.py', '27_Enumerate_Function.py', 'Eye.mp3', '22_F-Strings & String Formatting.py', '15_File_IO_Basics.py', '15_File_IO_Basics_File Handling.py', '28_How Import Works in Python.py', 'File_2.py', '13_Functions_Docstrings.py', '57_Function Caching.py', '54_Generators.py', '18_Scope_Local & Global Variable & Global Keyword.py', 'Harry_diet.txt', '17_Health Management System_Exercise & Solution.py', '32_Healthy programmer_Exercise & Solution.py', '30_Join Function.py', '53_Library Project Based On OOPS Exercise & Solution.py', 'log_data.txt', '31_Map_Filter_Reduce Function.py', 'Name_main1.py', '29_if__name__==__main__.py', 'Nitin.txt', '1_Comment_Escape_Print.py', '2_Variable_Datatypes.py', '3_String Slicing_Its Functions.py', '4_List_Its Functions_Tuple.py', '5_Dictionary_Its Functions.py', '6_Sets_Its Functions.py', '7_If Else Conditions.py', '8_For Loop.py', '9_While Loop.py', '34_OOPS_Introduction.py', '35_OOPS_Creating Our First Class.py', '44_OOPS_Multilevel Inheritance.py', '45_OOPS_Public_Protected_Private Access Specifiers.py', '46_OOPS_Polymorphism.py', '47_OOPS_Super() & Overriding.py', '48_Diamond Shape Problem in Multiple Inheritance.py', '49_OOPS_Operator Overloading & Dunder Methods.py', '50_OOPS_Abstract Base Class & @abstractmethod.py', '51_OOPS_Setters & Property Decorators.py', '52_OOPS_Object Introspection.py', '36_OOPS_Instance & Class Variables.py', '37_OOPS_Self & __init__() (Constructors).py', '38_OOPS_Class Methods.py', '39_OOPS_Class Methods As Alternative Constructors.py', '40_OOPS_Static Methods.py', '41_OOPS_Abstraction & Encapsulation.py', '42_OOPS_Single Inheritance.py', '43_OOPS_Multiple Inheritance.py', '11_Operators.py', '60_OS Module.py', 'Physical.mp3', 'Praveen.txt', '55_Python Comprehensions.py', '19_Recursive vs Iterative Approach Using Factorial & Fibonacci example.py', 'Rohan_diet.txt', '12_Short Hand IF Else Notation.py', '23_Game Development_Snake_Water_Gun_Exercise and Solution.py', '20_Sort_Sorted_Lamda Or Anonymous_Function.py', '25_Time_Module.py', '14_Try_Except ExceptionHandling.py', '21_External & Built In Module.py', '56_Using Else With For Loop.py', '26_Virtual Environment & Full Commands.py', 'Water.mp3']

Current path : C:/Users/Nitin Manali/PycharmProjects/FirstProg\.idea
Directory Folder : ['inspectionProfiles']
File name : ['.gitignore', 'FirstProg.iml', 'misc.xml', 'modules.xml', 'workspace.xml']

Current path : C:/Users/Nitin Manali/PycharmProjects/FirstProg\.idea\inspectionProfiles
Directory Folder : []
File name : ['profiles_settings.xml']

Current path : C:/Users/Nitin Manali/PycharmProjects/FirstProg\Movies
Directory Folder : ['Songs']
File name : []

Current path : C:/Users/Nitin Manali/PycharmProjects/FirstProg\Movies\Songs
Directory Folder : ['Bolly']
File name : []

Current path : C:/Users/Nitin Manali/PycharmProjects/FirstProg\Movies\Songs\Bolly
Directory Folder : ['Holly']
File name : []

Current path : C:/Users/Nitin Manali/PycharmProjects/FirstProg\Movies\Songs\Bolly\Holly
Directory Folder : []
File name : []

Current path : C:/Users/Nitin Manali/PycharmProjects/FirstProg\__pycache__
Directory Folder : []
File name : ['File_2.cpython-38.pyc', 'Name_main1.cpython-38.pyc']



Now, if we wish to get environment variables so we have one function like

print(os.environ.get("path"))  : It shows an environment variables as provided variable path here.

Suppose I wish to join file "Nitin.txt" into the path "C:/Users/Nitin Manali" to create a combined
location path to reach this file so we have traditional approach like this

file_path = "C:/Users/Nitin Manali" + "Nitin.txt"
print(file_path)

Output : C:/Users/Nitin ManaliNitin.txt 

There is one problem occurs as we did not get / after Nitin Manali to join the file "Nitin.txt" because
it just concatenate strings.

Due to which we have one function os.path.join by which we do not even need to worry about how many slashes
would be present to join like

print(os.path.join("C:/Users/Nitin Manali","Nitin.txt")) 

Output : C:/Users/Nitin Manali/Nitin.txt  

Now, we got the / after Nitin Manali so we do not need to think about slashes and all as it joins two
paths or path with file in very optimal manner.

 


os.path.exists(): It gives an output in True or False suppose if we wish to check any directory or file exists
so we can check it like

print(os.path.exists("C://") so output would be True as this directory exists
print(os.path.exists("C://Nitin.txt") so output would be False as this file does not exist inside "C://"
print(os.path.exists("C:/Users/Nitin Manali/PycharmProjects/FirstProg/Nitin.txt")
so output would be True as Nitin.txt file exits inside this directory.

os.path.isfile(): It is used to check files only like

print(os.path.isfile("C://") Output would be False as it is directory path.
print(os.path.isfile("C:/Users/Nitin Manali/PycharmProjects/FirstProg/Nitin.txt") Output would be True
as Nitin.txt file presents inside the director FirstProg.

os.path.isdir(): It is used to check directory paths only like

print(os.path.isdir("C://") Output would be True as this is directory path.
print(os.path.isdir("C:/Users/Nitin Manali/PycharmProjects/FirstProg/Nitin.txt")) Output would be False
as this is file not a directory path.


os.path.splitext(): It is used to separate out the files or folder by its names and its extension in a 
tuple form suppose we have one file "Nitin.txt" and we apply this print(os.path.splitext("Nitin.txt")
so we will get an output like 

Output : ('Nitin', '.txt')




NOTE : Folder is also known as Directory and directory path is different like "C://"





"""


"""

Create a program to prettify the folder in which we will have one file inside folder which contains the name
of those files which we won't alter means will be excluded from the operation ( aur ye small letters me hongi
kyun ki ye module names file hai jinhe capital me save kre toh module name se clash hoke ye compilation error
deti hai ) and rest of the files will be capitalized by its first letter and selective format files like jpg 
or png etc will be renamed by serial numbers like 1.jpg,2.jpg,3.jpg and so on  ?


"""

# Oh Soldier Prettify My Folder

def soldier(path,file_name,file_extension):

    import os
    os.chdir(path)
    files = os.listdir(path)
    f = open(file_name, "r")
    content = f.read()
    i = 1
    for item in files:
        if item.endswith(file_extension):
            os.rename(item,f"{i}{file_extension}")
            i = i + 1
        elif item not in content:
            os.rename(item,item.capitalize())
    f.close()

soldier("C://Users/Nitin Manali/PycharmProjects/FirstProg/Soldier",
        "C://Users/Nitin Manali/PycharmProjects/FirstProg/Soldier/naveen.txt", ".jpg")





















