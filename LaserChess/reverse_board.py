import pygame as pg
import pieces as pcs
import check_options as chop
import draw_board as db
from variables import screen

def draw_reverse_button():
    reverse = pg.transform.scale(pg.image.load('img/reverse.webp'), (80, 80))
    reverse.set_colorkey((255, 255, 255))
    pg.draw.circle(screen, 'white', (1200, 700), 50)
    screen.blit(reverse, (1160, 660))

def reverse_board():
    db.board_rotate = db.board_rotate + 180
    if db.board_rotate == 360:
        db.board_rotate = 0
    db.board = pg.transform.rotate(db.board, 180)
    for i in range(len(chop.blocked_blue_coords)):
        chop.blocked_blue_coords[i] = (9 - chop.blocked_blue_coords[i][0], 7 - chop.blocked_blue_coords[i][1])
    for i in range(len(chop.blocked_red_coords)):
        chop.blocked_red_coords[i] = (9 - chop.blocked_red_coords[i][0], 7 - chop.blocked_red_coords[i][1])

    for i in range(len(pcs.blue_pieces)):
        pcs.blue_locations[i] = (9 - pcs.blue_locations[i][0], 7 - pcs.blue_locations[i][1])
        if pcs.blue_pieces[i] != 'switch':
            if pcs.blue_rotates[i] == 90:
                pcs.blue_rotates[i] = -90
            elif pcs.blue_rotates[i] == -90:
                pcs.blue_rotates[i] = 90
            else:
                pcs.blue_rotates[i] = 180 - pcs.blue_rotates[i]
        if pcs.blue_pieces[i] != 'king':
            pcs.blue_images[i] = pg.transform.rotate(pcs.blue_images[i], 180)

    for i in range(len(pcs.red_pieces)):
        pcs.red_locations[i] = (9 - pcs.red_locations[i][0], 7 - pcs.red_locations[i][1])
        if pcs.red_pieces[i] != 'switch':
            if pcs.red_rotates[i] == 90:
                pcs.red_rotates[i] = -90
            elif pcs.red_rotates[i] == -90:
                pcs.red_rotates[i] = 90
            else:
                pcs.red_rotates[i] = 180 - pcs.red_rotates[i]
        if pcs.red_pieces[i] != 'king':
            pcs.red_images[i] = pg.transform.rotate(pcs.red_images[i], 180)

    chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
    chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')