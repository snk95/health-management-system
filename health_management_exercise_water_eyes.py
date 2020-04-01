from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':

    init_water=time()
    init_eyes=time()
    init_exercise=time()
    water_secs=35*60
    eyes_secs=30*60
    exer_secs=45*60

    while True:
        if time()-init_water > water_secs:
            print("Water drinking time. Enter 'drank' to stop the music")
            musiconloop("water.mp3","drank")
            init_water=time()
            log_now("Last drank at")

        if time() - init_eyes > eyes_secs:
            print("Eye exercise time. Enter 'done' to stop the music")
            musiconloop("eyes.mp3", "done")
            init_eyes = time()
            log_now("Last done at")

        if time() - init_exercise > exer_secs:
            print("Exercise time. Enter 'done' to stop the music")
            musiconloop("exercise.mp3", "done")
            init_exercise = time()
            log_now("Last done at")