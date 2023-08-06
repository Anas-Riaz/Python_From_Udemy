
'''Healthy programmer
 1) reminder to drink water between 9:00 am to 5:00 pm, about 3.5 litre or 16-17 glass of water 
    untill user give input Drank. 
 2) Eyes excersise reminder after every 30 mins take input done .
 3) physical excercise after every 45 min and take input done.
 4) create file and note the time of input for every task  
'''

from datetime import datetime
import time
from pygame import mixer

p = time.localtime().tm_hour

def reminder(file , stopper) :
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.get_volume(0.9)
    while True :
        a = input("Enter 'stop' to stop the reminder : ")
        if a == stopper :
            mixer.music.stop()
        break

def my_log(msg) :
    with open ("myfile.txt", "a") as t :
        t.write(f"{msg} {datetime.now()} \n")

print("please run the program from ( 9am to 5pm")

if __name__ == '__main__' :
    inital_water = time.time()
    inital_eyes = time.time() 
    inital_excercise = time.time()
    water_time = 30*60
    eyes_time = 30*60
    excercise_time = 50*60
    
    if (p>= 9) and (p<=17) :
        
        while True :
            if time.time() - inital_water > water_time : 
                print("drink water and type syop to stop the reminder")
                reminder("water.wav", "stop")
                initial_water = time.time()
                my_log("drank at ")
        
            if time.time() - inital_eyes > eyes_time:
                print("drink water and type syop to stop the reminder")
                reminder("water.wav", "stop")
                inital_eyes = time.time()
                my_log("drank at ")
                
            if time.time() - inital_excercise > excercise_time:
                print("drink water and type syop to stop the reminder")
                reminder("water.wav", "stop")
                inital_excercise = time.time()
                my_log("drank at ")
    
    if p < 9 :
        print("Your time will start at 9:00 AM localtime.")
    if p > 17 :
        print("You are done for the day! Program will start at 9:00 AM localtime tomorrow.")
