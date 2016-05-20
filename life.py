import os
import time
from copy import deepcopy
class game_life():
    def __init__(self,size):
        loadmap = open("map","r")
        reading = loadmap.readline()
        self.map = []
        self.min_alive = 2
        self.max_alive = 3
        self.min_born = 3
        self.max_born = 3
        self.sleepingtime = 0.5
        self.newmap = []
        while reading:
            self.map.append(reading.split())
            reading = loadmap.readline()
        self.Are_you_alive()
    def Are_you_alive(self):
        self.newmap = deepcopy(self.map)
        while 1:
            for y in range(len(self.map)):
                for x in range(len(self.map[y])):
                    if self.map[y][x] == "1":
                        if not self.crowded(self.min_alive,self.max_alive,x,y):
                            self.newmap[y][x] = "0"
                    else:
                        if self.crowded(self.min_born,self.max_born,x,y):
                            self.newmap[y][x] = "1"
            self.map = deepcopy(self.newmap)
            for x in self.map:
                print(*x)
            time.sleep(self.sleepingtime)
            os.system('clear')
    def crowded(self,minn,maxx,x,y):
        count = 0
        for j in range(max(y-1,0),min(y+2,len(map))):
            for i in range(max(x-1,0),min(x+2,len(map))):
                if self.map[j][i] == 1:
                    count += 1
        return ((count <= maxx) and (count >= minn))
life = game_life(50)
