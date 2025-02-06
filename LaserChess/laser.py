import pygame as pg
import pieces as pcs
import check_options as chop
import sys
from variables import screen
import draw_board as db
import time

sys.setrecursionlimit(5000)
font_l = pg.font.Font('freesansbold.ttf', 80)
#click = 1

# destroy piece
def destroy_blue_piece(x, y):
    pcs.blue_pieces.pop(pcs.blue_locations.index((x, y)))
    pcs.blue_rotates.pop(pcs.blue_locations.index((x, y)))
    pcs.blue_images.pop(pcs.blue_locations.index((x, y)))
    pcs.blue_locations.pop(pcs.blue_locations.index((x, y)))

def destroy_red_piece(x, y):
    pcs.red_pieces.pop(pcs.red_locations.index((x, y)))
    pcs.red_rotates.pop(pcs.red_locations.index((x, y)))
    pcs.red_images.pop(pcs.red_locations.index((x, y)))
    pcs.red_locations.pop(pcs.red_locations.index((x, y)))

# laser up
def laser_up(x_laser_coord, y_laser_coord):
    for i in range(10):
        y_laser_coord -= 100
        laser_coords = (x_laser_coord // 100, y_laser_coord // 100)
        if laser_coords[1] == -1:
            pg.draw.rect(screen, 'red', (x_laser_coord, y_laser_coord + 50, 8, 50))
            return
        else:
            pg.draw.rect(screen, 'red', (x_laser_coord, y_laser_coord, 8, 100))

        if (laser_coords[0], laser_coords[1]) in pcs.blue_locations:
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'deflector':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_left(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 180:
                    laser_right(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0 or -90:
                    destroy_blue_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'switch':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_right(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_left(x_laser_coord, y_laser_coord)
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'defender':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 180:
                    return
                else:
                    destroy_blue_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'king':
                destroy_blue_piece(laser_coords[0], laser_coords[1])
                screen.blit(font_l.render(f'Red player wins', True, 'red'), (150, 815))
                pcs.turn_step = 4
                return

        if (laser_coords[0], laser_coords[1]) in pcs.red_locations:
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'deflector':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_left(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 180:
                    laser_right(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0 or -90:
                    destroy_red_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'switch':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_right(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_left(x_laser_coord, y_laser_coord)
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'defender':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    return
                else:
                    destroy_red_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'king':
                destroy_red_piece(laser_coords[0], laser_coords[1])
                screen.blit(font_l.render(f'Blue player wins', True, 'blue'), (150, 815))
                pcs.turn_step = 4
                return

# laser down
def laser_down(x_laser_coord, y_laser_coord):
    for i in range(10):
        laser_coords = (x_laser_coord // 100, y_laser_coord // 100)
        if laser_coords[1] == 7:
            pg.draw.rect(screen, 'red', (x_laser_coord, y_laser_coord, 8, 50))
            return
        else:
            pg.draw.rect(screen, 'red', (x_laser_coord, y_laser_coord, 8, 108))
        y_laser_coord += 100
        laser_coords = (x_laser_coord // 100, y_laser_coord // 100)

        if (laser_coords[0], laser_coords[1]) in pcs.blue_locations:
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'deflector':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_left(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == -90:
                    laser_right(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 90 or 180:
                    destroy_blue_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'switch':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_right(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_left(x_laser_coord, y_laser_coord)
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'defender':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    return
                else:
                    destroy_blue_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'king':
                destroy_blue_piece(laser_coords[0], laser_coords[1])
                screen.blit(font_l.render(f'Red player wins', True, 'red'), (150, 815))
                pcs.turn_step = 4
                return

        if (laser_coords[0], laser_coords[1]) in pcs.red_locations:
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'deflector':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_left(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == -90:
                    laser_right(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 90 or 180:
                    destroy_red_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'switch':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_right(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_left(x_laser_coord, y_laser_coord)
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'defender':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 180:
                    return
                else:
                    destroy_red_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'king':
                destroy_red_piece(laser_coords[0], laser_coords[1])
                screen.blit(font_l.render(f'Blue player wins', True, 'blue'), (150, 815))
                pcs.turn_step = 4
                return

# laser right
def laser_right(x_laser_coord, y_laser_coord):
    for i in range(10):
        laser_coords = (x_laser_coord // 100, y_laser_coord // 100)
        if laser_coords[0] == 9:
            pg.draw.rect(screen, 'red', (x_laser_coord, y_laser_coord, 53, 8))
            return
        else:
            pg.draw.rect(screen, 'red', (x_laser_coord, y_laser_coord, 108, 8))
        x_laser_coord += 100
        laser_coords = (x_laser_coord // 100, y_laser_coord // 100)

        if (laser_coords[0], laser_coords[1]) in pcs.blue_locations:
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'deflector':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_up(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_down(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == -90 or 180:
                    destroy_blue_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'switch':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_up(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_down(x_laser_coord, y_laser_coord)
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'defender':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    return
                else:
                    destroy_blue_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'king':
                destroy_blue_piece(laser_coords[0], laser_coords[1])
                screen.blit(font_l.render(f'Red player wins', True, 'red'), (150, 815))
                pcs.turn_step = 4
                return

        if (laser_coords[0], laser_coords[1]) in pcs.red_locations:
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'deflector':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_up(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_down(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == -90 or 180:
                    destroy_red_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'switch':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_up(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_down(x_laser_coord, y_laser_coord)
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'defender':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == -90:
                    return
                else:
                    destroy_red_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'king':
                destroy_red_piece(laser_coords[0], laser_coords[1])
                screen.blit(font_l.render(f'Blue player wins', True, 'blue'), (150, 815))
                pcs.turn_step = 4
                return

# laser left
def laser_left(x_laser_coord, y_laser_coord):
    for i in range(10):
        laser_coords = (x_laser_coord // 100, y_laser_coord // 100)
        if laser_coords[0] == 0:
            pg.draw.rect(screen, 'red', (x_laser_coord - 45, y_laser_coord, 45, 8))
            return
        x_laser_coord -= 100
        laser_coords = (x_laser_coord // 100, y_laser_coord // 100)
        pg.draw.rect(screen, 'red', (x_laser_coord, y_laser_coord, 100, 8))

        if (laser_coords[0], laser_coords[1]) in pcs.blue_locations:
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'deflector':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == -90:
                    laser_up(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 180:
                    laser_down(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0 or 90:
                    destroy_blue_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'switch':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_up(x_laser_coord, y_laser_coord)
                    return
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_down(x_laser_coord, y_laser_coord)
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'defender':
                if pcs.blue_rotates[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == -90:
                    return
                else:
                    destroy_blue_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.blue_pieces[pcs.blue_locations.index((laser_coords[0], laser_coords[1]))] == 'king':
                destroy_blue_piece(laser_coords[0], laser_coords[1])
                screen.blit(font_l.render(f'Red player wins', True, 'red'), (150, 815))
                pcs.turn_step = 4
                return

        if (laser_coords[0], laser_coords[1]) in pcs.red_locations:
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'deflector':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == -90:
                    laser_up(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 180:
                    laser_down(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0 or 90:
                    destroy_red_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'switch':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 0:
                    laser_up(x_laser_coord, y_laser_coord)
                    return
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    laser_down(x_laser_coord, y_laser_coord)
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'defender':
                if pcs.red_rotates[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 90:
                    return
                else:
                    destroy_red_piece(laser_coords[0], laser_coords[1])
                    return
            if pcs.red_pieces[pcs.red_locations.index((laser_coords[0], laser_coords[1]))] == 'king':
                destroy_blue_piece(laser_coords[0], laser_coords[1])
                screen.blit(font_l.render(f'Blue player wins', True, 'blue'), (150, 815))
                pcs.turn_step = 4
                return

def blue_laser():
    if db.board_rotate == 0:
        laser_up(946, 750)
    else:
        laser_down(46, 50)
    chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
    chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
    pg.display.update()
    #click = 0
    time.sleep(1)
    #click = 1

def red_laser():
    if db.board_rotate == 0:
        laser_down(46, 50)
    else:
        laser_up(946, 750)
    chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
    chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
    pg.display.update()
    #click = 0
    time.sleep(1)
    #click = 1
