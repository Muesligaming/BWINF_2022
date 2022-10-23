from ast import Not
from time import time
from turtle import color
from PIL import Image
import numpy as np
import random

def Space (Array):
    Space = False
    for y in range (0, len(Array)):
        for x in range (0,len(Array[0])):
            if Array[y][x] == 255:
                return True
    return False

def Keim_position (x,y):
    x = int(random.random()*(x))
    y = int(random.random()*(y))
    return x,y

def colour_down(color,Array,x,y,Boarder_y,):
    if y+1 < Boarder_y:
        if Array[y+1][x] == 255:
            Array[y+1][x] = -1
    return Array

def colour_up(color,Array,x,y,Boarder_y):
    if y-1 >= 0:
        if Array[y-1][x] == 255:
            Array[y-1][x] = -1
    return Array

def colour_right(color, Array,x,y,Boarder_x):
    #print(str(x+1) + ", "+ str(Boarder_x))
    if x+1 < Boarder_x:
        if Array[y][x+1] == 255:
            Array[y][x+1] = -1
    return Array

def colour_left(color,Array,x,y,Boarder_x):
    if x-1 >= 0:
        if Array[y][x-1] == 255:
            Array[y][x-1] = -1
    return Array

def colour_temp(pcolor,Array):
    for x in range (0,len(Array[0])):
        for y in range (0, len(Array)):
            if Array[y][x] == -1:
                Array[y][x] = pcolor
    #print(str(pcolor)+ "  sdöahsjkddsf")
    return Array

class Keim: 
    def __init__(self,x,y):
        self.speed_right = int(random.random()*5+1)
        self.speed_left = int(random.random()*5+1)
        self.speed_up = int(random.random()*5+1)
        self.speed_down = int(random.random()*5+1)
        self.speed_max = max(self.speed_down,self.speed_left,self.speed_right,self.speed_up)
        #self.speed = int(random.random()*4+1)
        self.time = int(random.random()*50)
        self.color = int(random.random()*200+20)
        self.x, self.y = Keim_position(x,y)
        print(str(self.speed_right) + "; "+str(self.speed_left) + "; "+str(self.speed_up) + "; "+str(self.speed_down) + "; "+str(self.time) + "; " + str(self.color) )


#y = int(input("Enter rows: "))
#x = int(input("Enter colums: "))
#Anzahl = int(input("Enter Quantities of Keims: "))
time = 0
Border_x, Border_y, Anzahl = 500, 500, 200
Verzinkt_array= np.array([[255]*Border_x]*Border_y)
#for lkasdghkljdfksziuwejhbf in range(0,len(Verzinkt_array[0]),2):
#    Verzinkt_array[0][lkasdghkljdfksziuwejhbf]=254
#    Verzinkt_array[0][lkasdghkljdfksziuwejhbf+1]=1
Keime = {}
for Keime_Anzahl in range (0,Anzahl):
    Keim_temp = Keim(Border_x,Border_y)
    Keime[Keime_Anzahl] = Keim_temp
    Verzinkt_array[Keim_temp.y][Keim_temp.x] = 0
time_to_shine=[]
while Space(Verzinkt_array):
    #print(time_to_shine)
    im = Image.fromarray(Verzinkt_array.astype('uint8'))
    im.save("./result.png")
    im.show()
    for wachsen in range (0, len(Keime)):
        if Keime[wachsen].time == 0:
            Verzinkt_array=colour_right(Keime[wachsen].color,Verzinkt_array,Keime[wachsen].x,Keime[wachsen].y,Border_x)
            Verzinkt_array=colour_left(Keime[wachsen].color,Verzinkt_array,Keime[wachsen].x,Keime[wachsen].y,Border_x)
            Verzinkt_array=colour_up(Keime[wachsen].color,Verzinkt_array,Keime[wachsen].x,Keime[wachsen].y,Border_y)
            Verzinkt_array=colour_down(Keime[wachsen].color,Verzinkt_array,Keime[wachsen].x,Keime[wachsen].y,Border_y)
            Verzinkt_array = colour_temp(Keime[wachsen].color,Verzinkt_array)
            time_to_shine.append(Keime[wachsen])
        Keime[wachsen].time = Keime[wachsen].time- 1
        #print(Keime[wachsen].time)
    for Color in range (0, len(time_to_shine)):
            times = 0
            y,x = 0,0
            while times < time_to_shine[Color].speed_max:
                for y in range(0, Border_y):
                    for x in range(0,Border_x):
                        if (Verzinkt_array[y][x] == time_to_shine[Color].color):
                            if time_to_shine[Color].speed_right > times:
                                Verzinkt_array=colour_right(time_to_shine[Color].color,Verzinkt_array,x,y,Border_x)
                            if time_to_shine[Color].speed_left > times:
                                Verzinkt_array=colour_left(time_to_shine[Color].color,Verzinkt_array,x,y,Border_x)
                            if time_to_shine[Color].speed_up > times:
                                Verzinkt_array=colour_up(time_to_shine[Color].color,Verzinkt_array,x,y,Border_y)
                            if time_to_shine[Color].speed_down > times:
                                Verzinkt_array=colour_down(time_to_shine[Color].color,Verzinkt_array,x,y,Border_y)
                Verzinkt_array = colour_temp(time_to_shine[Color].color,Verzinkt_array)
                #print(str(time_to_shine[Color].color)+" lolo lololol")
                #print(str(Color)+"  HÄäääääääää")
                times = times +1
    im.close()
    
im = Image.fromarray(Verzinkt_array.astype('uint8'))
im.save("./result.png")
im.show()