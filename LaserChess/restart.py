import pygame as pg
import pieces as pcs
import draw_board as db
import check_options as chop
import variables as v

def draw_restart_button():
    restart = pg.transform.scale(pg.image.load('img/restart.webp'), (80, 80))
    restart.set_colorkey((255, 255, 255))
    pg.draw.circle(v.screen, 'white', (1070, 700), 50)
    v.screen.blit(restart, (1030, 660))

def restart():
    db.board = pg.transform.rotate(db.board, db.board_rotate)
    db.board_rotate = 0
    pcs.blue_locations = [(9, 7), (9, 4), (9, 3), (7, 6), (2, 7), (2, 4), (2, 3), 
                         (3, 2), (3, 7), (5, 7), (4, 4), (5, 4), (4, 7)]

    pcs.red_locations = [(0, 0), (2, 1), (7, 0), (0, 3), (0, 4), (7, 3), (7, 4), 
                        (6, 5), (4, 0), (6, 0), (4, 3), (5, 3), (5, 0)]

    pcs.blue_rotates = [0, 90, 0, -90, 0, 0, 90, 0, 0, 0, 90, 0, 0]

    pcs.red_rotates = [0, 90, 180, -90, 180, 180, -90, 180, 0, 0, 0, 90, 0]

    pcs.blue_images = [pcs.blue_laser, pcs.blue_deflector90, pcs.blue_deflector, pcs.blue_deflector270, pcs.blue_deflector, 
                         pcs.blue_deflector, pcs.blue_deflector90, pcs.blue_deflector, pcs.blue_defender, pcs.blue_defender,
                        pcs.blue_switch90, pcs.blue_switch, pcs.blue_king]

    pcs.red_images = [pcs.red_laser, pcs.red_deflector90, pcs.red_deflector180, pcs.red_deflector270, pcs.red_deflector180, 
                         pcs.red_deflector180, pcs.red_deflector270, pcs.red_deflector180, pcs.red_defender, pcs.red_defender,
                        pcs.red_switch, pcs.red_switch90, pcs.red_king]
    
    pcs.blue_pieces = ['laser', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 
               'defender', 'defender', 'switch', 'switch', 'king']

    pcs.red_pieces = ['laser', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 'deflector', 
                   'defender', 'defender', 'switch', 'switch', 'king']

    chop.blocked_blue_coords = [(8, 0), (8, 7), (9, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 0)]
    chop.blocked_red_coords = [(1, 0), (1, 7), (0, 0), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (9, 0)]
    chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
    chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
    pcs.selection = 100
    pcs.turn_step = 0