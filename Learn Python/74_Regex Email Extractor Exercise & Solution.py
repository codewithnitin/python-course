# Excersie on Regex ( Find out email addresss from a given string using regex and
# save them to the file )

import re

str = '''

It was during a visit to Prague that a besotted Henry, 61, pursued her with a string of emails and phone calls.

In a string of emails and memos, senior Farc officers reported that the Venezuelan government had offered hundreds of millions of dollars to buy weapons.

Embarrassment for  surajthapafc@gmail.com the governo mynigga@yahoo.com r grew when the biggest newspaper in South Carolina, The State, published a string of emails between him and his lover.

Robert Booth of the Guardian reports: The fc@abc.com string of emails between Akhras and Assad over a nine-month period appear to show that the doctor was particularly concerned about how better to present the regime's actions internationally.

Ed Miliband, the former climate change secretary, said: "Muir Russell has given the world a clear message: we should not believe those who tell us that one string of emails undermines years of climate science. "


'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(str)

for match in matches:
    print(match)

with open("Email_Extracter.txt", "a") as f:
    f.write(f"email1 : {str[289:311]}\n")
    f.write(f"email2 : {str[324:341]}\n")
    f.write(f"email1 : {str[505:515]}\n")

with open("Email_Extracter.txt", "r") as f:
    print(f.read())