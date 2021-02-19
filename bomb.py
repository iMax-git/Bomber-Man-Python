'''
Created on 17 fevr. 2021

@author: tdiard
'''

class Bomb:
    def __init__(self, range, x, y, map, bomber):
        self.range = range
        self.x = x
        self.y = y
        self.timer = 3000
        self.bomber = bomber
        self.sectors = []
        self.get_range(map)
        self.frame = 1
        
    def update(self, dt):

        self.timer = self.timer - dt

        if self.timer < 1000:
            self.frame = 2
        elif self.timer < 2000:
            self.frame = 1


    def get_range(self, map):

        self.sectors.append([self.x, self.y])

        for xp in range(1, self.range):
            if map[self.x + xp][self.y] == 1:
                break
            elif map[self.x+xp][self.y] == 0 or map[self.x-xp][self.y] == 3:
                self.sectors.append([self.x+xp, self.y])
            elif map[self.x+xp][self.y] == 2:
                self.sectors.append([self.x+xp, self.y])
                break
        for xp in range(1, self.range):
            if map[self.x - xp][self.y] == 1:
                break
            elif map[self.x-xp][self.y] == 0 or map[self.x-xp][self.y] == 3:
                self.sectors.append([self.x-xp, self.y])
            elif map[self.x-xp][self.y] == 2:
                self.sectors.append([self.x-xp, self.y])
                break
        for xp in range(1, self.range):
            if map[self.x][self.y + xp] == 1:
                break
            elif map[self.x][self.y+xp] == 0 or map[self.x][self.y+xp] == 3:
                self.sectors.append([self.x, self.y+xp])
            elif map[self.x][self.y+xp] == 2:
                self.sectors.append([self.x, self.y+xp])
                break
        for xp in range(1, self.range):
            if map[self.x][self.y - xp] == 1:
                break
            elif map[self.x][self.y-xp] == 0 or map[self.x][self.y-xp] == 3:
                self.sectors.append([self.x, self.y-xp])
            elif map[self.x][self.y - xp] == 2:
                self.sectors.append([self.x, self.y - xp])
                break
