mystr = "Nitin is a technical guy"

# print(mystr)       # It prints the the variable content
# print(type(mystr)) # It shows class of the variable
# print(len(mystr))  # It shows length of the variable content and it always starts from 1

"""
# String Slicing :

print(mystr[4])      # It prints only 4 indexing character of the string.
print(mystr[0:5])    # String slicling has a rule to execute code by [include : Exclude by 1]
print(mystr[:])      # By default include 0:so on till full string completion
print(mystr[:24])    # By default include 0:so on till full string completion exclude by 1 indexing
print(mystr[0:])     # Inculde 0 : so on till full string completion
print(mystr[0:50])   # Inculde 0 : so on till full string completion and avoid after that as no characters present
print(mystr[0:5:])   # No change in output as previous one [include : Exclude : ] last : for skipping the string
print(mystr[0:5:1])  # No change in output as previous one [include : Exclude : 1] last :1 exclude by 1
print(mystr[0:5:2])  # Skipping will be done by 1 character
print(mystr[0:5:3])  # Skipping will be done by 2 character
print(mystr[0:5:90]) # It will reflect include 0 character and after that 89 characters cannot be jumped as total
#of 4 characters length
"""
"""
print(mystr[-3])       # It shows negative indexing -3 character in output
print(mystr[-24:])     # It shows the full string.
print(mystr[-13:-4])   # Include -13 : Exclude by 1
print(mystr[-13:-4:])  # No change in output as previous one [include : Exclude : ] last : for skipping the string
print(mystr[-13:-4:1]) # No change in output as previous one [include : Exclude : 1] last :1 exclude by 1
print(mystr[-13:-4:2]) # Skipping will be done by 1 character
print(mystr[::-1])     # It reveres the string
print(mystr[::-2])     # It reveres the string along with skipping by 1 character
print(mystr[-5:-14:-2]) # It reveres the string -5 include :-14 exclude by -1 along with skipping by 1 character 
"""
"""
Boolean function : It gives output in True or False

# print(mystr.isalnum())       # isalnum detects alphanumeric string if gets so output True otherwise False.
# print(mystr.isalpha())       # islpha() detects alphabets only if gets so output True otherwise False.
# print(mystr.endswith("guy"))    # If endswith("last word") so output True otherwise False.
# print(mystr.startswith("Nitin"))    # If startswith("First word") so output True otherwise False.
"""
"""
Functions in string :

print(mystr.capitalize()) # capitalize() gives capital letter to the first alphabet of first word of string.
print(mystr.find("technical")) # find() provides the indexing number where word starts up in the string.
print(mystr.lower()) #lower() lowers up the string.
print(mystr.upper()) #upper() uppers up the string.
print(mystr.replace("technical","good")) #replace() it replaces the word in the string.
print(mystr.count("i")) Count() shows how many repeation of the character which we want to search in string.

"""





