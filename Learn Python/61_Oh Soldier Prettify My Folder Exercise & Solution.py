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
