
# import Pycharm__Nitin
#
# obj = Pycharm__Nitin.Improvement_module()
# print(obj.achafunc("Kya baat hai Nitin Bhai kya module banaya hai aapne :)"))


"""
First of all we created one directory or folder naming Pycharm__Nitin inside 
directory whose path is C://Users/Nitin Manali/PycharmProjects/FirstProg so
we will have one folder Pycharm__Nitin under FirstProg.

We also created another folder naming Pycharm__Nitin along with two text files
naming license.txt and readme.txt and one python file setup.py inside the dir
Pycharm__Nitin whose location path is 
C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin
so we have one folder Pycharm__Nitin along with two text files license.txt and
readme.txt and setup.py inside the dir Pycharm__Nitin

Here we built a python file __init__.py inside that folder naming Pycharm__Nitin
which is adjacent to license.txt and readme.txt

Now we will type our code inside __init__.py like this

def achafunc(a):
    print("This is a function")
    return(a)
    
After that we will tell to the file setup.py that a folder naming Pycharm__Nitin
which has a file __init__.py is a package or module ( Matlab yaha hum kahenge
setup.py ko ki bhai ye jo folder hai Pycharm__Nitin jisme file hai __init__.py
woh ek package hai or module hai ) by writing this code like this

from setuptools import setup

setup(name = "Pycharm__Nitin",
      version = 0.2,
      description = "This is a module which is made by code with Nitin",
      author = "Nitin",
      packages = ["Pycharm__Nitin"],
      install_requires = [])
    
    
We used one inbuilt module of python naming setuptools here and then imported its
function setup which is used to create wheel file of one package (Matlab jaise
abhi hmare pas ek package hai Pycharm__Nitin jisme file hai __init__.py toh jb ek
package ki wheel file bnate hai toh setup function ka use krte hai aur agar hmare
pas aur packages hote jaise Pycharm1__Nitin usme ek file hoti __init__.py aur ek
hota Pycharm2__Nitin usme ek file hoti __init__.py toh tb agr hum chahte ki ek
wheel file banaye ye saree packages ki toh ek function hota hai setuptools module
me jiska name hai find_packages ye ek se jayda packages ho toh unki ek wheel file
bana deta hai )

After importing setup function we declare some of the required things like that

setup(name = "Pycharm__Nitin",
      version = 0.2,
      description = "This is a module which is made by code with Nitin",
      author = "Nitin",
      packages = ["Pycharm__Nitin"],
      install_requires = [])
      
      
Here name = "Pycharm__Nitin" tells the name of the module and version = 0.2 tells
the version of the module, description = "This is a module which is made by code 
with Nitin" tells for what purpose this module is created and who is created ( ye
hum kuch bhi describe kr skte hai ), author = "Nitin" tells the owner name of this
module, packages = ["Pycharm_Nitin] tells how many packages are there in our code
there is ony one package or module naming Pycharm__Nitin ( agar ek se jayda hote
jaise Pycharm1__Nitin aur Pycharm2__Nitin toh packages = ["Pycharm__Nitin","Pych-
arm1__Nitin","Pycharm2__Nitin"] jb hum find_packages function use krte hai) then
install_requires = [] ( jaise hamari __init__.py me jo code hai usme koi module
import nhi kiya but agar krte toh us module ka name install_requires=[] iss list
me daal dete hai toh ye bhi package ke sath install hote hai jo module package per
depend kr rhe hote hai )


Now we will open our command prompt or window power shell so we will be in our
directory like C://Users/Nitin Manali>  and then we type python to launch our
python interpreter >>> import Pycharm_Nitin then enter so will get an error as
No module name found ( Kyunki abhi toh sirf __init__.py and setup.py me code likha
hai wheel file nhi bani )

So inside this directory C://Users/Nitin Manali we will install module wheel which
will be helpful us to create wheel file of our package or module folder Pycharm__
Nitin like this C://Users/Nitin Manali>pip install wheel then enter to install it

Once it is installed so we will change the directory where our setup.py is located
to C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin after that we 
will type this command like this

C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin>python setup.py 
sdist dist_wheel  once we we enter this to process so we will get some folders 
build, dist and Pycharm_Nitin.egg-info just adjacent to our module or package
folder Pycharm__Nitin which has __init__.py which we had created earlier inside
the dir Pycharm__Nitin.

In dist folder we will have two files like this :
Pycharm__Nitin-0.2.tar.gz
Pycharm_Nitin-0.2-py3-none-any.whl

Now we have wheel file Pycharm_Nitin-0.2-py3-none-any.whl inside a folder dist
which we got after running a command python setup.py sdist bdist_wheel inside
dir Pycharm__Nitin

We got wheel file of our package or module Pycharm__Nitin but still our package
will not be treated as module untill we install this wheel file so we will change
our directory to dist folder like this

C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/dist

As we know our wheel file is presented inside a folder dist that is the reason
we change our directory to dist folder here and now we will install our wheel
file like this

C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/dist>pip install
Pycharm_Nitin-0.2-py3-none-any.whl    once we enter it so this wheel file will
be installed inside our site-packages folder as we know all our module which
we install from pip are installed into this location site-packages and once we
got a message successfully installed on command prompt so it means now our 
package or module naming Pycharm__Nitin becomes a module which we can import
from anywhere after restarting our cmd or our IDE like pycharm.


Now we opened our cmd again into this directory like this

C://Users/Nitin Manali>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import Pycharm__Nitin
>>> print(Pycharm__Nitin.achafunc(100))
This is a function
100

If we change the directory to dist even still we will get the same result
as we have created module Pycharm__Nitin now like this

C://Users/Nitin Manali>cd "C:/Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/dist"

C:/Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/dist>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import Pycharm__Nitin
>>> print(Pycharm__Nitin.achafunc("Nitin bhai bhot acha module banaya aapne :)")
...
...
... print(Pycharm__Nitin.achafunc("Nitin bhai bhot acha module banaya aapne")
  File "<stdin>", line 4
    print(Pycharm__Nitin.achafunc("Nitin bhai bhot acha module banaya aapne")
    ^
SyntaxError: invalid syntax
>>> print(Pycharm__Nitin.achafunc("Nitin bhai bhot acha module banaya aapne :)"))
This is a function
Nitin bhai bhot acha module banaya aapne :)



If we come to Pycharm instead of command prompt still we can use this nodule
like this

import Pycharm__Nitin

print(Pycharm__Nitin.achafunc("Nitin bhai bhot acha module banaya aapne :)"))

Output :

This is a function
Nitin bhai bhot acha module banaya aapne :)

We can change path in IDE as well like this

import Pycharm__Nitin
import os
print(os.getcwd())
os.chdir("C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/build")
print(os.getcwd())

print(Pycharm__Nitin.achafunc("Nitin bhai bhot acha module banaya aapne :)"))

Output :

C:/Users/Nitin Manali/PycharmProjects/FirstProg
C:/Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/build
This is a function
Nitin bhai bhot acha module banaya aapne :)




# SECOND APPROACH 

Suppose we made some improvement in our module or package inside a file __init__.py
as software communities do (Matlab kal ko humne apna module kuch aur behtar bana
diya jaise software communities apne module ko behtar krti hai tb unka new version
aata hai update hoke hmare liye waise he hum bhi kr sakte hai jaise humne kiya apni
__init__.py ) like this

class Improvement_module:
    def __init__(self):
        print("Constructor ban gaya atti uttam :)")

    def achafunc(self, a):
        print("This is a function")
        return(a)
        
Then we will also change the version inside our setup.py file like this

from setuptools import setup

setup(name = "Pycharm__Nitin",
      version = 0.4,
      description = "This is a module which is made by code with Nitin",
      author = "Nitin",
      packages = ["Pycharm__Nitin"],
      install_requires = [])
      
Now we have changed our version from 0.2 to 0.4

After that we will come to our command prompt window and will get into
the directory Pycharm__Nitin where our setup.py is present or located
C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin and then
type a command like this

C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin>python
setup.py sdist bdist_wheel then enter so we will get new wheel file with
version 0.4 inside a folder dist like Pycharm_Nitin-0.4-py3-none-any.whl

After that we will change our directory to dist folder where our wheel
file is present with version 0.4 as well as 0.2 like this

cd "C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/dist"
Once we enter it so we will get into this dist folder directory like

C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/dist> then
will write a command which is given below

C://Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/dist>pip
install Pycharm_Nitin-0.4-py3-none-any.whl and once we enter so our prev
version 0.2 file will be uninstalled first and then 0.4 version will be 
installed successfully due to which our package or module Pycharm__Nitin
will be treated as module now and then we will exit() from cmd now to re-
start the resources


Once we open our cmd again like this

C:/Users/Nitin Manali>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import wheel
>>> import Pycharm__Nitin
>>> obj = Pycharm__Nitin.Improvement_module()
Constructor ban gaya atti uttam :)
>>> print(obj.achafunc("Kya baat hai Nitin bhai kya module banaya hai aapne Balle balle shaba shaba :)"))
This is a function
Kya baat hai Nitin bhai kya module banaya hai aapne Balle balle shaba shaba :)


We can also change the directory to import this module as well like this

C:/Users/Nitin Manali>cd "C:/Users/Nitin Manali/PycharmProjects/FirstProg\Pycharm__Nitin/build"

C:/Users/Nitin Manali/PycharmProjects/FirstProg/Pycharm__Nitin/build>python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import Pycharm__Nitin
>>> obj = Pycharm__Nitin.Improvement_module()
Constructor ban gaya atti uttam :)
>>> print(obj.achafunc(100))
This is a function
100


We can use this module Pycharm__Nitin via IDE like pycharm like this

import Pycharm__Nitin

obj = Pycharm__Nitin.Improvement_module()
print(obj.achafunc("Kya baat hai Nitin Bhai kya module banaya hai aapne :)"))

Output :

Constructor ban gaya atti uttam :)
This is a function
Kya baat hai Nitin Bhai kya module banaya hai aapne :)


 















"""