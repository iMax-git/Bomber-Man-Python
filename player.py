'''
Created on 17 fevr. 2021

@author: tdiard
'''

import pygame
import math

from main.bomb import Bomb

class Player:
    def __init__(self):
        self.life = True
        self.x = 4
        self.y = 4
        self.head = 0
        self.frame = 0
        self.animation = []
        self.range = 3
        self.bomb_limit = 1
        
    def move(self,dx,dy,grid,enemies):
        
        x = int(self.x/4)
        y = int(self.y/4)
        
        map = []
        
        for i in range(len(grid)):
            map.append([])
            for j in range(len(grid[i])):
                map[i].append(grid[i][j])
        
        for pax in enemies:
            if pax == self:
                continue
            elif not pax.life:
                continue
            else:
                map[int(x.posX/4)][int(x.posY/4)] = 2

        if self.x % 4 != 0 and dx == 0:
            if self.x % 4 == 1:
                self.x -= 1
            elif self.x % 4 == 3:
                self.x += 1
            return
        if self.y % 4 != 0 and dy == 0:
            if self.y % 4 == 1:
                self.y -= 1
            elif self.y % 4 == 3:
                self.y += 1
            return
        
         # right
        if dx == 1:
            if map[x+1][y] == 0:
                self.x += 1
        # left
        elif dx == -1:
            x = math.ceil(self.x / 4)
            if map[x-1][y] == 0:
                self.x -= 1

        # bottom
        if dy == 1:
            if map[x][y+1] == 0:
                self.y += 1
        # top
        elif dy == -1:
            y = math.ceil(self.y / 4)
            if map[x][y-1] == 0:
                self.y -= 1
                
    def plantbomb(self,map):
        bomb = Bomb(self.range, round(self.x/4),round(self.y/4), map,self)
        return bomb
    
    def dead(self,exp):
        for explode in exp:
            for sector in explode.sectors:
                if int(self.y/4) == sector[0] and int(self.y/4) == sector[1]:
                    self.life = False
        pass
        
    def load_animations(self, scale):
        front = []
        back = []
        left = []
        right = []
        resize_width = scale
        resize_height = scale

        f1 = pygame.image.load('images/hero/pf0.png')
        f2 = pygame.image.load('images/hero/pf1.png')
        f3 = pygame.image.load('images/hero/pf2.png')

        f1 = pygame.transform.scale(f1, (resize_width, resize_height))
        f2 = pygame.transform.scale(f2, (resize_width, resize_height))
        f3 = pygame.transform.scale(f3, (resize_width, resize_height))

        front.append(f1)
        front.append(f2)
        front.append(f3)

        r1 = pygame.image.load('images/hero/pr0.png')
        r2 = pygame.image.load('images/hero/pr1.png')
        r3 = pygame.image.load('images/hero/pr2.png')

        r1 = pygame.transform.scale(r1, (resize_width, resize_height))
        r2 = pygame.transform.scale(r2, (resize_width, resize_height))
        r3 = pygame.transform.scale(r3, (resize_width, resize_height))

        right.append(r1)
        right.append(r2)
        right.append(r3)

        b1 = pygame.image.load('images/hero/pb0.png')
        b2 = pygame.image.load('images/hero/pb1.png')
        b3 = pygame.image.load('images/hero/pb2.png')

        b1 = pygame.transform.scale(b1, (resize_width, resize_height))
        b2 = pygame.transform.scale(b2, (resize_width, resize_height))
        b3 = pygame.transform.scale(b3, (resize_width, resize_height))

        back.append(b1)
        back.append(b2)
        back.append(b3)

        l1 = pygame.image.load('images/hero/pl0.png')
        l2 = pygame.image.load('images/hero/pl1.png')
        l3 = pygame.image.load('images/hero/pl2.png')

        l1 = pygame.transform.scale(l1, (resize_width, resize_height))
        l2 = pygame.transform.scale(l2, (resize_width, resize_height))
        l3 = pygame.transform.scale(l3, (resize_width, resize_height))

        left.append(l1)
        left.append(l2)
        left.append(l3)

        self.animation.append(front)
        self.animation.append(right)
        self.animation.append(back)
        self.animation.append(left)