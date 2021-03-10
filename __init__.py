import pygame
import pygame_menu
import socket
try:
    from initGame import *
    from SELECT import *
except ImportError: 
    from main.initGame import *
    from main.SELECT import *



pygame.display.init()
pyinfo = pygame.display.Info()
size = int(pyinfo.current_h * 0.035)
wsize = (13 * size, 13 * size)

player_ia = SELECT.PLAYER
ennemi1_ia = SELECT.BOT
ennemi2_ia = SELECT.NONE
ennemi3_ia = SELECT.BOT
show_path = False
surface = pygame.display.set_mode(wsize)


host, port = ('',5566)
#https://www.youtube.com/watch?v=5FqzL9LJkXA
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket.connect((host, port))
    print("client connecter")
except :
    print("Connection Failed")
finally:
    socket.close()

def show_path(value, c):
    global show_path
    show_path = c


def select1(value, c):
    global player_ia
    player_ia = c


def select2(value, c):
    global ennemi1_ia
    ennemi1_ia = c


def select3(value, c):
    global ennemi2_ia
    ennemi2_ia = c


def select4(value, c):
    global ennemi3_ia
    ennemi3_ia = c


def start():
    initGame(show_path, player_ia, ennemi1_ia, ennemi2_ia, ennemi3_ia, size)

def startmultiplayer():
    pass

def main_background():
    global surface
    surface.fill((0, 0, 0))


def menu_loop():
    pygame.init()

    pygame.display.set_caption('Bomber-Man-Python')


    menu_theme = pygame_menu.themes.THEME_DEFAULT

    play_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(wsize[1] * 0.7),
        width=int(wsize[0] * 0.7),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Play menu'
    )

   
    play_options = pygame_menu.Menu(theme=menu_theme,
        height=int(wsize[1] * 0.7),
        width=int(wsize[0] * 0.7),
        title='Options'
    )
    
    play_multiplayer = pygame_menu.Menu(theme=menu_theme,
        height=int(wsize[1] * 0.7),
        width=int(wsize[0] * 0.7),
        title='Multiplayer'
    )
    
    play_options.add_selector("Player 1", [("Player", SELECT.PLAYER), ("Bot", SELECT.BOT), ("Rien", SELECT.NONE)], onchange=select1)
    play_options.add_selector("Player 2", [("Bot", SELECT.BOT), ("Rien", SELECT.NONE)], onchange=select2)
    play_options.add_selector("Player 3", [("Bot", SELECT.BOT), ("Rien", SELECT.NONE)], onchange=select3,  default=1)
    play_options.add_selector("Player 4", [("Bot", SELECT.BOT), ("Rien", SELECT.NONE)], onchange=select4)
    play_options.add_selector("Afficher les paths", [("Yes", True), ("No", False)], onchange=show_path)
    play_options.add_button('Arriere', pygame_menu.events.BACK)
    
    play_multiplayer.add_label("Connection:",max_char=-1, font_size=20)
    play_multiplayer.add_label("Player 1 -> "+"You",max_char=-1, font_size=20)
    play_multiplayer.add_label("Player 2 -> "+"None", max_char=-1, font_size=20)
    play_multiplayer.add_label("Player 3 -> "+"None", max_char=-1, font_size=20)
    play_multiplayer.add_label("Player 4 -> "+"None", max_char=-1, font_size=20)
    
    play_multiplayer.add_button('Lancer', startmultiplayer())
    play_multiplayer.add_button('Arriere', pygame_menu.events.BACK)


    play_menu.add_button('Lancer',start)
    play_menu.add_button('Multijoueur(CS)',play_multiplayer)
    play_menu.add_button('Options', play_options)
    play_menu.add_button('Quitter', pygame_menu.events.EXIT)

    
    while True:


        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        play_menu.mainloop(surface, main_background, disable_loop=False, fps_limit=0)
        play_menu.update(events)
        play_menu.draw(surface)

        pygame.display.flip()


menu_loop()
