# Pip install requests

import requests

# r = requests.get("https://xkcd.com/353")
# print(dir(r))
# print(r.text)
# print(r)
# print(r.status_code)
# print(r.ok)
# print(r.headers)



# r = requests.get("https://xkcd.com/353/123")
# print(r.status_code)
# print(r.ok)




# r = requests.get("https://imgs.xkcd.com/comics/python.png")
# print(r.content)

# with open("C:/Users/Nitin Manali/PycharmProjects/FirstProg/comic.png", "wb") as f:
#     f.write(r.content)



# payload = {"page": 2, "count": 25}
# r = requests.get("https://httpbin.org/get", params=payload)
# print(r.text)
# print(r.url)


# payload = {"username": "Nitin", "password": "testing"}
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)
# print(r.url)
# print(r.headers)
# print(r.json())
# r_dict = r.json()
# print(r_dict["form"])




# r = requests.get("https://httpbin.org/basic-auth/Nitin/IPLUAE@2020", auth=("Nitin","IPLUAE@2020"))
# print(r.text)







"""

Request module : HTTP for humans


It is designed to make http requests via programmatically to get the useful information from the websites
or web pages.

It is developed by a person Kenith Reitz and he has made one website https://httpbin.org for testing 
purpose for these get, post, auth (basic authentication requests) etc using this request module.



Get request : This is used to get information or content of a particular website or web page.

In above approach we imported a library or module request then we used the url of a comic xkcd website 
which is given below :


url : "https://xkcd.com/353"

Syntax of get request :

r = requests.get("https://xkcd.com/353")

Here, r is the response object as we requested the url https://xkcd.com/353 so if we print print(dir(r))
so we will get a list of attributes, methods which we can use within this response object.

print(r.text) : It gives content of the above url in unicode means source code of the web page which comes
up in html coding.

print(r) : It gives output response with status code so if our request hits on correct url so we will get
output response 200, sometimes it comes up with response 300 which means re-direct, 400 means client error
and 500 means server error.

Print(r.status_code) : It gives output just as 200 if request goes successfully.

So, in above url we will get output 200 if we print print(r.status_code) as it is correct url so we will
get response successfully.

print(r.headers) : It gives a dictionary in which we get {"server" : ******, "last modified time" : ******,
Content/Type : Text/html and so on } of the above url. ( Kaunse server ko use krke url bana hai, kya
type ka content hai,kb last modify hua ye web page and etc etc.)

print(r.ok) : It gives output True or False when our status code of the url is below 400 so we will get
output True and if we get status code equals to 400 or more so will get an output False.

Due to which as our url is correct we will have status code 200 here because our request will be going on
successfully to get response back if we print print(r.status_code) so output would be True for print(r.ok).




Suppose we are requesting this url r = requests.get("https://xkcd.com/353/123") with the help of get request
of module request as we know this is not found our invalid url r = requests.get("https://xkcd.com/353/123")
so if we print print(r.status_code) so will get an output 404 due to not found or invalid url client error
and if we print print(r.ok) here so output would be False which we had learnt just above.




Now we will study how we can download images like jpg or png via programmatically using python with the
help of get request of module request

r = requests.get("https://imgs.xkcd.com/comics/python.png")
print(r.content)


here we are requesting the above url with the help of get request of module request so if we print
print(r.content) so we will get the output in bytes as images are made up with the bytes code (
Matlab binary code ).


r = requests.get("https://imgs.xkcd.com/comics/python.png")
with open("C:/Users/Nitin Manali/PycharmProjects/FirstProg/comic.png", "wb") as f:
    f.write(r.content)
    
    
Here, we requested the url https://imgs.xkcd.com/comics/python.png then opened up a new file in a location
"C:/Users/Nitin Manali/PycharmProjects/FirstProg/comic.png" in write byte mode the write the file with
response object in bytes with the help of r.content like f.write(r.content)

Due to which there will be a new file come up of comic.png and when we click on it to open up so we will
get the same image which is associated with this url so this is how we download the image programmatically
in python.

NOTE : if we open file like with open("comic.txt", "wb") as f: so file will be created into the same
directory or folder where our request module is saved or stored that is the reason we specify the full
path location where we want this file.




Now, we will study how to pass parameters along with url as sometimes we route some of the websites which
has parameters in url so we will also do it with the help of get request of module request.

Here, I will use url https://httpbin.org which is designed by Kenith Reitz for testing these request
module request like get,post,auth etc.


r = requests.get("https://httpbin.org/get?page=2&count=25") this is how we pass parameters to the url
but it occurs some mistakes and we cannot afford it so we will pass the parameters wth the help of
dictionary here like this.


so syntax would be :

payload = {"page": 2, "count": 25}
r = requests.get("https://httpbin.org/get", params = payload)
print(r.text)

Here, we created a dictionary payload which has two parameters page = 2 and count = 25 and then we 
requested the above url along with passing parameters like params = payload and then we print print(r.text)
so we will get an output with these parameters page = 2 and count = 25

if we print print(r.url) so will get output : https://httpbin.org/get?page=2,count=25

So we learnt how we pass parameters to the url programmatically.




Post request : It is special type of request in which we use one API url end point and pass data in form
of submission of form as we do not want to forward data like username or password via get request where
entry is stored into the history of browser so for security purpose we use Post request if we are passing
such kind of data to end point API url.


syntax of post request :

payload = {"username": "Nitin", "password": "testing"}
r = requests.post("https://httpbin.org/post", data=payload)


Here, we created one dictionary which has two parameters username = Nitin and password = testing then
we requested the above url with post request along with passing parameters like data = payload instead
of params = payload in get request of module request.

so if we print print(r.text) so will get an output where we will get a form in which we will have two
parameters username = Nitin and password = testing and if we print print(r.url) here so will get an 
output : https://httpbin.org/post in spite of https://httpbin.org/post?username=Nitin&password=testing
in get request.

similarly, if we print print(r.headers) as we do in get request so we will get a dictionary which
tells ( Kaunse server ne ye web page banaya hai, last modify kb hua with date, content/type = text/html
etc).

If we print print(r.json()) so it also gives a data like dictionary we have in python but not exactly
dictionary which we will study further in next session of json module which is as important as this
request library where we will have entry of our form parameters as well which we do not get in 
print(r.headers) so we can create one variable r_dict here and store r.json() into it like this

r_dict = r.json()
print(r_dict["form"])

Here, we saved the dictionary into the variable r_dict by r_dict = r.json() then print print(r_dict["form"]
to get an output : {'password': 'testing', 'username': 'Nitin'}



Post request example in real life :
 
As we have end point API www.instagram.com so we request this end point with the help of post request
along with parameters data = payload where payload is a dictionary with parameters which could be username
and password so it goes to the server of instagram and where server validates these credentials and if
server founds these credentials so will forward the response accordingly.





Now, we will study about basic authentication which is also done with the help of get request of module
request like


syntax :

r = requests.get("https://httpbin.org/basic-auth/Nitin/IPLUAE@2020", auth=("Nitin","IPLUAE@2020"))   
print(r.text)   


Here, we requested the url API https://httpbin.org like https://httpbin.org/basic-auth/Nitin/IPLUAE@2020
so here we passed user equals to Nitin and password would be IPLUAE@2020 then passed arguments auth =
("Nitin","IPLUAE@2020") that is tuple so if we pass the correct credentials user = Nitin and password =
IPLUAE@2020 so we will get an output like


{
  "authenticated": true, 
  "user": "Nitin"                                                                                      
}  


if we pass credentials like user = NitinSharma and password = IPLUAE@2020 so we will not get any output
as we are not passing the correct credentials.    



Real life example of basic auth : 

If we enter the API IP something like 168.192.0.1 of any router in url
in browser so it prompts us to enter username and password and if we enter the correct credentials so
it will direct us to the web page further.


Mechanism of basic auth :

Client sends a request to the server then server forwards back response as a form based username and
password like dialog box and if client enters the correct details then server sends the response back
to client with the login into web page further and if not enter the correct credentials so server will
give an error called unauthorised error with status code 401 ( Client error unauthorised access 401 )                                                                                    





"""











