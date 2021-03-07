import pygame
import pygame_menu
try:
    from initGame import *
    from AI import *
except ImportError: 
    from main.initGame import *
    from main.AI import *


fps = 60.0

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
    initGame(show_path, player_ia, ennemi1_ia, ennemi2_ia, ennemi3_ia, size)


def main_background():
    global surface
    surface.fill((153, 153, 255))


def menu_loop():
    pygame.init()

    pygame.display.set_caption('Bomber-Man-Python')
    clock = pygame.time.Clock()


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
    play_options.add_selector("Character 1", [("Player", IA.PLAYER), ("Bot", IA.PERSO), ("None", IA.NONE)], onchange=change_player)
    play_options.add_selector("Character 2", [("Bot", IA.PERSO), ("None", IA.NONE)], onchange=change_enemy1)
    play_options.add_selector("Character 3", [("Bot", IA.PERSO), ("None", IA.NONE)], onchange=change_enemy2,  default=1)
    play_options.add_selector("Character 4", [("Bot", IA.PERSO), ("None", IA.NONE)], onchange=change_enemy3)
    play_options.add_selector("PATH", [("Yes", True), ("No", False)], onchange=change_path)

    play_options.add_button('Back', pygame_menu.events.BACK)
    play_menu.add_button('Start',
                         run_game)

    play_menu.add_button('Options', play_options)
    play_menu.add_button('Quit', pygame_menu.events.EXIT)

    
    while True:

        clock.tick(fps)

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
