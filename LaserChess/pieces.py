import pygame as pg
import draw_board as db
from variables import screen

selection = 100
turn_step = 100

# blue
blue_laser = pg.image.load('img/blue_laser.png')
blue_laser = pg.transform.scale(blue_laser, (80, 80))
blue_laser.set_colorkey((250, 250, 250))

blue_deflector = pg.image.load('img/blue_deflector.png')
blue_deflector = pg.transform.scale(blue_deflector, (80, 80))
blue_deflector90 = pg.transform.rotate(blue_deflector, 90)
blue_deflector180 = pg.transform.rotate(blue_deflector, 180)
blue_deflector270 = pg.transform.rotate(blue_deflector, -90)

blue_defender = pg.image.load('img/blue_defender.png')
blue_defender = pg.transform.scale(blue_defender, (80, 80))

blue_switch = pg.image.load('img/blue_switch.png')
blue_switch = pg.transform.scale(blue_switch, (80, 80))
blue_switch90 = pg.transform.rotate(blue_switch, 90)

blue_king = pg.image.load('img/blue_king.png')
blue_king = pg.transform.scale(blue_king, (80, 80))

# red
red_laser = pg.image.load('img/red_laser.png')
red_laser = pg.transform.scale(red_laser, (80, 80))
red_laser = pg.transform.rotate(red_laser, 180)

red_deflector = pg.image.load('img/red_deflector.png')
red_deflector = pg.transform.scale(red_deflector, (80, 80))
red_deflector90 = pg.transform.rotate(red_deflector, 90)
red_deflector180 = pg.transform.rotate(red_deflector, 180)
red_deflector270 = pg.transform.rotate(red_deflector, -90)

red_defender = pg.image.load('img/red_defender.png')
red_defender = pg.transform.scale(red_defender, (80, 80))
red_defender = pg.transform.rotate(red_defender, 180)

red_switch = pg.image.load('img/red_switch.png')
red_switch = pg.transform.scale(red_switch, (80, 80))
red_switch90 = pg.transform.rotate(red_switch, 90)

red_king = pg.image.load('img/red_king.png')
red_king = pg.transform.scale(red_king, (80, 80))

blue_pieces = ['laser', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 
               'defender', 'defender', 'switch', 'switch', 'king']

red_pieces = ['laser', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 
               'defender', 'defender', 'switch', 'switch', 'king']

blue_locations = [(9, 7), (9, 4), (9, 3), (7, 6), (2, 7), (2, 4), (2, 3), 
                  (3, 2), (3, 7), (5, 7), (4, 4), (5, 4), (4, 7)]

red_locations = [(0, 0), (2, 1), (7, 0), (0, 3), (0, 4), (7, 3), (7, 4), 
                  (6, 5), (4, 0), (6, 0), (4, 3), (5, 3), (5, 0)]

blue_rotates = [0, 90, 0, -90, 0, 0, 90, 0, 0, 0, 90, 0, 0]

red_rotates = [0, 90, 180, -90, 180, 180, -90, 180, 0, 0, 0, 90, 0]

blue_images = [blue_laser, blue_deflector90, blue_deflector, blue_deflector270, blue_deflector, 
                          blue_deflector, blue_deflector90, blue_deflector, blue_defender, blue_defender,
                         blue_switch90, blue_switch, blue_king]

red_images = [red_laser, red_deflector90, red_deflector180, red_deflector270, red_deflector180, 
                          red_deflector180, red_deflector270, red_deflector180, red_defender, red_defender,
                         red_switch, red_switch90, red_king]

piece_list = ['laser', 'deflector', 'defender', 'switch', 'king']

def draw_pieces():
    for i in range(len(blue_pieces)):
        screen.blit(blue_images[i], (blue_locations[i][0] * 100 + 11, blue_locations[i][1] * 100 + 11))

        if turn_step < 2:
            if selection == i and blue_pieces[i] != 'laser' and blue_pieces[i] != 'king':
                pg.draw.rect(screen, 'yellow', [blue_locations[i][0] * 100 + 10.8, blue_locations[i][1] * 100 + 10.8,
                                             80, 80], 4, 15)
            if selection == i and blue_pieces[i] == 'king':
                pg.draw.rect(screen, 'yellow', [blue_locations[i][0] * 100 + 8, blue_locations[i][1] * 100 + 8,
                                             85, 85], 4, 15)
            if selection == i and blue_pieces[i] != 'laser' and blue_pieces[i] != 'king':
                pg.draw.circle(screen, 'green', (1125, 370), 35)
                pg.draw.circle(screen, 'green', (1125, 480), 35)
                screen.blit(db.left_rotate, (1102, 346))
                screen.blit(db.right_rotate, (1101, 453))


    for i in range(len(red_pieces)):
        screen.blit(red_images[i], (red_locations[i][0] * 100 + 11, red_locations[i][1] * 100 + 11))

        if turn_step >= 2:
            if selection == i and red_pieces[i] != 'laser' and red_pieces[i] != 'king':
                pg.draw.rect(screen, 'yellow', [red_locations[i][0] * 100 + 10.8, red_locations[i][1] * 100 + 10.8,
                                             80, 80], 4, 15)
            if selection == i and red_pieces[i] == 'king':
                pg.draw.rect(screen, 'yellow', [red_locations[i][0] * 100 + 8, red_locations[i][1] * 100 + 8,
                                             85, 85], 4, 15)
            if selection == i and red_pieces[i] != 'laser' and red_pieces[i] != 'king':
                pg.draw.circle(screen, 'green', (1125, 370), 35)
                pg.draw.circle(screen, 'green', (1125, 480), 35)
                screen.blit(db.left_rotate, (1102, 346))
                screen.blit(db.right_rotate, (1101, 453))