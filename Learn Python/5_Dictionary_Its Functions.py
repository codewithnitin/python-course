# Dictionary is nothing but key value pairs.

"""
d1 = {"Nitin":"Burger",
      "Praveen":"Pepsi",
      "Pandey":"Chole bhature",
      420:50.5,
      "Piyush":{"B":"Dosa","L":"Dal Rice","D":"Salad"}}
"""
#print(type(d1))
#print(d1)
#d1["Anoop"] = "Pranthe"          #Adding item or element in the dictionary.
#d1[555] = 200                    #Adding item or element in the dictionary.
#del d1[420]                      #Deleting item or element in the dictionary.
#print(d1)                        #Printing item or element in the dictionary.
#print(d1["Piyush"]["L"])         #Printing output of item or element in the dictionary.
"""
d2 = d1                           d2 & d1 are pointers here which means d1 is not copying in d2 yet.
del d2["Pandey"]                  It deletes the element ["Pandey"] from the original d1 as well.
print(d1)
"""
#To avoid this we use copy() function :

#d2 = d1.copy()                   #Copying the items or elements of d1 dictionary into d2 variable.
#del d2[420]                      #Deleting [420] from d2 only so original d1 wil remain same ( No change occurs)
#print(d1)
#print(d1.get("Piyush")["L"])     #Printing output of item ["Piyush]["L] via get() function
#d1.update({"Sahil":[1,5,10]})    #Updating new item or element {"Sahil":[1,5,10]} via update() function
#print(d1)
#print(d1.keys())                 #Keys() shows keys in the dictionary.
#print(d1.items())                #items() shows key value pairs in the dictionary

# Exercise1 : Creating a dictionary via input from user

"""
d1 = {"Abandon":"Stopped", "Thrash":"Destroy", "Mutable":"Can change", "Immutable":"Cannot change"}
print("Enter your word")
n1 = input()
print(d1.get(n1))
print("You entered", d1[n1])
"""

