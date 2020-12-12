"""

Python is a multi paradigm programming language means it supports several techniques or
approaches like object oriented programming (OOPS)


Introduction of OOPS :

Object oriented programming is a way of programming by which we obtain objects.

What doest it mean exactly ? Will clear it below

Classes = Template

Object = Instance of the class (Template ko input details se bharna phir jo mile woh object)

Example : If we are banker and customers are coming to us one by one for several things
like entry to the passbook or asking etc so we will have one template in which we will
have Sole/Account holder name, Account number etc already written so we will input
customer's name and account number of the customer only in spite of creating the full
document like

Sole/Account holder name : "name"
Account number           : 9876543210000

Once we enter with the following details so we will get all the details of the particular
customer and can take the print out of the information to pass it to the customer and
same will be doing with the next customer and so on.

Here, we had one template in which we input details of the customers so whatever information
or output we get is the object of that class

That is known as object oriented programming means to perform operation in an organised
form or way

Example 2 : Making movie

Here script would be template or class and when we obtain video of that movie by acting
and everything so video is the object.

Example 3 : Writing a letter for taking leaves

Here, we will have template of letter where thanks and regards or you are highly obiliged
already written so we will have blanks where we need to input person name who is going on
leave and blank for period of leave (No. of days) so whatever output we get as a complete
letter is the object

Why do we create class ?

1. DRY ( Do Not Repeat Yourself ) as class works on the concept of DRY

Ex : Suppose we are writing a letter in which it is clearly mentioned as this letter is
only applicable for 100 characters so if we will have template of that letter in which
this line is already written like this letter is only applicable for 100 characters so
we will no need to write it due to which we will save time, money and efforts.

Now question is how money ? Time is also money ( Samay se balwan koi nahi )

2. Restricting access of functions under class

Ex : Suppose we have one function def get_no._of_films(Actor name) which tells which actor has
made how many movies so when we input argument as an actor name so it will tell no. of films
count of that actor accordingly and if we provide invalid input youtuber name or sports men
name so we will get output zero as youtuber makes videos and sports men play sports

Here we wish to restrict access of this function for film stars only so what we will do?

We will create one class name Film in which we will write this def no._of_films(Actor name)
means we are defining or declaring this function under class Film which needs of this function
only this is how we will restrict the access of function with the help of class



"""

