from time import time
from PIL import Image
import numpy as np
import random

def Space (Array):
    Space = False
    for y in range (0, len(Array)):
        for x in range (0,len(Array)):
            if Array[y][x] == 255:
                Space = True
                break
    return Space

def Keim_position (x,y):
    x = int(random.random()*(x))
    y = int(random.random()*(y))
    return x,y


class Keim: 
    def __init__(self,x,y):
        self.speed = int(random.random()*25)
        self.time = int(random.random()*200)
        self.color = int((random.random()*200)+20)
        self.x, self.y = Keim_position(x,y)


#rows = int(input("Enter rows: "))
#colums = int(input("Enter colums: "))
#Anzahl = int(input("Enter Quantities of Keims: "))
time = 0
x, y, Anzahl = 2, 1, 1
Verzinkt_array= np.array([[255]*x]*y)
Keime = {}
for Keime_Anzahl in range (0,Anzahl):
    Keim_temp = Keim(x,y)
    Keime[Keime_Anzahl] = Keim_temp
    Verzinkt_array[Keim_temp.y][Keim_temp.x] = 0

print(Keime[0].time)
while Space(Verzinkt_array):
    for wachsen in range (0, len(Keime)):
        if Keime[wachsen].time == 0:
            if Keime[wachsen].x+1 < x:
                Verzinkt_array[Keime[wachsen].y][Keime[wachsen].x+1] = Keime[wachsen].color
                print("right")
            if Keime[wachsen].x-1 >= 0:
                Verzinkt_array[Keime[wachsen].y][Keime[wachsen].x-1] = Keime[wachsen].color
                print("left")
            if Keime[wachsen].y+1 < y:
                Verzinkt_array[Keime[wachsen].y+1][Keime[wachsen].x] = Keime[wachsen].color
                print("up")
            if Keime[wachsen].y-1 >= 0:
                Verzinkt_array[Keime[wachsen].y-1][Keime[wachsen].x] = Keime[wachsen].color
                print("down")
        if Keime[wachsen].time >= 0 :
            Keime[wachsen].time = Keime[wachsen].time- 1
        print(Keime[wachsen].time)
        if Keime[wachsen].time < 0:
            exit

im = Image.fromarray(Verzinkt_array.astype('uint8'))
im.save("./result.png")