
"""

There is a story whenever we talk about softwares like MS Office, Adobe Photoshop, Google Chrome,
Pycharm, Notepad++. These all are GUI based softwares where we give input by clicking mouse and
navigate to open up web pages. (Matlab yha click kro toh ye hoga waha kro toh woh hoga jaisa
dikhega hume ki yha click krne se ye response milega waha se ye toh hum waise inhe use krte hai
to get the output )

Command line utility or software : It is a program which allows end user to pass or give input
as a text form command and then our system or computer responds back accordingly. ( Yha kuch
dikhega nhi ki esa kroge toh esa milega toh hum command pass krte hai cmd or window powershell
se computer ko ki bhai ye input humne diya aapko and ab appko output dena hai hmari input di
gyi command ke according.)

So we learnt there are two types of softwares one is GUI and another one is Command line utility.

Now the question raises why we need of command line utility ?

Suppose we are programmer of python language and we are creating one utility where we need of
output of one of the GUI based software or application like MS Excel so it will difficult for
us to get an output of GUI into command line utility. ( Agar hum kahe ki ek esa python program
likho jo excel ko open kre excel me computation kre phr excel ka jo output ho usko le aaye
python me and usko use krke phr hum further python me apna aage ka kaam kre ye hum kr skte hai
pr command line utlity se kisi GUI ka output lena bahot difficult padta hai isliye hum command
line utlity bnate hai )

This is because if we have command line utlity or software so we can easily call it from any
programming language to get an output which will appear on console  ( Suppose koi programmer
hai jo C or Java me code likhta hai and usse apne code me kuch esi cheez ki need hai jo python
me ache se kri jaati hai ya sirf python me he hoti hai jaise tensorflow module ho ML module ho
toh woh programmer python me aayega and argparse module ki help se jis cheez ka output chahe
apne code ke liye uski utility banayega and apni programming language C or Java se python me
bani utility ko call krlega ab yha call krne ke liye har programming language me kuch and kuch
hota hai toh aap call kr skte ho kisi bhi language me bani command line utility ko kisi bhi
programming language se and jo output aata hai console pr usko leke apne code me aage ka kaam
kr skte ho )


Today we will study how we can create our own command line utility in python with built in
module argparse instead of learning how to call command line utility which is made on one lang
by calling some other language( Isko banake hum apni utility ko software communities ko de skte
hai or distribute kar sakte hai ki yeh meri command line utlity hai isko aap use kre aur apna
further kaam kre )


Note : Command line utility is also used to pass command line arguments mean when we provide
arguments from cmd or window powershell at the time of run time.





"""


import argparse
import sys

def cal(args):
    if args.o == "add":
        return(args.x + args.y)
    elif args.o == "sub":
        return(args.x - args.y)
    elif args.o == "mul":
        return(args.x * args.y)
    elif args.o == "div":
        return(args.x / args.y)
    else:
        return("Something went wrong")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=3.0, help="Enter the first number")
    parser.add_argument("--y", type=float, default=1.0, help="Enter the second number")
    parser.add_argument("--o", type=str, default="add", help="What do you want to do?")

    args = parser.parse_args()
    sys.stdout.write(str(cal(args)))


"""

First of all we imported two modules one is argparse which is used to create command line
utility in python and sys module which is used to display an output in command line screen
or console.

After importing these modules we created one main function like if __name__ == '__main__'
inside it we created one object Parser of the class ArgumentParser() which is present inside
the module argparse like this parser = argparse.ArgumentParser() so now we have created one
object Parser of class ArgumentParser() which exists inside the module argparse.

After that we know we have one function add_argument() inside the class ArgumentParser() so
we will call this function by object Parser of this class ArgumentParser() like this 

parser.add_argument("--x", type=float, default=3.0, help="Enter the first number")

Here we pass command line argument --x and you can remember we had also passed command line
argument while creating one file of .exe in the conversion of .py to .exe like this
pyinstaller --onefile yourfile.py

So we pass command line argument with help of this add_argument function of the class
ArgumentParser() and here we also mention type of the argument which is type = float and
default value of the argument is 3.0 and help = "Enter the first number" inside the add_
argument() like this

parser.add_argument("--x", type=float, default=3.0, help="Enter the first number")
Similarly, we will create another argument like this
parser.add_argument("--y", type=float, default=1.0, help="Enter the second number")
Another argument will be passed in a form of operation which we wish to perform along 
with these two arguments --x and --y like this
parser.add_argument("--o", type=str, default="add", help="What do you want to do?")

So we will have three arguments inside main function like this

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=3.0, help="Enter the first number")
    parser.add_argument("--y", type=float, default=1.0, help="Enter the second number")
    parser.add_argument("--o", type=str, default="add", help="What do you want to do?")
    
There is one function parse_args() inside the class ArgumentParser() just like adding
argument function which is add_argument(self,argument,type,default,help) self is the
object of the class which is Parser.

So when we call this parse_args() function from the object Parser it will pack or parse
all the arguments inside one variable args like this

args = Parser.parse_args()

After that we will type this line sys.stdout.write(str(cal(args)) here sys.stdout.write()
prints the desired result or output on command line screen.

It takes input as a string version of the result of the function cal here inside cal we
pass argument as args which is a variable having a collection of command line arguments

( Jo bhi result aayega command line argument pass krne me variable args ki madat se cal
function se uska string version as an inpput leta hai sys.stdout.write isliye hum jo bhi
result aata hai or return hota hai function cal se usko str me type cast krte hai kyunki
sys.stdout.write print krta hai string version ko only )

We did not create cal function as of now so now we will create it and before that I would
say we have code like this inside main function now

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=3.0, help="Enter the first number")
    parser.add_argument("--y", type=float, default=1.0, help="Enter the second number")
    parser.add_argument("--o", type=str, default="add", help="What do you want to do?")

    args = parser.parse_args()
    sys.stdout.write(str(cal(args)))
    
Now this is the time to define or declare cal function like this

def cal(args):
    if args.o == "add":
        return(args.x + args.y)
    elif args.o == "sub":
        return(args.x - args.y)
    elif args.o == "mul":
        return(args.x * args.y)
    elif args.o == "div":
        return(args.x / args.y)
    else:
        return("Something went wrong")
        
Here we declare or define cal function which accepts positional argument as args
which is a variable having a collection of command line arguments which we had
passed using add_argument() so if args.o == "add" then return(args.x + args.y)
elif args.o == "sub then return(args.x - args.y) and if args.o == "mul" then
return(args.x * args.y) elif args.o == "div" then return(args.x / args.y) else
return("Something went wrong")


If we right click and run this code inside IDE like pycharm or IDLE by F5 so will
get an output corresponding to the default value which would be 4.0 so here we 
will pass argument from the cmd or window power shell ( Remember we will open
the same directory in command prompt in which directory our utility is present )
like this

C:/Users/Nitin Manali/PycharmProjects/FirstProg>python 72_Command Line Utility.py --x 5 --y 7.5 --o mul

Output : 37.5

If we call from cmd like this

C:/Users/Nitin Manali/PycharmProjects/FirstProg>python 72_Command Line Utility.py

Output : 4.0   ( If we do not pass command line argument so it accepts default value which
is 3.0 for --x and 1.0 for --y and operation --o for "add" )








"""



"""


Create a command line utility of faulty calculator program?


import argparse
import sys


def cal(args):
    if args.x == 45 and args.y == 3 and args.o =="mul":
        return(65.0)
    elif args.o == "mul":
        return(args.x * args.y)
    elif args.x == 60 and args.y == 10 and args.o =="div":
        return(4.0)
    elif args.o == "div":
        return(args.x / args.y)
    elif args.x == 65 and args.y == 7 and args.o =="add":
        return(73.0)
    elif args.o == "add":
        return(args.x + args.y)
    elif args.x == 39 and args.y == 13 and args.o =="sub":
        return(25.0)
    elif args.o == "sub":
        return(args.x - args.y)
    else:
        return("Something went wrong")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=3.0, help="Enter the first number")
    parser.add_argument("--y", type=float, default=2.0, help="Enter the first number")
    parser.add_argument("--o", type=str, default="add", help="Enter the first number")

    args = parser.parse_args()
    sys.stdout.write(str(cal(args)))

"""