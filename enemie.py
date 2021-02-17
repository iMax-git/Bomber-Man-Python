'''
Created on 17 fvr. 2021

@author: tdiard
'''
import pygame
import random
from main.bomb import Bomb

class Ennemi:
    
    def __init__(self,x,y,ia):
        self.life = True
        self.path = []
        self.movement_path = []
        self.x = x * 4
        self.y = y * 4
        self.direction = 0
        self.frame = 0
        self.animation = []
        self.range = 3
        self.bomb_limit = 1
        self.plant = False
        self.ia = ia
        
    def live(self, map, bomb, exp, skin):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1
            
    def plantbomb(self):
        pas