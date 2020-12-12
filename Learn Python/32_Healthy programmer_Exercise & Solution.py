
from pygame import mixer
from datetime import datetime
from time import time
def playmusiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()                    #Keep our python file, music files and log file in same directory
    while(True):
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_data(msg):
    with open("log_data.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")
        print("Written successfully")
init_water = time()
watersecs = 3600
init_eyes = time()
eyesecs = 5400
init_physical = time()
physicalsecs = 6300
while(True):
    if time()-init_water>watersecs:
        print("Water drinking time. Enter drank to stop the alarm")
        playmusiconloop("Water.mp3", "drank")
        log_data("Drank water at")
        init_water = time()
    if time()-init_eyes>eyesecs:
        print("Eyes exercise time. Enter eydone to stop the alarm")
        playmusiconloop("Eye.mp3", "eydone")
        log_data("Eyes exercise done at")
        init_eyes = time()
    if time()-init_physical>physicalsecs:
        print("Physical exercise time. Enter phydone to stop the alarm")
        playmusiconloop("Physical.mp3", "phydone")
        log_data("Physical exercise done at")
        init_physical = time()
















