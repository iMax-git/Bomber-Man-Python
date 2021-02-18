import pygame
import pygame_menu

import initGame
from AI import IA

Keys = {"UP":273,"DOWN":274,"RIGHT":276,"LEFT":274, "A":113, "B":98, "C":99, "D":100, "E":101, "F":102,
         "G":103, "H":104, "I":105, "J":106, "K":107, "M":59, "N":110, "O":111, "P":112, "Q":97, "R":114,
          "S":115, "T":116, "U":117, "V":118, "W":122, "X":120, "Y":121, "Z":119, "ESC":27}

width = 500
height = 1280
pygame.init()


pygame.display.set_caption("Pyreet-Fighter")
screen = pygame.display.set_mode(size=(height, width))


while True:
    pass




bg = (153, 153, 255)
black = (0, 0, 0)
white = (255, 255, 255)
fps = 60.0
bgcolor = (102, 102, 153)
titlecolor = (51, 51, 255)

pygame.display.init()
pyinfo = pygame.display.Info()
size = int(pyinfo.current_h * 0.035)
wsize = (13 * size, 13 * size)

clock = None
player_ia = IA.PLAYER
ennemi1_ia = IA.PERSO
ennemi2_ia = IA.PATH
ennemi3_ia = IA.PERSO
show_path = True
surface = pygame.display.set_mode(wsize)


def change_path(value, c):
    global show_path
    show_path = c


def change_player(value, c):
    global player_ia
    player_ia = c


def change_enemy1(value, c):
    global ennemi1_ia
    ennemi1_ia = c


def change_enemy2(value, c):
    global ennemi2_ia
    ennemi2_ia = c


def change_enemy3(value, c):
    global ennemi3_ia
    ennemi3_ia = c


def run_game():
    initGame.initGame(show_path, player_ia, ennemi1_ia, ennemi2_ia, ennemi3_ia, size)


def main_background():
    global surface
    surface.fill(bg)


def menu_loop():
    pygame.init()

    pygame.display.set_caption('Bomberman')
    clock = pygame.time.Clock()

    menu_theme = pygame_menu.themes.Theme(
        selection_color=white,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=int(size*0.8),
        title_font_color=black,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=black,
        widget_font_size=int(size*0.7),
        background_color=bgcolor,
        title_background_color=titlecolor,
        widget_shadow=False
    )

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
    play_options.add_selector("Character 1", [("Player", IA.PLAYER), ("DFS", IA.DFS),
                                              ("DIJKSTRA", IA.DIJKSTRA), ("None", IA.NONE)], onchange=change_player)
    play_options.add_selector("Character 2", [("DIJKSTRA", IA.DIJKSTRA), ("DFS", IA.DFS),
                                              ("None", IA.NONE)], onchange=change_enemy1)
    play_options.add_selector("Character 3", [("DIJKSTRA", IA.DIJKSTRA), ("DFS", IA.DFS),
                                              ("None", IA.NONE)], onchange=change_enemy2,  default=1)
    play_options.add_selector("Character 4", [("DIJKSTRA", IA.DIJKSTRA), ("DFS", IA.DFS),
                                              ("None", IA.NONE)], onchange=change_enemy3)
    play_options.add_selector("Show path", [("Yes", True), ("No", False)], onchange=change_path)

    play_options.add_button('Back', pygame_menu.events.BACK)
    play_menu.add_button('Start',
                         run_game)

    play_menu.add_button('Options', play_options)
    play_menu.add_button('Return  to  main  menu', pygame_menu.events.BACK)

    about_menu_theme = pygame_menu.themes.Theme(
        selection_color=white,
        widget_font=pygame_menu.font.FONT_BEBAS,
        title_font_size=size,
        title_font_color=black,
        title_font=pygame_menu.font.FONT_BEBAS,
        widget_font_color=black,
        widget_font_size=int(size*0.4),
        background_color=bgcolor,
        title_background_color=titlecolor,
        widget_shadow=False
    )

    about_menu = pygame_menu.Menu(theme=about_menu_theme,
        height=int(wsize[1] * 0.7),
        width=int(wsize[0] * 0.7),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='About'
    )
    about_menu.add_label("Player_controls: ")
    about_menu.add_label("Movement:_Arrows")
    about_menu.add_label("Plant bomb:_Space")
    about_menu.add_label("Author:_Michal_Sliwa")
    about_menu.add_label("Sprite: ")

    about_menu.add_label("https://opengameart.org/content")
    about_menu.add_label("/bomb-party-the-complete-set")

    main_menu = pygame_menu.Menu(
        theme=menu_theme,
        height=int(wsize[1] * 0.6),
        width=int(wsize[0] * 0.6),
        onclose=pygame_menu.events.DISABLE_CLOSE,
        title='Main menu'
    )

    main_menu.add_button('Play', play_menu)
    main_menu.add_button('About', about_menu)
    main_menu.add_button('Quit', pygame_menu.events.EXIT)
    while True:

        clock.tick(fps)

        main_background()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        main_menu.mainloop(surface, main_background, disable_loop=False, fps_limit=0)
        main_menu.update(events)
        main_menu.draw(surface)

        pygame.display.flip()


menu_loop()
