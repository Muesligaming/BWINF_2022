#from ast import Not
#from time import time
#from turtle import color
from PIL import Image
import numpy as np
import random

def Space (Array):
    Space = False
    for y in range (0, len(Array)):
        for x in range (0,len(Array[0])):
            if Array[y][x][0] == 255:
                return True
    return False

def Keim_position (x,y):
    x = int(random.random()*(x))
    y = int(random.random()*(y))
    return x,y

def colour_down(color,x,y,Array,t):
    if Array[y][x][4]>t:
        if color == -5:
            color = Array[y][x][0]
        if y+1 < len(Array):
            if Array[y+1][x][0] == 255:
                Array[y+1][x][0] = color - (color*2)
                Array[y+1][x][1] = Array[y][x][1]
                Array[y+1][x][2] = Array[y][x][2]
                Array[y+1][x][3] = Array[y][x][3]
                Array[y+1][x][4] = Array[y][x][4]
                Array = colour_right(color,x,y+1,Array,t+1)
                Array = colour_left(color,x,y+1,Array,t+1)
                Array = colour_up(color,x,y+1,Array,t+1)
                Array = colour_down(color,x,y+1,Array,t+1)
    return Array

def colour_up(color,x,y,Array,t):
    if Array[y][x][3]>t:
        if color == -5:
            color = Array[y][x][0]
        if y-1 >= 0:
            if Array[y-1][x][0] == 255:
                Array[y-1][x][0] = color - (color*2)
                Array[y-1][x][1] = Array[y][x][1]
                Array[y-1][x][2] = Array[y][x][2]
                Array[y-1][x][3] = Array[y][x][3]
                Array[y-1][x][4] = Array[y][x][4]
                Array = colour_right(color,x,y-1,Array,t+1)
                Array = colour_left(color,x,y-1,Array,t+1)
                Array = colour_up(color,x,y-1,Array,t+1)
                Array = colour_down(color,x,y-1,Array,t+1)
    return Array

def colour_right(color,x,y, Array,t):
    #print(str(x+1) + ", "+ str(Boarder_x))
    if Array[y][x][1]>t:
        if color == -5:
            color = Array[y][x][0]
        #print(color)
        if x+1 < len(Array[0]):
            if Array[y][x+1][0] == 255:
                Array[y][x+1][0] = color - (color*2)
                Array[y][x+1][1] = Array[y][x][1]
                Array[y][x+1][2] = Array[y][x][2]
                Array[y][x+1][3] = Array[y][x][3]
                Array[y][x+1][4] = Array[y][x][4]
                Array = colour_right(color,x+1,y,Array,t+1)
                Array = colour_left(color,x+1,y,Array,t+1)
                Array = colour_up(color,x+1,y,Array,t+1)
                Array = colour_down(color,x+1,y-1,Array,t+1)
    return Array

def colour_left(color,x,y,Array,t):
    if Array[y][x][2]>t:
        if color == -5:
            color = Array[y][x][0]
        if x-1 >= 0:
            if Array[y][x-1][0] == 255:
                Array[y][x-1][0] = color - (color*2)
                Array[y][x-1][1] = Array[y][x][1]
                Array[y][x-1][2] = Array[y][x][2]
                Array[y][x-1][3] = Array[y][x][3]
                Array[y][x-1][4] = Array[y][x][4]
                Array = colour_right(color,x-1,y,Array,t+1)
                Array = colour_left(color,x-1,y,Array,t+1)
                Array = colour_up(color,x-1,y,Array,t+1)
                Array = colour_down(color,x-1,y,Array,t+1)
    return Array

def colour_temp(Array):
    for x in range (0,len(Array[0])):
        for y in range (0, len(Array)):
            if Array[y][x][0] < 0:
                temp = Array[y][x][0]
                Array[y][x][0] = -temp
    #print(str(pcolor)+ "  sdöahsjkddsf")
    #print(Array)
    return Array

class Keim: 
    def __init__(self,x,y):
        self.speed_right = int(random.random()*20+1)
        self.speed_left = int(random.random()*20+1)
        self.speed_up = int(random.random()*20+1)
        self.speed_down = int(random.random()*20+1)
        self.speed_max = max(self.speed_down,self.speed_left,self.speed_right,self.speed_up)
        #self.speed = int(random.random()*4+1)
        self.time = int(random.random()*10)
        self.color = int(random.random()*200+20)
        self.x, self.y = Keim_position(x,y)
        print(str(self.speed_right) + "; "+str(self.speed_left) + "; "+str(self.speed_up) + "; "+str(self.speed_down) + "; "+str(self.time) + "; " + str(self.color) )


Border_y = 768 #int(input("Enter rows: "))
Border_x = 1024 #int(input("Enter colums: "))
Anzahl = int(input("Enter Quantities of Keims: "))
time = 0
#Border_x, Border_y, Anzahl = 500, 500, 200
Verzinkt_array= np.array([[[255,0,0,0,0]]*Border_x]*Border_y)
#print(Verzinkt_array[0][0][0])
#for lkasdghkljdfksziuwejhbf in range(0,len(Verzinkt_array[0]),2):
#    Verzinkt_array[0][lkasdghkljdfksziuwejhbf]=254
#    Verzinkt_array[0][lkasdghkljdfksziuwejhbf+1]=1
Keime = {}
for Keime_Anzahl in range (0,Anzahl):
    Keim_temp = Keim(Border_x,Border_y)
    Keime[Keime_Anzahl] = Keim_temp
    Verzinkt_array[Keim_temp.y][Keim_temp.x][0] = 0
    Verzinkt_array[Keim_temp.y][Keim_temp.x][1] = Keim_temp.speed_right
    Verzinkt_array[Keim_temp.y][Keim_temp.x][2] = Keim_temp.speed_left
    Verzinkt_array[Keim_temp.y][Keim_temp.x][3] = Keim_temp.speed_up
    Verzinkt_array[Keim_temp.y][Keim_temp.x][4] = Keim_temp.speed_down
time_to_shine=[]
while Space(Verzinkt_array):
    print("Next Picture \n")
    #final_array = np.array([[255]*Border_x]*Border_y)
    #for y in range(0, Border_y):
    #    for x in range(0,Border_x):
    #        final_array[y][x] = Verzinkt_array[y][x][0]
    #im = Image.fromarray(final_array.astype('uint8'))
    #im.save("./result.png")
    #im.show()
    for wachsen in range (0, len(Keime)):
        if Keime[wachsen].time == 0:
            Verzinkt_array = colour_right(Keime[wachsen].color,Keime[wachsen].x,Keime[wachsen].y,Verzinkt_array,0)
            Verzinkt_array = colour_left(Keime[wachsen].color,Keime[wachsen].x,Keime[wachsen].y,Verzinkt_array,0)
            Verzinkt_array = colour_up(Keime[wachsen].color,Keime[wachsen].x,Keime[wachsen].y,Verzinkt_array,0)
            Verzinkt_array = colour_down(Keime[wachsen].color,Keime[wachsen].x,Keime[wachsen].y,Verzinkt_array,0)
            Verzinkt_array = colour_temp(Verzinkt_array)
            time_to_shine.append(Keime[wachsen])
        Keime[wachsen].time = Keime[wachsen].time- 1
        #print(Keime[wachsen].time)
    #for Color in range (0, len(time_to_shine)):
    #times = 0
    #y,x = 0,0
    #while times < time_to_shine[Color].speed_max:
    for y in range(0, Border_y):
        for x in range(0,Border_x):
            if (0 < Verzinkt_array[y][x][0] < 255 ):
                    Verzinkt_array=colour_right(-5,x,y,Verzinkt_array,0)
                    Verzinkt_array=colour_left(-5,x,y,Verzinkt_array,0)
                    Verzinkt_array=colour_up(-5,x,y,Verzinkt_array,0)
                    Verzinkt_array=colour_down(-5,x,y,Verzinkt_array,0)
    Verzinkt_array = colour_temp(Verzinkt_array)
    #print(str(time_to_shine[Color].color)+" lolo lololol")
    #print(str(Color)+"  HÄäääääääää")
    #times = times +1
    #im.close()
    
final_array = np.array([[255]*Border_x]*Border_y)
for y in range(0, Border_y):
    for x in range(0,Border_x):
        final_array[y][x] = Verzinkt_array[y][x][0]
im = Image.fromarray(final_array.astype('uint8'))
im.save("./result.png")
im.show()