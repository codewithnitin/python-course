

import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

Meta characters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

321-555-4321
123.555.1234
231*444*3421
810-444-3421
900-444-3421
543--32-2341
657**45*3241
854..23.7652

cat
mat
pat
bat


Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

Sentence = "Start a sentence and then bring it to an end"

url = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


# pattern = re.compile(r'abc')
# pattern = re.compile(r'.')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\S')
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')
# pattern = re.compile(r'^Start')
# pattern = re.compile(r'nd$')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'\d\d\d[-.][-.]\d\d.\d\d\d\d')
# pattern = re.compile(r'[89]\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-zA-Z0-9]')
# pattern = re.compile(r'[^a-zA-Z0-9]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'\w+[-.]?\w+-?\w+@\w+-?\w+\.(com|edu|net)')
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# pattern = re.compile(r'https?://[a-z.]*\w+\.\w+')
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# matches = pattern.finditer(text_to_search)

# matches = pattern.finditer(Sentence)

# matches = pattern.finditer(url)


# with open("People_fake_data.txt", "r") as f:
#     content = f.read()
#
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# matches = pattern.finditer(content)
#
# for match in matches:
#     print(match)

# pattern = re.compile(r'.91-\d\d\d\d\d\d\d\d\d\d')


# for match in matches:
#     print(match)
    # print(text_to_search[1:4])


pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', url )
print(subbed_urls)









"""

Regular Expression : It is the technique by which we can get useful information or search
for match specific pattern from the string or text file.
It is also known as regex and we have built in module re in python for regular expression.


First of all we will know what is raw string as we will be using raw string through out
in regex.

Suppose we print print("\tTeb") so output would be    Tab there will be a tab in console
due to this \t which is escaoe sequence character in python so if we wish not to escape
this \t in output so we can use raw string like print(r"\tTab") now output would be \tTab.

There is a method or function called re.compile() in regex which is used to separate our
pattern into a variable like

pattern = re.compile(r'abc') 

It means we are looking for the pattern r'abc' now we will apply finditer() method on the
variable pattern here finditer() will iterate the string for searching match for required
pattern like this

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
    
Here for loop will find out how many match we have for the required pattern in matches.

Output would be :

<re.Match object; span=(1, 4), match='abc'>  only one match as abc present in the string
text_to_search for only once and span would be index of beginning and ending of match.

So if we print print(text_to_search[1:4]) so output would be abc and note we we had pattern
of abc in spite of ABC or cba like that so if we have pattern re.compile(r'cba') so we will
not get any output as we do not get this match in string or pattern re.compile(r'abc') still
not search as it is case sensitive too so whatever would be the pattern if it finds out in
the string so will return the output otherwise no output will be come up.



If we will have a pattern re.compile(r'.') so it will give match of all the characters in
the string text_to_search except new line and this single . is known as period.

So if we wish to print it all the match for this single . so we will use \ before . like \.
in our pattern re.compile(r'\.')

Example : if we have a pattern re.compile(r'coreyms\.com') so output would be coreyms.com

Now comes to \d it gives all the match for digits (0-9) only so if we will have pattern
re.compile(r'\d') so outout would be all the match for digits only.

If we will have pattern re.compile(r'\D') means we will have output along with all the 
match except digits means ( Not a digit )

If we have a pattern re.compile(r'\w') so output would be all the match for a-z,A-Z,0-9,_ 
means lower case alphabet or upper case or any digit and under score as well.

If we have pattern opposite of it means re.compile(r'\W') means output would be all the
match for those which are not a-z, A-Z , 0-9 and _

If we have a pattern re.compile(r'\s') so output would be all the match for spaces, tabs
and new lines which all comes under whitespace in the string text_to_search

If we have opposite pattern like re.compile(r'\S') so output would be all the match for
those which are not whitespace ( spaces, tabs and new lines )



Now we will study about anchors which do not match any character but invisible positions
before or after the characters and Anchors are \b, \B, ^ is known as carrot and $

Let us take a example of word boundary \b which is included by whitespace (spaces, tabs,
new lines) and non alphanumeric.

If we have a pattern re.compile(r'\bHa') so output would be two Ha first at the beginning
of the new line Ha and after that second Ha which have space just before it.

If we have pattern opposite of this pattern like re.compile(r'\BHa') so output would be 
one match of Ha which has no word boundary.



Now we will use the Sentence = "Start a sentence and then bring it to an end" to learn
^ carrot which is starts with if we are searching the string from which character or
word our string starts up and $ dollar sign means endswith if we are searching match from
which character or word our string ends with.

If we have a pattern like 

pattern = re.compile(r'^Start')
matches = pattern.finditer(Sentence)

for match in matches:
    print(match) 
    
so output would be one match as our string Sentence starts up with the word Start

If we will have a pattern re.compile(r'nd$') so output would be one match as our string
Sentence ends with nd and if pattern would be re.compile(r'a$') so no output will be come
up as our string Sentence does not endswith character a.


Now we will use our previous text_to_search multi line string so we will change it likt
matches = pattern.finditer(text_to_search)

Now we will write a pattern for searching match for phone numbers which are present in
our text_to_serach like this


pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') so output would be all the matches for
phone numbers which are present under text_to_search and now we have one file which has
details of several person along with their names, addresses, phone numbers and emails
so we will open that file first and will read the content of that file to find out all
the phone numbers.

Here we opened up the file People_fake_data which has fake data of random people along
with their names, phone numbers, addresses and emails and then set a pattern to find out
all the phone numbers of that file like this

with open("People_fake_data.txt", "r") as f:
    content = f.read()

pattern = re.compile(r'.91-\d\d\d\d\d\d\d\d\d\d')

matches = pattern.finditer(content)

for match in matches:
    print(match)
    
So output would be all the match for phone numbers of this file and now I will comment
out this file code and will open up our multi line string text_to_search. 


If we use a pattern pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') so it will give
output of all the match related to phone numbers under a string text_to_search however
if we wish to get only those numbers which are separated by - and . instead of * so
we can use character set [] so pattern would be now like this

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') so output would be two match of
phone numbers which are separated by - and . instead of *

Note : 

Inside character set [-.] we do not need of any backslash to show . as we need to use 
it to escape period with the help of backslash outside character set and it picks up
only one character - or . in this case.

Suppose we have [a-zA-z0-9-.] so character set picks up only one
character at a time out of lower case or upper case letters or digits or - or . etc.


If we use dash - inside a character set like [-.] so it means character would be - or .
however if we use dash - between values in character set so gives range like [a-zA-z0-9]
so character would be any lower case between a to z or upper one A to Z or digits 0 to 9

If we put carrot ^ inside a character set like this [^a-zA-Z0-9] it will give output
for all those match which are not in a range of a to z or A to Z or 0 to 9



Example if we have a phone number 543--32-2341 and we are using the same above pattern
so it will pick up match for phone numbers which are separated by - and . only instead
of -- as in our pattern in place of second dash there must a digit.

so if we wish to search for a match this phone number 543--32-2341 so pattern would be
like

pattern = re.compile(r'\d\d\d[-.][-.]\d\d.\d\d\d\d')

Suppose if we have to find out only those numbers which are starts from 8 or 9 so how 
will we do that

pattern = re.compile(r'[89]\d\d.\d\d\d.\d\d\d\d') so we will get output as in match for
only those phone numbers which starts from 8 or 9


If pattern would be re.compile(r'[1-5]') so output would be match for all the digits 
inside this string which comes up in a range of 1 to 5

Similarly, if pattern would be re.compile(r'[a-zA-z0-9]') so output would be all the
match for any lower case a to z or upper case A to Z letter  or any digit 0 to 9

If we have a pattern like pattern = re.compile(r'[^a-zA-Z0-9]') it will give output 
for all those characters which are not in a range of a to z or A to Z or 0 to 9

Example :

Suppose we have word cat, mat, pat and bat in our string text_to_search and we wish
to get all the match for cat, mat, pat but not bat so pattern would be like

pattern = re.compile(r'[^b]at') it will give output all the match for cat, mat, pat
instead of bat.



We will study Quantifiers now which are *, +, ?, {n}, {n1,n2} which is very useful
while creating pattern in a shorter way.

Suppose we have a same pattern to search mobile numbers which is given below :

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') so here we are using \d multiple times
instead of this we can use quantifiers {} with exact number so pattern would be

pattern = re.compile(r'\d{3}.\d{3}.\d{4}') so output would be same all the match which
we were getting with the code pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') and this
will helpful for us to avoid the mistakes while entering \d in an exact numbers.


Now I will take an example of names which we have in our string text_to_search

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') it will give output for all the match
for names present in the string text_to_search.

Here, we could have used M[rs] so it gives Mr and Ms but not Mrs that is the reason
we used a group M(r|s|rs) or M is also common in all so we can write (Mr|Ms|Mrs) after
that we put \. to get period . but now the question is we need . in some title and
not in some so we can do it with the help of another quantifier ? which allows 0 or 1
means whatever would be prefix in front of quantifier ? that can exit once or sometimes
not so \.? will give single . sometimes and sometimes not then we put \s to get a space
then used a character set [A-Z] which returns any character in a range of A to Z to 
start first letter of names with Caps and then we need lower case characters which we
can get by applying \w but it will give one character in a range of a-z and we want 
more and sometimes not for Mr.T so we can apply quantifier just after \w* which allows
0 or More and if we use \w+ so it does not give the match of Mr. T as it does not have
any lower case letter so we used \w* instead of \w+


Now I will also take an example of some emails which are present in multi line string
text_to_search so we will write a pattern to get all the match for emails like

pattern = re.compile(r'\w+[-.]?\w+-?\w+@\w+-?\w+\.(com|edu|net)')

Here we put \w along with quantifier + like \w+ it means starts with any lower or upper
case characters and more on then we put character set [-.]? means sometimes we want 
either - or . or sometimes not as it allows 0 or 1 then we put \w+ to get any lower or
upper case or digit & more on then put dash -? means sometimes we want dash or sometimes
not then we put \w+ means want lower or upper case character and more on then @ then we
put \w+ to get character in terms of lower or upper case letters and more on then put -?
means we want dash sometimes and sometimes not then we put \w+ to get lower or upper case
letter and more on and then put a period by \. then a group of (com|edu|net)

so above pattern will give us an output for all the match which are related to emails.


Note : Universal pattern for email :

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

Now we opened up a file People_fake_data.txt in r mode and read the content of a file
and save into a variable content and then applied a method finditer to iterate content
to search the all the match for above required pattern by using for loop like this

with open("People_fake_data.txt", "r") as f:
    content = f.read()
    
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(content)

for match in matches:
    print(match)
    
Output : Would be all the match for emails which are present in the above file.



We know how to use group to match several patterns and now we will study how we can
capture information from group like domain name along with top level domain only
instead of full urls like
google.com
coreyms.com
youtube.com
nasa.gov


Here we will use one multi line string url which is present above and to get output
for all the match of urls which are present inside multi line string would be

pattern = re.compile(r'https?://[a-z.]*\w+\.\w+')
                
                OR 
                
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(url)
for match in matches:
    print(match)
    
    
Here we will have output all the match for above urls but our goal was to get only
domain and top level domain like
google.com
coreyms.com
youtube.com
nasa.gov

So here we will do grouping of domain name (google,youtube,coreyms,nasa) and top 
level domain name (.com,.com,.com,.gov) like this

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(url)
for match in matches:
    print(match)
    
As of now output will be same which are all the match of entire urls even we have
done grouping here.


Here, we have one group which is optional (www.)? indexing 1 and another domain 
group (\w+) indexing 2 and top level group (\.\w+) indexing 3 and group index 0
would be the entire url or pattern.

Here, match object has method group inside so we can use it like this

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(url)
for match in matches:
    print(match.group(0))     Output : All the match for entire urls
    print(match.group(1))     Output : All the match for optional group (www.)?
    print(match.group(2))     Output : All the match for domain group
    print(match.group(3))     Output : All the match for top level domain group
    
    
We have separated the urls in group(0) for entire urls, group(1) for optional group
and group(2) for domain group and for top level domain group (3) however we were 
looking for domain name along with top level domain name.

To get back references or substitution of groups from entire body or urls we use 
method sub() in place of finditer() like this

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', url )
print(subbed_urls)

Here, we created pattern only pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
and then we used sub() method to substitute groups from entire pattern or urls by
subbed_urls = pattern.sub(r'\2\3', url ) here \2\3 are group 2 and group3 which we
are finding out from url variable which consists urls so if print print(subbed_urls)

Output would be like :

google.com
coreyms.com
youtube.com
nasa.gov

This is what we were looking for.





"""




    





























