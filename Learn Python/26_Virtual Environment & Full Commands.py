"""
Virtual environment = It is just a clone of our base python interpreter

Why do we need of it?

Suppose I have made a project which uses flask module or library version 1 and sklearn 1.5
so if I am providing the source code of this project which could be anything like website or
game etc to the others after 2 years and meanwhile sklearn module has been upgraded so if a
person who is using my source code in which I had imported sklearn with previous version may
face error while executing the program and we do not want it actually that is why we have created
virtual environment where we can store our module along with the version which we had used at
the time of creating project for future purposes as well into the requirements.txt so we will
give requirements.txt in which we will have all the modules details which we had used while
creating project so that person can create virtual environment and can install that particular
modules version which were used earlier accordingly.

"""

# How will you create virtual environment now?

"""
First of all we will create a folder Tut by right click outside pycharm I mean on Desktop and then
we will enter by clicking on Tut after that we have to press shift + right click to open
windows power shell or command prompt and then we will get into command prompt or windows power
shell

Get into directory -> c:\users\NitinManali\Desktop\Tut  

Here we will install virtual environment module : pip install virtualenv once it is completed then
we can create our virtual environment by naming like : virtualenv Nitz once it is completed so we
will get a folder inside Tut naming Nitz which is virtual environment (NAVJAT SHISHU).

Now the thing is to activate virtual envrionment like : .\Nitz\scripts\activate then enter so we
will get into (Nitz):\users\NitinManali\Desktop\Tut so if we install any module here by pip
like (Nitz):\users\NitinManali\Desktop\Tut pip install pandas so it will be downloaded under Nitz
which is our virtual environment and then we can type python to launch python interpreter of
virtual environment Nitz and then import pandas into it and if we have flask and
sklearn in our base interpreter so we cannot import those modules here it will show an error no
module name is defined here because we did not install them under Nitz in spite of C:

Here we can type exit() to come out from python interpreter of Nitz and then type deactivate to
come out from virtual environment Nitz back to c:\users\NitinManali\Desktop\Tut 

Here we can activate our virtual environement again like .\Nitz\scripts\activate and then we will
enter into (Nitz):\users\NitinManali\Desktop\Tut here we will type command to get the details of
modules along with their version which are presented under this virtual environment :

(Nitz):\users\NitinManali\Desktop\Tut pip freeze > requirements.txt once it is completed so we will
get a text file inside Tut folder along with virtual environement folder naming Nitz so you can
give it to the others as these are modules which are present under it which were using to create
a project earlier so that person will create virtual environment in his/her PC and will install
the package accordingly.

Suppose you have requirements.txt of 500 modules so if you install like pip install sklearn==version
and then next module and so on so it does not make any sense here we have one command like :

(Nitz):\users\NitinManali\Desktop\Tut pip install -r .\requirements.txt once we enter it will 
download all the modules one by one which are present under requirements.txt that's amazing.

Suppose if you wish to create a virtual environment which will come up with site packages means
whatever modules we have in our base interpreter that virtual environement will have access of
base interpreter modules as well so we have one command for this

c:\users\NitinManali\Desktop\Tut virtualenv--system-site-packages Nitz2 so here will get a new
folder Nitz2 inside Tut where we have one virtual environment folder Nitz along with text file
requirements.txt so if we activate it by command like :

.\Nitz2\scripts\activate once it is activated and we enter into it like 
(Nitz2):\users\NitinManali\Desktop\Tut and then type python to launch python interpreter of
virtual environment Nitz2 and then import flask which were already presented in our base inter-
preter so we will not get any error as this environement has an access of base interpreter 
modules

so c:\users\NitinManali\Desktop\Tut virtualenv--system-site-packages Nitz2 (NavjatShishu nahi hai
kyunki ye base interpreter ke modules access kar sakta hai)

How to delete virtual environment?

c:\users\NitinManali\Desktop\Tut del Nitz once we enter so it will delete virtual environment Nitz
and there will be no folder anymore of Nitz inside Tut however if you wish to get it back so we
will type c:\users\NitinManali\Desktop\Tut virtualenv Nitz so it will create a folder Nitz inside
Tut and if we wish to install modules which were earlier so we will activate it first like
c:\users\NitinManali\Desktop\Tut .\Nitz\scripts\activate and then enter to activate it and then
(Nitz):\users\NitinManali\Desktop\Tut pip install -r .\requirements.txt so it will download
modules one by one from requirements.txt


"""