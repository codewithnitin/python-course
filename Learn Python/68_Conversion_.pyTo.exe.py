"""
Conversion of python program file means .py to .exe

Why do we need of it?

The main basic reason behind it if we wish to run our python program which are in .py
extension on that machine which does not have python installed so there will be a need
to change it to .exe as that machine can run only those files which are having .exe
extension means executable files.

How we will do it then?

We have one external module pyinstaller by which we can change .py to .exe easily.

First of all we will create a folder or directory Tutorial anywhere inside the system
and then click on start menu of the PC and in search bar we will write IDLE(Python 3.8
32-bit) and click on it to open IDLE and then click on new file to write a python code
and then save it as series_num into the same directory or folder which we had created
early whose name is Tutorial so we saved the python file which are in .py extension as
series_num.py in the same directory or folder naming Tutorial.

Now we have python file series_num.py inside a folder or directory Tutorial but our task
is to change it into .exe extension file so in this folder we will open a command line
or power shell directory by pressing shift+right click once we do that so there we will
find an option of open command window here or power shell window here and once we click
on open command or power shell window here so we will get into the directory like

C:\Users\Nitin Manali\Desktop\Tutorial>

If we type C:\Users\Nitin Manali\Desktop\Tutorial> python series_num.py and then enter
so it will execute or run python file series_num.py code

Here we will install our external module pyinstaller like

C:\Users\Nitin Manali\Desktop\Tutorial>pip install pyinstaller

Once it is installed so we will type like this to change .py to .exe like this

C:\Users\Nitin Manali\Desktop\Tutorial>pyinstaller series_num.py       ( Matlab ese
C:\Users\Nitin Manali\Desktop\Tutorial>pyinstaller yourprogram.py ) then enter so it
will successfully change the series_num.py file into the same directory Tutorial by
naming like folder build, folder dist, file series_num.spec and one folder _pycache_
so here we need to click on dist folder and where we will get another folder with the
same name series_num and once we click on it so there will be so many files included
one series_num.exe file and if we click on it right now so it takes us to command or
power shell window and exit out which we do not want it actually so in this same
folder or directory which is series_num we will open command or window power shell
window again by pressing shift+right click to get into the command or power shell
utility whose path is

C:\Users\Nitin Manali\Desktop\Tutorial\dist\series_num> here we will open .exe file
like this

C:\Users\Nitin Manali\Desktop\Tutorial\dist\series_num>series_num.exe and then enter
so it will run our same python program code as in executable file which we can run
now in any machine which does not have python installed in it.


So we can forward the folder name dist to a person who does not have python in his/
her system to execute the .exe file of our python program but there is one drawback
as we know when we click on dist folder there will another folder naming series_num
which is as similar as our python program file series_num.py and when we click on
series_num folder inside dist folder so there will be so many files which all are
the dependencies files for file series_num.exe except series_num.exe so if we think
to delete such files and just past series_num.exe to a person which have no python
installed in his/her system so it will not run as these all files are dependent on
series_num.exe but we want only one file series_num.exe to forward in spite of all
these dependencies so pyinstaller have something very special for us.

We will type like this while changing .py to.exe using pyinstaller

C:\Users\Nitin Manali\Desktop\Tutorial>pyinstaller --oneline series_num.py
once it is completed so we will have folder _pycache_, folder dist, folder build &
file series_num.spec inside the same directory or folder Tutorial and this time
once we click on the folder dist so there will be only single file which is
series_num.exe instead of a folder name series_num and inside it lots of dependen-
cies files along with series_num.exe



In this approach we change the python file series_num.py which had below code to
represent a series of numbers in a single row till n number which is entered by
user.



Note :

1)
Suppose we had used some of the modules while writing python program / code
or might be not using modules as we did not use any module inside our python code
example of series_num if we changed our .py into .exe so it will run as it is which
we were running in .py extension in python ( Matlab python code me module use ho ya
nahi ho python agar woh python code file change kr li .exe meh toh as it is work
kregi hume koi bhi tension nahi leni )

2) When we open command or power shell window so directory must be same or that
where our file is present which we wish to execute or run ( Basic funda hai chahe
python ki file kholo chahe .exe ya koi aur extension matlab directory koi aur kholi
aur file kahi aur loacation par hai toh nahi open hogi )




"""
def series_num(num):
    for i in range(0,num + 1):
        print(i, end=" ")
num = int(input("Enter the number\n"))
series_num(num)