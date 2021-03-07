import pygame
import sys # Pour le Fin de tache
import random
import time
try:
    from player import *
    from enemi import *
    from AI import *
    from explode import *
except ImportError: 
    from main.player import *
    from main.enemi import *
    from main.AI import *
    from main.explode import *


Keys = {"UP":273,"DOWN":274,"RIGHT":276,"LEFT":274, "A":113, "B":98, "C":99, "D":100, "E":101, "F":102,
         "G":103, "H":104, "I":105, "J":106, "K":107, "M":59, "N":110, "O":111, "P":112, "Q":97, "R":114,
          "S":115, "T":116, "U":117, "V":118, "W":122, "X":120, "Y":121, "Z":119, "ESC":27}
width = 40
height = 40 

window_width = 13*width
window_height = 13*height

background = (107, 142, 35)




screen = None
show_path = True

clock = None

player = None
other_list = []
blocks = []
bombs = []
explode = []

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

grass_img = None
block_img = None
box_img = None
bomb1_img = None
bomb2_img = None
bomb3_img = None
explosion1_img = None
explosion2_img = None
explosion3_img = None


terrain_images = []
bomb_images = []
explosion_images = []

pygame.font.init()
font = pygame.font.SysFont('Bebas', 30)
string_lose = font.render('GAME OVER', False, (0, 0, 0))
string_win = font.render('WIN', False, (0, 0, 0))

def initGame(path,player_ia,ennemi1_ia,ennemi2_ia,ennemi3_ia, scale):
    global height,width,screen,font,clock,other_list,blocks,player,explode,bombs,grass_img,block_img,box_img,bomb1_img,bomb2_img,bomb3_img,explosion1_img,explosion2_img,explosion3_img,terrain_images,bomb_images,explosion_images
    height = scale
    width = scale
    font = pygame.font.SysFont('Bebas', scale)
    show_path = path
    screen = pygame.display.set_mode((13 * width, 13 * height))
    pygame.display.set_caption('Bomber-Man-Python')
    clock = pygame.time.Clock()
    other_list = []
    blocks = []
    bombs.clear()
    explode.clear()
    player = Player()

    if ennemi1_ia is not IA.NONE:
        ennemi1 = Ennemi(11, 11, ennemi1_ia)
        ennemi1.load_animations('1', scale)
        other_list.append(ennemi1)
        blocks.append(ennemi1)

    if ennemi2_ia is not IA.NONE:
        ennemi2 = Ennemi(1, 11, ennemi2_ia)
        ennemi2.load_animations('2', scale)
        other_list.append(ennemi2)
        blocks.append(ennemi2)

    if ennemi3_ia is not IA.NONE:
        ennemi3 = Ennemi(11, 1, ennemi3_ia)
        ennemi3.load_animations('3', scale)
        other_list.append(ennemi3)
        blocks.append(ennemi3)

    if player_ia is IA.PLAYER:
        player.load_animations(scale)
        blocks.append(player)
    elif player_ia is not IA.NONE:
        en0 = Ennemi(1, 1, player_ia)
        en0.load_animations('', scale)
        other_list.append(en0)
        blocks.append(en0)
        player.life = False
    else:
        player.life = False
    

    
    grass_img = pygame.image.load('images/terrain/grass.png')
    grass_img = pygame.transform.scale(grass_img, (width, height))
    block_img = pygame.image.load('images/terrain/block.png')
    block_img = pygame.transform.scale(block_img, (width, height))
    box_img = pygame.image.load('images/terrain/box.png')
    box_img = pygame.transform.scale(box_img, (width, height))
    bomb1_img = pygame.image.load('images/bomb/1.png')
    bomb1_img = pygame.transform.scale(bomb1_img, (width, height))
    bomb2_img = pygame.image.load('images/bomb/2.png')
    bomb2_img = pygame.transform.scale(bomb2_img, (width, height))
    bomb3_img = pygame.image.load('images/bomb/3.png')
    bomb3_img = pygame.transform.scale(bomb3_img, (width, height))
    explosion1_img = pygame.image.load('images/explosion/1.png')
    explosion1_img = pygame.transform.scale(explosion1_img, (width, height))
    explosion2_img = pygame.image.load('images/explosion/2.png')
    explosion2_img = pygame.transform.scale(explosion2_img, (width, height))
    explosion3_img = pygame.image.load('images/explosion/3.png')
    explosion3_img = pygame.transform.scale(explosion3_img, (width, height))
    terrain_images = [grass_img, block_img, box_img, grass_img]
    bomb_images = [bomb1_img, bomb2_img, bomb3_img]
    explosion_images = [explosion1_img, explosion2_img, explosion3_img]
    main()

def main():
    createmap()
    while player.life:
        timer = clock.tick(15)
        for bot in other_list:
            bot.make_move(map, bombs, explode, blocks)
        keys = pygame.key.get_pressed()
        temp = player.head
        movement = False
        if keys[pygame.K_DOWN]:
            temp = 0
            player.move(0, 1, map, blocks)
            movement = True
        elif keys[pygame.K_RIGHT]:
            temp = 1
            player.move(1, 0, map, blocks)
            movement = True
        elif keys[pygame.K_UP]:
            temp = 2
            player.move(0, -1, map, blocks)
            movement = True
        elif keys[pygame.K_LEFT]:
            temp = 3
            player.move(-1, 0, map, blocks)
            movement = True
        if temp != player.head:
            player.frame = 0
            player.head = temp
        if movement:
            if player.frame == 2:
                player.frame = 0
            else:
                player.frame += 1

        DrawAll()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    if player.bomb_limit == 0:
                        continue
                    temp_bomb = player.plantbomb(map)
                    bombs.append(temp_bomb)
                    map[temp_bomb.x][temp_bomb.y] = 3
                    player.bomb_limit -= 1

        update_bombs(timer)
    endgame()

def createmap():

    for i in range(1, len(map) - 1):
        for j in range(1, len(map[i]) - 1):
            if map[i][j] != 0:
                continue
            elif (i < 3 or i > len(map) - 4) and (j < 3 or j > len(map[i]) - 4):
                continue
            if random.randint(0, 9) < 7:
                map[i][j] = 2

    return


def DrawAll():
    screen.fill(background)
    for i in range(len(map)):
        for j in range(len(map[i])):
            screen.blit(terrain_images[map[i][j]], (i * width, j * height, height, width))

    for x in bombs:
        screen.blit(bomb_images[x.frame], (x.x * width, x.y * height, height, width))

    for y in explode:
        for x in y.sectors:
            screen.blit(explosion_images[y.frame], (x[0] * width, x[1] * height, height, width))
    if player.life:
        screen.blit(player.animation[player.head][player.frame],
               (player.x * (width / 4), player.y * (height / 4), width, height))
    for bot in other_list:
        if bot.life:
            screen.blit(bot.animation[bot.head][bot.frame],
                   (bot.x * (width / 4), bot.y * (height / 4), width, height))
            if show_path:
                if bot.ia == IA.PATH:
                    for bb in bot.path:
                        pygame.draw.rect(screen, (255, 0, 0, 240), [bb[0] * width, bb[1] * height, width, width], 1)
                else:
                    for bb in bot.path:
                        pygame.draw.rect(screen, (255, 0, 255, 240), [bb[0] * width, bb[1] * height, width, width], 1)

    pygame.display.update()

def update_bombs(timer):
    for bomb in bombs:
        bomb.update(timer)
        if bomb.timer < 1:
            bomb.bomber.bomb_limit += 1
            map[bomb.x][bomb.y] = 0
            exp = Explode(bomb.x, bomb.y, bomb.range)
            exp.explode(map, bombs, bomb)
            exp.clear_sectors(map)
            explode.append(exp)
    if player not in other_list:
        player.dead(explode)
    for bot in other_list:
        bot.dead(explode)
    for e in explode:
        e.update(timer)
        if e.time < 1:
            explode.remove(e)



def endgame():

    while True:
        timer = clock.tick(15)
        update_bombs(timer)
        count = 0
        winner = ""
        for bot in other_list:
            bot.make_move(map, bombs, explode, blocks)
            if bot.life:
                count += 1
                winner = bot.ia.name
        if count == 1:
            DrawAll()
            if winner == "PERSO":
                winner == "IA"
            textsurface = font.render(winner + " à gagner", False, (0, 0, 0))
            font_w = textsurface.get_width()
            font_h = textsurface.get_height()
            screen.blit(textsurface, (screen.get_width() // 2 - font_w//2,  screen.get_height() // 2 - font_h//2))
            pygame.display.update()
            time.sleep(2)
            break
        if count == 0:
            DrawAll()
            textsurface = font.render("égalité", False, (0, 0, 0))
            font_w = textsurface.get_width()
            font_h = textsurface.get_height()
            screen.blit(textsurface, (screen.get_width() // 2 - font_w//2, screen.get_height() // 2 - font_h//2))
            pygame.display.update()
            time.sleep(2)
            break
        DrawAll()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
    explode.clear()
    other_list.clear()
    blocks.clear()