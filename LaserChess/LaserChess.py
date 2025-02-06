import pygame as pg
from variables import screen, valid_moves, click_coords, main_click_coords, conf, choice
import draw_board as db
import pieces as pcs
import check_options as chop
import laser as l
import restart as rst
import reverse_board as rv
import starting_configurations as sc

pg.init()

pg.display.set_caption('Two-Player Laser Chess')
font = pg.font.Font('freesansbold.ttf', 18)
timer = pg.time.Clock()
#pg.mouse.set_visible(False)
fps = 60

def counter():
    pass
    # pg.draw.rect(screen, 'white', [1000, 100, 300, 500])
    # screen.blit(font.render(f'turn step: {pcs.turn_step}', True, 'black'), (1010, 110))
    # screen.blit(font.render(f'selection: {pcs.selection}', True, 'black'), (1010, 135))
    # screen.blit(font.render(f'main click coords: {main_click_coords}', True, 'black'), (1010, 160))
    # screen.blit(font.render(f'click coords: {click_coords}', True, 'black'), (1010, 185))
    # if pcs.selection == 100:
    #     screen.blit(font.render(f'selected piece: not selected', True, 'black'), (1010, 210))
    # else:
    #     if pcs.turn_step <= 1:
    #         screen.blit(font.render(f'selected piece: {pcs.blue_pieces[pcs.selection]}', True, 'black'), (1010, 210))
    #         screen.blit(font.render(f'rotation: {pcs.blue_rotates[pcs.selection]}', True, 'black'), (1010, 235))
    #     else:
    #         screen.blit(font.render(f'selected piece: {pcs.red_pieces[pcs.selection]}', True, 'black'), (1010, 210))
    #         screen.blit(font.render(f'rotation: {pcs.red_rotates[pcs.selection]}', True, 'black'), (1010, 235))

#check = True

# main game loop
run = True

while run:
    timer.tick(fps)
    screen.fill((255, 239, 226))
    counter()
    db.draw_board()
    pcs.draw_pieces()
    rst.draw_restart_button()
    rv.draw_reverse_button()
    sc.starting_configurations(choice, conf)
    chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
    chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
    if conf != None:
        choice = False
    if pcs.selection != 100:
        valid_moves = chop.check_valid_moves()
        chop.draw_valid(valid_moves)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            main_click_coords = (x_coord, y_coord)
            click_coords = (event.pos[0], event.pos[1])

            if (click_coords[0] - 1070) ** 2 + (click_coords[1] - 700) ** 2 <= 2500:
                rst.restart()
                choice = True
                conf = None
            if (click_coords[0] - 1200) ** 2 + (click_coords[1] - 700) ** 2 <= 2500:
                rv.reverse_board()

            if conf == None:
                if 80 <= click_coords[0] <= 460 and 100 <= click_coords[1] <= 404:
                    conf = 'classic'
                    choice = True
                    pcs.turn_step = 0

                if 510 <= click_coords[0] <= 890 and 100 <= click_coords[1] <= 404:
                    conf = 'imhotep'
                    choice = True
                    pcs.turn_step = 0

                if 940 <= click_coords[0] <= 1320 and 100 <= click_coords[1] <= 404:
                    conf = 'dynasty'
                    choice = True
                    pcs.turn_step = 0

            if pcs.turn_step <= 1:
                if main_click_coords in pcs.blue_locations:
                    pcs.selection = pcs.blue_locations.index(main_click_coords)
                    if pcs.turn_step == 0:
                        pcs.turn_step = 1
                if pcs.selection != 100 and pcs.blue_pieces[pcs.selection] != 'switch' and \
                    main_click_coords in valid_moves:
                    pcs.blue_locations[pcs.selection] = main_click_coords
                    chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
                    chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
                    pcs.turn_step = 2
                    pcs.selection = 100
                    valid_moves = []
                    db.draw_board()
                    pcs.draw_pieces()
                    l.blue_laser()

                if pcs.selection != 100 and pcs.blue_pieces[pcs.selection] == 'switch' and \
                    main_click_coords in valid_moves:
                    if main_click_coords in pcs.red_locations:
                        pcs.blue_locations[pcs.selection], pcs.red_locations[pcs.red_locations.index(main_click_coords)] = \
                        main_click_coords, pcs.blue_locations[pcs.selection]
                        chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
                        chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
                        pcs.turn_step = 2
                        pcs.selection = 100
                        valid_moves = []
                        db.draw_board()
                        pcs.draw_pieces()
                        l.blue_laser()

                    if main_click_coords not in pcs.blue_locations and main_click_coords not in pcs.red_locations:
                        pcs.blue_locations[pcs.selection] = main_click_coords
                        chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
                        chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
                        pcs.turn_step = 2
                        pcs.selection = 100
                        valid_moves = []
                        db.draw_board()
                        pcs.draw_pieces()
                        l.blue_laser()

                    #if pcs.turn_step <= 1 and main_click_coords in pcs.blue_locations:
                     #   print('f')
                      #  pcs.blue_locations[pcs.selection] = (3, 7) 
                     #   #pcs.blue_locations[pcs.blue_locations.index(main_click_coords)] = \
                     #   #main_click_coords, pcs.blue_locations[11]
                     #   chop.red_options = chop.check_options(pcs.blue_pieces, pcs.red_locations, 'red')
                     #   chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
                     #   pcs.turn_step = 2
                      #  valid_moves = []
                     #   pcs.selection = 100

                if pcs.selection != 100 and pcs.blue_pieces[pcs.selection] != 'king' and pcs.blue_pieces[pcs.selection] != 'laser':
                    if (click_coords[0] - 1125) ** 2 + (click_coords[1] - 370) ** 2 <= 35 ** 2:
                        pcs.blue_images[pcs.selection] = pg.transform.rotate(pcs.blue_images[pcs.selection], 90)
                        pcs.blue_rotates[pcs.selection] += 90
                        if pcs.blue_pieces[pcs.selection] == 'deflector' or 'defender':
                            if pcs.blue_rotates[pcs.selection] == 270:
                                pcs.blue_rotates[pcs.selection] = -90
                        if pcs.blue_pieces[pcs.selection] == 'switch':
                            if pcs.blue_rotates[pcs.selection] == 180:
                                pcs.blue_rotates[pcs.selection] = 0
                        if pcs.turn_step == 1:
                            pcs.turn_step = 2
                            pcs.selection = 100
                            valid_moves = []
                            db.draw_board()
                            pcs.draw_pieces()
                            l.blue_laser()

                    if (click_coords[0] - 1125) ** 2 + (click_coords[1] - 480) ** 2 <= 35 ** 2:
                        pcs.blue_images[pcs.selection] = pg.transform.rotate(pcs.blue_images[pcs.selection], -90)
                        pcs.blue_rotates[pcs.selection] -= 90
                        if pcs.blue_pieces[pcs.selection] == 'deflector' or 'defender':
                            if pcs.blue_rotates[pcs.selection] == -270:
                                pcs.blue_rotates[pcs.selection] = 90
                            if pcs.blue_rotates[pcs.selection] == -180:
                                pcs.blue_rotates[pcs.selection] = 180
                        if pcs.blue_pieces[pcs.selection] == 'switch':
                            if pcs.blue_rotates[pcs.selection] == -90:
                                pcs.blue_rotates[pcs.selection] = 90
                        if pcs.turn_step == 1:
                            pcs.turn_step = 2
                            pcs.selection = 100
                            valid_moves = []
                            db.draw_board()
                            pcs.draw_pieces()
                            l.blue_laser()

            if 4 > pcs.turn_step > 1:
                if main_click_coords in pcs.red_locations:
                    pcs.selection = pcs.red_locations.index(main_click_coords)
                    if pcs.turn_step == 2:
                        pcs.turn_step = 3
                if pcs.selection != 100 and pcs.red_pieces[pcs.selection] != 'switch' and \
                    main_click_coords in valid_moves:
                    pcs.red_locations[pcs.selection] = main_click_coords
                    chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
                    chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
                    pcs.turn_step = 0
                    pcs.selection = 100
                    valid_moves = []
                    db.draw_board()
                    pcs.draw_pieces()
                    l.red_laser()

                if pcs.selection != 100 and pcs.red_pieces[pcs.selection] == 'switch' and \
                    main_click_coords in valid_moves:
                    if main_click_coords in pcs.blue_locations:
                        pcs.red_locations[pcs.selection], pcs.blue_locations[pcs.blue_locations.index(main_click_coords)] = \
                        main_click_coords, pcs.red_locations[pcs.selection]
                        chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
                        chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
                        pcs.turn_step = 0
                        pcs.selection = 100
                        valid_moves = []
                        db.draw_board()
                        pcs.draw_pieces()
                        l.red_laser()
                    else:
                        pcs.red_locations[pcs.selection] = main_click_coords
                        chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
                        chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
                        pcs.turn_step = 0
                        pcs.selection = 100
                        valid_moves = []
                        db.draw_board()
                        pcs.draw_pieces()
                        l.red_laser()

                if pcs.selection != 100 and pcs.red_pieces[pcs.selection] != 'king' and \
                    pcs.red_pieces[pcs.selection] != 'laser':
                    if (click_coords[0] - 1125) ** 2 + (click_coords[1] - 370) ** 2 <= 35 ** 2:
                        pcs.red_images[pcs.selection] = pg.transform.rotate(pcs.red_images[pcs.selection], 90)
                        pcs.red_rotates[pcs.selection] += 90
                        if pcs.red_pieces[pcs.selection] == 'deflector' or 'defender':
                            if pcs.red_rotates[pcs.selection] == 270:
                                pcs.red_rotates[pcs.selection] = -90
                        if pcs.red_pieces[pcs.selection] == 'switch':
                            if pcs.red_rotates[pcs.selection] == 180:
                                pcs.red_rotates[pcs.selection] = 0
                        if pcs.turn_step == 3:
                            pcs.turn_step = 0
                            pcs.selection = 100
                            valid_moves = []
                            db.draw_board()
                        pcs.draw_pieces()
                        l.red_laser()

                    if (click_coords[0] - 1125) ** 2 + (click_coords[1] - 480) ** 2 <= 35 ** 2:
                        pcs.red_images[pcs.selection] = pg.transform.rotate(pcs.red_images[pcs.selection], -90)
                        pcs.red_rotates[pcs.selection] -= 90
                        if pcs.red_pieces[pcs.selection] == 'deflector' or 'defender':
                            if pcs.red_rotates[pcs.selection] == -270:
                                pcs.red_rotates[pcs.selection] = 90
                            if pcs.red_rotates[pcs.selection] == -180:
                                pcs.red_rotates[pcs.selection] = 180
                        if pcs.red_pieces[pcs.selection] == 'switch':
                            if pcs.red_rotates[pcs.selection] == -90:
                                pcs.red_rotates[pcs.selection] = 90
                        if pcs.turn_step == 3:
                            pcs.turn_step = 0
                            pcs.selection = 100
                            valid_moves = []
                            db.draw_board()
                            pcs.draw_pieces()
                            l.red_laser()
    pg.display.flip()
pg.quit()

