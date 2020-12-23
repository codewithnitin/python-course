# Write a program to create a news reader from getting latest news in a json form data from the website
# https://newsapi.org which has a collection of news in a json form data ?

# pip install pywin32


import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

def speak1(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

def speak2(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)


r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=YourNewsApiKey")
json_string = r.text
dict = json.loads(json_string)
print(dict)

for i in range(0,10):
    speak(f"Headline number {i + 1}")
    speak1(dict["articles"][i]["title"])
    speak2(dict["articles"][i]["description"])




# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.speak(str)
#
# speak("There is a huge possibility of war between India and China now")



