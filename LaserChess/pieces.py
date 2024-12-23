import pygame as pg

WIDTH = 1200
HEIGHT = 900
screen = pg.display.set_mode([WIDTH, HEIGHT])

turn_step = 0
selection = 100

blue_pieces = ['laser', 'reflector', 'reflector', 'reflector', 'reflector', 'reflector', 'reflector', 'reflector', 
               'defender', 'defender', 'key', 'key', 'king']
blue_locations = [(9, 7), (9, 4), (9, 3), (7, 6), (2, 7), (2, 4), (2, 3), 
                  (3, 2), (3, 7), (5, 7), (4, 4), (5, 4), (4, 7)]
red_pieces = ['laser', 'reflector', 'reflector', 'reflector', 'reflector', 'reflector', 'reflector', 'reflector', 
              'defender', 'defender', 'key', 'key', 'king']
red_locations = [(0, 0), (2, 1), (7, 0), (0, 3), (0, 4), (7, 3), (7, 4), 
                  (6, 5), (4, 0), (6, 0), (4, 3), (5, 3), (5, 0)]


#blue
blue_laser = pg.image.load('img/laser.jpg')
blue_laser = pg.transform.scale(blue_laser, (80, 80))

blue_reflector = pg.image.load('img/reflector.webp')
blue_reflector = pg.transform.scale(blue_reflector, (80, 80))

blue_defender = pg.image.load('img/defender.jpg')
blue_defender = pg.transform.scale(blue_defender, (80, 80))

blue_key = pg.image.load('img/key.webp')
blue_key = pg.transform.scale(blue_key, (80, 80))

blue_king = pg.image.load('img/king.jpg')
blue_king = pg.transform.scale(blue_king, (80, 80))

#red
red_laser = pg.image.load('img/red_laser.jpg')
red_laser = pg.transform.scale(red_laser, (80, 80))

red_reflector = pg.image.load('img/red_reflector.jpg')
red_reflector = pg.transform.scale(red_reflector, (80, 80))

red_defender = pg.image.load('img/red_defender.jpeg')
red_defender = pg.transform.scale(red_defender, (80, 80))

red_key = pg.image.load('img/red_key.webp')
red_key = pg.transform.scale(red_key, (80, 80))

red_king = pg.image.load('img/red_king.jpg')
red_king = pg.transform.scale(red_king, (80, 80))

blue_images = [blue_laser, blue_reflector, blue_defender, blue_key, blue_king]
red_images = [red_laser, red_reflector, red_defender, red_key, red_king]

piece_list = ['laser', 'reflector', 'defender', 'key', 'king']

captured_pieces_blue = []
captured_pices_red = []
def draw_pieces():
    for i in range(len(blue_pieces)):
        index = piece_list.index(blue_pieces[i])
        if blue_pieces[i] == 'laser':
            screen.blit(blue_laser, (blue_locations[i][0] * 100 + 11, blue_locations[i][1] * 100 + 11))
        else:
            screen.blit(blue_images[index], (blue_locations[i][0] * 100 + 11, blue_locations[i][1] * 100 + 11))
        if turn_step < 2:
            if selection == i:
                pg.draw.rect(screen, 'red', [blue_locations[i][0] * 100 + 1, blue_locations[i][1] * 100 + 1,
                                             100, 100], 2)

    for i in range(len(red_pieces)):
        index = piece_list.index(red_pieces[i])
        if red_pieces[i] == 'laser':
            screen.blit(red_laser, (red_locations[i][0] * 100 + 11, red_locations[i][1] * 100 + 11))
        else:
            screen.blit(red_images[index], (red_locations[i][0] * 100 + 11, red_locations[i][1] * 100 + 11))
        if turn_step >= 2:
            if selection == i:
                pg.draw.rect(screen, 'red', [red_locations[i][0] * 100 + 1, red_locations[i][1] * 100 + 1,
                                             100, 100], 2)