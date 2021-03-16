from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,sttoper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input("enter commound to stop:\n")
        if a==sttoper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylog.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")

if __name__ == '__main__':
    init_water=time()
    init_eye = time()
    init_phy = time()
    watersec=60*60
    eyesec = 65*60
    physec = 70*60
    while True:
        if time()-init_water > watersec:
            print("water drinking time and write \npress  'stop' to stop alarm")
            musiconloop("sound.mp3.mp3","stop")
            init_water=time()
            log_now("drank water at:")
        if time()-init_eye > eyesec:
            print("hello its your eye exercise time \npress  'stop' to stop alarm")
            musiconloop("sound.mp3.mp3","stop")
            init_eye=time()
            log_now("drank water at:")
        if time()-init_phy > physec:
            print("hello astha its your physical exercise time \npress 'stop' to stop alarm")
            musiconloop("sound.mp3.mp3","stop")
            init_phy=time()
            log_now("physical exercise done at:")
            

