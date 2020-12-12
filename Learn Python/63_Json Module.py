import json
import requests

# Employee = '''
# {
#     "People" : [
#         {
#             "Name" : "Nitin Sharma",
#             "Phone" : 2277772211,
#             "Email" : "s1950nitin@gmail.com",
#             "Salary" : 50000,
#             "Is_programmer" : true
#         },
#         {
#             "Name" : "Praveen Sharma",
#             "Phone" : 9876543210,
#             "Email" : null,
#             "Salary" : 30000,
#             "Is_programmer" : false
#         }
#         ]
# }
# '''

# print(type(Employee))
# dict = json.loads(Employee)

# print(type(dict))
# print(dict)
# print(type(dict["People"]))
# print(dict["People"])

# for item in dict["People"]:
#     del item["Salary"]
#     print(item["name"], ":", item["phone"])
#     for i, j in item.items():
#         print(i, ":", j)
#     print()

# print(dict)

# new_json_string = json.dumps(dict, indent=2, sort_keys=True)
# print(type(new_json_string))
# print(new_json_string)


# with open("data.json", "w") as f:
#     f.write(new_json_string)




# Separate code for load and dump functions is given below




# with open("data.json", "r") as f:
#     dict = json.load(f)

# print(type(dict))
# print(dict)
# print(type(dict["States"]))

# for item in dict["States"]:
#     del item["Area_codes"]
#     print(item["Name"], ":", item["Abbreviation"])
#     for i, j in item.items():
#         print(i, ":", j)
#     print()

# print(dict)


# with open("data1.json", "w") as f:
#     json.dump(dict, f, indent=2, sort_keys=True)




"""

Json : It is a data format for exchanging data between client and server ( Yaha client koi bhi ho 
sakta hai suppose we are accessing any url API from browser to make a request to the server and
getting a response from the server ).

It stands for Java Script Object Notation and it is language independent means this data can be
used by non python programming language too.

Earlier, we used to use data format xml for exchanging data between client and server and a few client
( any app or website) and server still uses the same concept  but json is getting popularity nowadays.


Why Json is getting famous ?

I will explain it with syntax of both xml and json data format

Json                                                        xml

{                                                
 "name" : "Harry",                                    </name>Harry<name/>
 "phone" : 12345,                                     </phone>12345<phone/>
 "salary" : 20000                                     </salary>20000<salary/>
}

In xml data format we are opening headers for each entries like name, phone and salary and then
closing the headers even so it takes more volume in spite of less volume is taken by json data
format

So, json is light weight data format that is the reason traffic does not face any congestion while
transmitting the data between client and server in json.



Now we will study why the syntax of json data looks like a python dictionary ?

Note : 

People think if we would be able to pass the string like data means plain text hello world my name
is Nitin Sharma that is not an issue to pass this data but we are living in object oriented world 
where data will be complex like name of the person then phone number then salary and much more if 
we take an example of employee detail of any organisation so it would be difficult for use to parse
such a long single string which will be containing so many useful information like ( Employee ka  
name, id, salary, department, email and etc).

That is the reason data is stored in json like a python dictionary in key value pairs data form
to parse it easily as we can parse python dictionary easily which we have learnt so our motive
will be here to get the json data either it is in form of json string or json file and then convert
it into the python object in terms of dictionary which will be parsed easily in python.


For example :

data = '{"Harry" : 2, "Larry" : 4, "Carry" : 8, "Marry : null}'

data1 = {"Harry" : 2, "Larry" : 4, "Carry" : 8}

print(type(data))    Output : class str  (Python string which holds json data jo parse nahi ho sakta)
print(type(data1))   Output : class dict (Ye python dictionary hai which can be parsed easily )

print(data1["Larry"])  Output : 4
print(data["Larry"])   Output : Error as str must be indices as integer (Ye string hai not a dict)




Json data looks like a python dictionary but it is quiet different so we will learn how it is
different from a python dictionary.

1) In python, we have boolean True and False but in json we have boolean true and false means in
lower case.
2) We have None keyword in python similarly we have null in json.
3) In python, we have list [], in json we have array []




In python, json is a built in library or module which has 4 major functions :

1) loads : It is used to load or convert json data in a form of string to python dictionary.
2) dumps : It is used to dump or convert python dictionary to json data in a form of string.
3) load  : It is used to load or convert the json file into a python dictionary.
4) dump  : It is used to dump or convert python dictionary to json file.


Load or loads : Both comes under the process of deserialization when we make json data either
in a form of string or file to python dictionary which can be parsed easily.

Dump or dumps : Both comes under the process of serialization when we python dictionary to
string in a form of json data or a file.




In above approach, we have a json data in a form of string means json string Employee which
contains json data under {} as an object People which is an array [] in which have objects Name,
Phone, Email, Salary and Is_programmer under {} as we know json format is defined under {} and
we used ''' at the beginning and ending ''' because it is a multi line json string.

We know we face difficulties to parse a long string so we will change this Employee which is json
string to python dictionary now if print print(type(Employee)) before changing it into python
dictionary so it will give output class str which is json string.

Here, we will create a variable dict = json.loads(Employee) due to which this json string will be
converted or loaded into dict as a python dictionary so if we print print(type(dict) so output
would be class dict that is python dictionary and if we print print(dict) so python dictionary
will be printed in output and if we print(type(dict["People"]) so will get an output as class str
and if we print print(dict["People"]) so will get list items which are two python dictionaries 
which contain object Name, Phone, Email, Salary, Is_programmer in {} separately.

As we know dict["People"] is a list so we will apply for loop here like

for item in dict["People"]:
    del item["Salary"]
    print(item["name"], ":", item["phone"])
    
So both the list items of list dict["People"] which are two dictionaries separately in {} will be
coming into item and then del item["Salary"] so it will delete entry of "Salary" from both the
dictionaries and then printed print(item["name"], ":", item["phone"])

Output : 
Nitin Sharma : 2277772211
Praveen Sharma : 9876543210

if we type like this 

for item in dict["People"]:
    del item["Salary"]
    for i, j in item.items():
        print(i, ":", j)
    print()
    
Here, we are printing both the dictionaries object in a form of key value pairs along with unpack
except the entry of "Salary" in both the list items which are separate dictionaries stored in {} 
which we have deleted.

then printed print(dict) so will get an output as a dictionary which will have key "People" which
is further a list containing two list items in a form of dictionaries containing object Name, Phone,
Email, Is_programmer except one entry from both the list items which are separate dictionary of 
"Salary".

Now, created one new variable new_json_string which looks like

new_json_string = json.dumps(dict, indent=2, sort_keys=True)
print(type(new_json_string))
print(new_json_string)

Due to which our dict which is python dictionary which has one less entry of object "Salary" in key
"People" which is a list of two separate dictionaries will be dumped or converted into json string
new_json_string so if we print print(type(new_json_string)) so will get an output class str which
is json string and if we print print(new_json_string) so will get an output in console as a json
data string which is not much look easy to read so to make it readable in a form of human readability
we pass indent = value so we will get an output looks like data format form of json which comes under
{} and if we pass one more argument sort_keys=True in json.dumps like we passed indent = 2 so it
just prints the output the data of a json string in an alphabetical order.



We can also forward the json data in a form of string into a json file like

with open("data.json", "w") as f:
    f.write(new_json_string)
    
Here, we opened up one file "data.json" in a write mode and then write it as f.write(new_json_string)
so whatever content would be in json string new_json_string will be forwarded or copied into a file
naming data.json.







Now we have another approach in which we have one json file naming "data.json" in which have data
in {} which contains one object "States" which is an array which has two further json objects 
separate which come up in {} containing json objects Name, Abbreviation, Area_codes, Budget

so we opened up this file like 

with open("data.json", "r") as f:
    dict = json.load(f)
    
Due to which whatever json data is present inside the json file "data.json" will be changed or
converted into a variable dict as a python dictionary which can be parsed easily now.

if we print print(type(dict)) so will get an output class dict which is a python dictionary and
if we print print(dict) so will get an output as a python dictionary and if we print key of dict
which is "States" like print print(dict["States"]) so will get an output as a class list.

As we know dict["States"] is a list which has two list items as two dictionaries which are separated
and containing objects Name, Abbreviation, Area_codes and Budget so we will use for loop now like

for item in dict["States"]:
    del item["Area_codes"]
    print(item["Name"], item["Abbreviation"])
    
Here, we are passing list items of list dict["People'] into item which are further two dictionaries
so deleted del item["Area_codes"] it will delete Area_codes entries from both the list items then
print(item["Name"], ":", item["Abbreviation"]) so we will get an output which will look like

Output :
New Delhi : ND
Haryana : HR
Rajasthan : RJ
Uttar Pardesh : UP
Uttarakhand : UK

if we print code like 

for item in dict["States"]:
    del item["Area_codes"]
    for i, j in item.items():
        print(i, ":", j)
    print()
    
Here, we are printing both the dictionaries (list items) in a form of key value pairs along with unpack
except the entry of "Area_codes" in both the list items which are separate dictionaries stored in {} 
which we have deleted.

then printed print(dict) so will get an output as a dictionary which will have key "States" which
is further a list containing two list items in a form of dictionaries contains object Name, Abbreviation,
"Budget" except one entry from both the list items which are separate dictionaries of "Area_codes".


Now we opened up a new file "data1.json" as a write mode like

with open("data1.json", "w") as f:
    json.dump(dict, f, indent=2, sort_keys=True)
    
Due to which we are just importing or dumping the python dictionary dict into a new json file
"data1.json" so here in json.dump() first argument would be the python dictionary which we need
to dump into a json file "data1.json", second argument would be json file "data1.json" which we
have opened up for writing mode as f so python dictionary will be dumped into this new json file
however if we open up the file "data1.json" by clicking on it so it is not in easy representation
to read by a human as we know how to make it readable by a human by using indent = value which we
has learnt earlier and if we pass another argument sort_keys = True in dump function as we passed
indent = 2 so it will sort the objects of json data in a json file "data1.json" as in alphabetical
order.


   
"""



"""

To use quandl.com we need to sign up into quandl.com for free data and once we register into it
so it gives one unique API key to us : ARuyvUdN1pxnYyyu7L-x and whatever email address we had 
provided at the time of signing up would be your username and password would be password which
ypu had created at singing up an account on quandl.com

My quandl credentials are :
    Username : s19nitin@gmail.com
    Password : IPLUAE@2020

 


Now, we will use quandl.com which has lots of free data in a form of xml, csv, json  format so we 
will use url API of json data of quandl.com by using a library or module requests in python and will
play with quandl json data with the help of json module in python that will be something like
we are playing with json data in a corporate or professional life.

How to get url API of json free data in quandl.com that is for real life professional work which
we will be doing in corporate sector ?

First you will need to visit https://www.quandl.com/ then click on tab EXPLORE or we can also type
free data in search box so if we click on table EXPLORE then we will get at top left there will be
two filters Premium and the other is Free so we will check mark on Free then we will get free 
Featured Data so there will be first indexing like Wiki Continuous Futures once we click on Wiki
Continuous Futures so we will lots of free data in a tabular form like

Minneapolis HRWI Hard Red Wheat Futures, Continuous contract #1 [IH1] [Front Month]        EXPAND

When we click on this EXPAND so it will direct us to new web page where we will get graph appears
of our data and in this page at the top right side we will get API url of JSON, CSV, XML data under
EXPORT DATA so once we click on JSON under EXPORT DATA under API so we will get url API of JSON data
for Minneapolis HRWI Hard Red Wheat Futures, Continuous contract #1 [IH1] [Front Month]


url = https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=ARuyvUdN1pxnYyyu7L-x


So we will play with json data of quandl.com related to Minneapolis HRWI Hard Red Wheat Futures, 
Continuous contract #1 [IH1] [Front Month] which we got via above url API now by following code
which is given below :






# r = requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=ARuyvUdN1pxnYyyu7L-x")
# print(r.text)


# with open("quandl_data.json", "w") as f:
#     f.write(r.text)


# json_string = r.text
# print(type(json_string))

# dict = json.loads(json_string)
# print(type(dict))
# print(dict)

# print(type(dict["dataset"]))

# dict["dataset"]["Programmer"] = "Nitin Sharma"


# for item in dict["dataset"].items():
#     print(item)


# quandl_json_string = json.dumps(dict, indent= 2)
# print(type(quandl_json_string))
# print(quandl_json_string)

with open("quandl_data.json", "r") as f:
    dict = json.load(f)

# print(type(dict))
# print(dict)

# for item in dict["dataset"].items():
#     print(item)


# with open("quandl_data.json", "w") as f:
#     json.dump(dict, f, indent=2, sort_keys=True)



"""















