from ast import Not
from time import time
from PIL import Image
import numpy as np
import random

def Space (Array):
    Space = False
    for y in range (0, len(Array)):
        for x in range (0,len(Array[0])):
            if Array[y][x] == 255:
                Space = True
    return Space

def Keim_position (x,y):
    x = int(random.random()*(x))
    y = int(random.random()*(y))
    return x,y

def colour_down(color,Array,x,y,Boarder_y,):
    if y+1 < Boarder_y:
        if Array[y+1][x] == 255:
            Array[y+1][x] = color
    return Array

def colour_up(color,Array,x,y,Boarder_y):
    if y-1 >= 0:
        if Array[y-1][x] == 255:
            Array[y-1][x] = color
    return Array

def colour_right(color, Array,x,y,Boarder_x):
    #print(str(x+1) + ", "+ str(Boarder_x))
    if x+1 < Boarder_x:
        if Array[y][x+1] == 255:
            Array[y][x+1] = color
    return Array

def colour_left(color,Array,x,y,Boarder_x):
    if x-1 >= 0:
        if Array[y][x-1] == 255:
            Array[y][x-1] = color
    return Array

class Keim: 
    def __init__(self,x,y):
        self.speed = 2#int(random.random()*4)
        self.time = 0#int(random.random()*50)
        self.color = 30#int((random.random()*200)+20)
        self.x, self.y = 5,5#Keim_position(x,y)


#y = int(input("Enter rows: "))
#x = int(input("Enter colums: "))
#Anzahl = int(input("Enter Quantities of Keims: "))
time = 0
Border_x, Border_y, Anzahl = 10, 10, 1
Verzinkt_array= np.array([[255]*Border_x]*Border_y)
for lkasdghkljdfksziuwejhbf in range(0,len(Verzinkt_array[0]),2):
    Verzinkt_array[0][lkasdghkljdfksziuwejhbf]=254
    Verzinkt_array[0][lkasdghkljdfksziuwejhbf+1]=1
Keime = {}
for Keime_Anzahl in range (0,Anzahl):
    Keim_temp = Keim(Border_x,Border_y)
    Keime[Keime_Anzahl] = Keim_temp
    Verzinkt_array[Keim_temp.y][Keim_temp.x] = 0
time_to_shine=[]
while Space(Verzinkt_array):
    print(time_to_shine)
    im = Image.fromarray(Verzinkt_array.astype('uint8'))
    im.save("./result.png")
    im.show()
    for wachsen in range (0, len(Keime)):
        if Keime[wachsen].time == 0:
            Verzinkt_array=colour_right(Keime[wachsen].color,Verzinkt_array,Keime[wachsen].x,Keime[wachsen].y,Border_x)
            Verzinkt_array=colour_left(Keime[wachsen].color,Verzinkt_array,Keime[wachsen].x,Keime[wachsen].y,Border_x)
            Verzinkt_array=colour_up(Keime[wachsen].color,Verzinkt_array,Keime[wachsen].x,Keime[wachsen].y,Border_y)
            Verzinkt_array=colour_down(Keime[wachsen].color,Verzinkt_array,Keime[wachsen].x,Keime[wachsen].y,Border_y)
            time_to_shine.append(Keime[wachsen])
        Keime[wachsen].time = Keime[wachsen].time- 1
        print(Keime[wachsen].time)
    for Color in range (0, len(time_to_shine)):
            times = time_to_shine[Color].speed
            while times > 0:
                times = times -1
                y,x = 0,0
                for y in range(0, Border_y):
                    for x in range(0,Border_x):
                        Verzinkt_array_temp = Verzinkt_array
                        if (Verzinkt_array[y][x] == time_to_shine[Color].color):
                            Verzinkt_array_temp=colour_right(time_to_shine[Color].color,Verzinkt_array_temp,x,y,Border_x)
                            Verzinkt_array_temp=colour_left(time_to_shine[Color].color,Verzinkt_array_temp,x,y,Border_x)
                            Verzinkt_array_temp=colour_up(time_to_shine[Color].color,Verzinkt_array_temp,x,y,Border_y)
                            Verzinkt_array_temp=colour_down(time_to_shine[Color].color,Verzinkt_array_temp,x,y,Border_y)
            Verzinkt_array = Verzinkt_array_temp
    im.close()
    
im = Image.fromarray(Verzinkt_array.astype('uint8'))
im.save("./result.png")
im.show()