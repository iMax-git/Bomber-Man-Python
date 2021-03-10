'''
Created on 17 fvr. 2021

@author: tdiard
'''
import pygame
import random
try:
    from bomb import *
    from bonus import *
    from SELECT import *
except ImportError: 
    from main.bomb import *
    from main.bonus import *
    from main.SELECT import *

class Ennemi:
    
    def __init__(self,x,y,ia):
        self.life = True
        self.path = []
        self.movement_path = []
        self.x = x * 4
        self.y = y * 4
        self.head = 0
        self.frame = 0
        self.animation = []
        self.range = 3
        self.bomb_limit = 1
        self.plant = False
        self.ia = ia
        self.dire = [[1, 0, 1], [0, 1, 0], [-1, 0, 3], [0, -1, 2]]
        
    def live(self, map, bomb, exp, ennemi):
        if self.head == 0:
            self.y += 1
        elif self.head == 1:
            self.x += 1
        elif self.head == 2:
            self.y -= 1
        elif self.head == 3:
            self.x -= 1
            
        if self.x % 4 == 0 and self.y % 4 == 0:
            self.movement_path.pop(0)
            self.path.pop(0)
            if len(self.path) > 1:
                grid = self.create_grid(map, bomb, exp, ennemi)
                next = self.path[1]
                if grid[next[0]][next[1]] > 1:
                    self.movement_path.clear()
                    self.path.clear()

    def make_move(self, map, bombs, explosions, enemy):
        if not self.life:
            return
        if len(self.movement_path) == 0:
            if self.plant:

                bombs.append(self.plant_bomb(map))
                self.plant = False
                map[int(self.x / 4)][int(self.y / 4)] = 3
            if self.ia is SELECT.BOT:
                self.paths(self.create_grid(map, bombs, explosions, enemy))
            else:
                self.perso(self.create_grid_perso(map, bombs, explosions, enemy))

        else:
            self.head = self.movement_path[0]
            self.live(map, bombs, explosions, enemy)

    def plant_bomb(self, map):
        b = Bomb(self.range, round(self.x / 4), round(self.y / 4), map, self)
        self.bomb_limit -= 1
        return b

    def dead(self, explode):

        for exp in explode:
            for area in exp.sectors:
                if int(self.x / 4) == area[0] and int(self.y / 4) == area[1]:
                    print("hit")
                    if exp.bomber == self:
                        self.life = False
                    return

    def paths(self, grid):
        new_path = [[int(self.x / 4), int(self.y / 4)]]
        if self.bomb_limit == 0:
            self.paths_rec(grid, 0, new_path, 0)
        else:
            self.paths_rec(grid, 2, new_path, 0)

        self.path = new_path

    def paths_rec(self, grid, end, path, depth):
        last = path[-1]
        if depth > 200:
            return
        if grid[last[0]][last[1]] == 0 and end == 0:
            return
        elif end == 2:
            if grid[last[0] + 1][last[1]] == end or grid[last[0] - 1][last[1]] == end or grid[last[0]][last[1] + 1] == end or grid[last[0]][last[1] - 1] == end:
                if len(path) == 1 and end == 2:
                    self.plant = True
                return

        grid[last[0]][last[1]] = 9

        random.shuffle(self.dire)
        if grid[last[0] + self.dire[0][0]][last[1] + self.dire[0][1]] == 0:
            path.append([last[0] + self.dire[0][0], last[1] + self.dire[0][1]])
            self.movement_path.append(self.dire[0][2])
        elif grid[last[0] + self.dire[1][0]][last[1] + self.dire[1][1]] == 0:
            path.append([last[0] + self.dire[1][0], last[1] + self.dire[1][1]])
            self.movement_path.append(self.dire[1][2])
        elif grid[last[0] + self.dire[2][0]][last[1] + self.dire[2][1]] == 0:
            path.append([last[0] + self.dire[2][0], last[1] + self.dire[2][1]])
            self.movement_path.append(self.dire[2][2])
        elif grid[last[0] + self.dire[3][0]][last[1] + self.dire[3][1]] == 0:
            path.append([last[0] + self.dire[3][0], last[1] + self.dire[3][1]])
            self.movement_path.append(self.dire[3][2])
        elif grid[last[0] + self.dire[0][0]][last[1] + self.dire[0][1]] == 1:
            path.append([last[0] + self.dire[0][0], last[1] + self.dire[0][1]])
            self.movement_path.append(self.dire[0][2])
        elif grid[last[0] + self.dire[1][0]][last[1] + self.dire[1][1]] == 1:
            path.append([last[0] + self.dire[1][0], last[1] + self.dire[1][1]])
            self.movement_path.append(self.dire[1][2])
        elif grid[last[0] + self.dire[2][0]][last[1] + self.dire[2][1]] == 1:
            path.append([last[0] + self.dire[2][0], last[1] + self.dire[2][1]])
            self.movement_path.append(self.dire[2][2])
        elif grid[last[0] + self.dire[3][0]][last[1] + self.dire[3][1]] == 1:
            path.append([last[0] + self.dire[3][0], last[1] + self.dire[3][1]])
            self.movement_path.append(self.dire[3][2])
        else:
            if len(self.movement_path) > 0:
                path.pop(0)
                self.movement_path.pop(0)
        depth += 1
        self.paths_rec(grid, end, path, depth)

    def perso(self, grid):

        end = 1
        if self.bomb_limit == 0:
            end = 0

        visited = []
        open_list = []
        map = grid[int(self.x / 4)][int(self.y / 4)]
        map.weight = map.base_weight
        new_path = []
        while True:
            visited.append(map)
            random.shuffle(self.dire)
            if (map.value == end and end == 0) or (end == 1 and (grid[map.x+1][map.y].value == 1 or grid[map.x-1][map.y].value == 1 or grid[map.x][map.y+1].value == 1 or grid[map.x][map.y-1].value == 1)):
                new_path.append([map.x, map.y])
                while True:
                    if map.parent is None:
                        break
                    map = map.parent
                    new_path.append([map.x, map.y])
                new_path.reverse()
                for xd in range(len(new_path)):
                    if new_path[xd] is not new_path[-1]:
                        if new_path[xd][0] - new_path[xd+1][0] == -1:
                            self.movement_path.append(1)
                        elif new_path[xd][0] - new_path[xd + 1][0] == 1:
                            self.movement_path.append(3)
                        elif new_path[xd][1] - new_path[xd + 1][1] == -1:
                            self.movement_path.append(0)
                        elif new_path[xd][1] - new_path[xd + 1][1] == 1:
                            self.movement_path.append(2)
                if len(new_path) == 1 and end == 1:
                    self.plant = True
                self.path = new_path
                return

            for i in range(len(self.dire)):
                if map.x + self.dire[i][0] < len(grid) and map.y + self.dire[i][1] < len(grid):
                    if grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].reach and grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]] not in visited:
                        if grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]] in open_list:
                            if grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].weight > grid[map.x][map.y].weight + grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].base_weight:
                                grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].parent = map
                                grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].weight = map.weight + grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].base_weight
                                grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].head = self.dire[i][2]

                        else:
                            grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].parent = map
                            grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].weight = map.weight + grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].base_weight
                            grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]].head = self.dire[i][2]
                            open_list.append(grid[map.x + self.dire[i][0]][map.y + self.dire[i][1]])

            if len(open_list) == 0:
                self.path = [[int(self.x / 4), int(self.y / 4)]]
                return

            next = open_list[0]
            for n in open_list:
                if n.weight < next.weight:
                    next = n
            open_list.remove(next)
            map = next


    def create_grid(self, map, bombs, explosions, bot):
        grid = [[0] * len(map) for i in range(len(map))]

        for b in bombs:
            b.get_range(map)
            for x in b.sectors:
                grid[x[0]][x[1]] = 1
            grid[b.x][b.y] = 3

        for e in explosions:
            for s in e.sectors:
                grid[s[0]][s[1]] = 3

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    grid[i][j] = 3
                elif map[i][j] == 2:
                    grid[i][j] = 2

        for BotInfo in bot:
            if BotInfo == self:
                continue
            elif not BotInfo.life:
                continue
            else:
                grid[int(BotInfo.x / 4)][int(BotInfo.y / 4)] = 2

        return grid

    def create_grid_perso(self, map, bombs, explosions, bot):
        grid = [[None] * len(map) for r in range(len(map))]

        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] == 0:
                    grid[i][j] = Bonus(i, j, True, 1, 0)
                elif map[i][j] == 2:
                    grid[i][j] = Bonus(i, j, False, 999, 1)
                elif map[i][j] == 1:
                    grid[i][j] = Bonus(i, j, False, 999, 2)
                elif map[i][j] == 3:
                    grid[i][j] = Bonus(i, j, False, 999, 2)

        for b in bombs:
            b.get_range(map)
            for x in b.sectors:
                grid[x[0]][x[1]].weight = 5
                grid[x[0]][x[1]].value = 3
            grid[b.x][b.y].reach = False

        for e in explosions:
            for s in e.sectors:
                grid[s[0]][s[1]].reach = False

        for BotInfo in bot:
            if BotInfo == self:
                continue
            elif not BotInfo.life:
                continue
            else:
                grid[int(BotInfo.x / 4)][int(BotInfo.y / 4)].reach = False
                grid[int(BotInfo.x / 4)][int(BotInfo.y / 4)].value = 1
        return grid

    def load_animations(self, en, scale):
        front = []
        back = []
        left = []
        right = []
        resize_width = scale
        resize_height = scale

        image_path = 'images/enemy/e'
        if en == '':
            image_path = 'images/hero/p'

        f1 = pygame.image.load(image_path + en + 'f0.png')
        f2 = pygame.image.load(image_path + en + 'f1.png')
        f3 = pygame.image.load(image_path + en + 'f2.png')

        f1 = pygame.transform.scale(f1, (resize_width, resize_height))
        f2 = pygame.transform.scale(f2, (resize_width, resize_height))
        f3 = pygame.transform.scale(f3, (resize_width, resize_height))

        front.append(f1)
        front.append(f2)
        front.append(f3)

        r1 = pygame.image.load(image_path + en + 'r0.png')
        r2 = pygame.image.load(image_path + en + 'r1.png')
        r3 = pygame.image.load(image_path + en + 'r2.png')

        r1 = pygame.transform.scale(r1, (resize_width, resize_height))
        r2 = pygame.transform.scale(r2, (resize_width, resize_height))
        r3 = pygame.transform.scale(r3, (resize_width, resize_height))

        right.append(r1)
        right.append(r2)
        right.append(r3)

        b1 = pygame.image.load(image_path + en + 'b0.png')
        b2 = pygame.image.load(image_path + en + 'b1.png')
        b3 = pygame.image.load(image_path + en + 'b2.png')

        b1 = pygame.transform.scale(b1, (resize_width, resize_height))
        b2 = pygame.transform.scale(b2, (resize_width, resize_height))
        b3 = pygame.transform.scale(b3, (resize_width, resize_height))

        back.append(b1)
        back.append(b2)
        back.append(b3)

        l1 = pygame.image.load(image_path + en + 'l0.png')
        l2 = pygame.image.load(image_path + en + 'l1.png')
        l3 = pygame.image.load(image_path + en + 'l2.png')

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
