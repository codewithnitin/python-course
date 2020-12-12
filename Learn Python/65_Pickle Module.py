import pickle

# My_cars = ["BMW", "Audi", "Mercedis Benz", "Wolksvogen"]

# python_bytes = pickle.dumps(My_cars)
# print(type(python_bytes))
# print(python_bytes)

# My_cars_list = pickle.loads(python_bytes)
# print(type(My_cars_list))
# print(My_cars_list)

My_dict = {"Harry" : "chole bhature", "Larry" : "pizaa", "Carry" : "burger"}

# python_bytes = pickle.dumps(My_dict)
# print(type(python_bytes))
# print(python_bytes)

# My_python_dict = pickle.loads(python_bytes)
# print(type(My_python_dict))
# print(My_python_dict)

# for item, lollypop in My_python_dict.items():
#     print(item, ":", lollypop)




# Code for separate functions of pickle module load from a file or dump to a file



# with open("data.pkl", "wb") as f:
#     pickle.dump(My_dict, f)

# with open("data.pkl", "rb") as f:
#     Required_dict = pickle.load(f)

# print(type(Required_dict))
# print(Required_dict)




"""

pickle module : It is a built in python module which is used to pickle the python objects like
string, list, dict or any class object etc as we know everything is just an object in python.

( Pickle karke object ko rakhna kuch esa he jaise real aachar ko hum preserve karke rkhte hai
jab khaana ho toh dabe me se nikal ke enjoy krte hai )

It has four functions which are given below :

1) loads : It is used to load or convert the bytes ( binary data ) into python objects for parsing.
2) dumps : It is used to dump or convert the python objects into bytes ( binary data ).
3) load : It is used to load or convert the bytes ( binary data ) from a file to python objects for
parsing.
4) dump : It is used to dump or convert the python objects into a file as a binary data.

Loads or load : Both comes under the process of deserialization or unpickling.
Dumps or dump : Both comes under the process of serialization or pickling.





Difference between JSON module or Pickle module :

               Pickle                                        Json
       
1) It is used to convert all the python          1) Json stands for Java Script Object Notation which
   objects ( string, list, dict, class,             is used to convert python dictionary mainly into
   methods ) into bytes (binary data).              string which contains json data which looks like
                                                    a python dictionary.
                                                    
                                                    (Json convert aur bhi python objects kar sakta
                                                    hai par unka output dictionary jaisa nhi hoga
                                                    jo json data jaisa look nhi dega jo ki dictionary
                                                    sa hota hai)
       
       
2) Pickle lets the user to store data            2) Json lets the user to store data in a human
   in a binary format.                              readable format which is text.

3) Pickle can be used for serialize &            3) Json is limited to a certain objects as classes
   deserialize all the python objects.              & methods are not serialized or deserialized.
                                                     
4) Pickling is specific to python only           4) Json is supported by almost all the programming
   and it does not guarantee cross   -              languages.
   language compatibility.                          Json is language independent.
   Even diff python versions are not                So even a non Python programmer can use this for
   compatible with each other. It means             data interchange.
   pickling done in python version 2.x
   may not work in python version 3.x                   
                        
                                              
5) There is always a security risk with          5) There are no loopholes in security using JSON &
   Pickle.                                          is free from security threats.
   Unpickling data from unknown sources 
   should be avoided as it may contain 
   malicious or erroneous data.                                            
                                            
     
     
                                            
"""










