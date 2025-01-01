import pygame as pg
import draw_board as db
import pieces as pcs
import check_options as chop

pg.init()
WIDTH = 1300
HEIGHT = 900
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Two-Player Laser Chess')
font = pg.font.Font('freesansbold.ttf', 18)
big_font = pg.font.Font('freesansbold.ttf', 50)
timer = pg.time.Clock()
fps = 60

valid_moves = []
main_click_coords = ()
click_coords = ()

def counter():
    pg.draw.rect(screen, 'white', [1000, 100, 300, 500])
    screen.blit(font.render(f'turn step: {pcs.turn_step}', True, 'black'), (1010, 110))
    screen.blit(font.render(f'selection: {pcs.selection}', True, 'black'), (1010, 135))
    screen.blit(font.render(f'main click coords: {main_click_coords}', True, 'black'), (1010, 160))
    screen.blit(font.render(f'click coords: {click_coords}', True, 'black'), (1010, 185))

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill((255, 239, 226))
    counter()
    db.draw_board()
    pcs.draw_pieces()

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
            if pcs.turn_step <= 1:
                if main_click_coords in pcs.blue_locations:
                    pcs.selection = pcs.blue_locations.index(main_click_coords)
                    if pcs.turn_step == 0:
                        pcs.turn_step = 1

                if main_click_coords in valid_moves and pcs.selection != 100:
                    pcs.blue_locations[pcs.selection] = main_click_coords
                    chop.red_options = chop.check_options(pcs.red_pieces, pcs.red_locations, 'red')
                    chop.blue_options = chop.check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
                    pcs.turn_step = 2
                    pcs.selection = 100
                    valid_moves = []
                if pcs.selection != 12 and pcs.selection != 0 and pcs.selection != 100:
                    if 1090 <= click_coords[0] <= 1160 and 335 <= click_coords[1] <= 405:
                        #pcs.blue_images[pcs.piece_list.index(pcs.pieces[pcs.selection])] = \
                        #pg.transform.rotate(pcs.blue_images[pcs.piece_list.index(pcs.pieces[pcs.selection])], 90)
                        if pcs.turn_step == 1:
                            pcs.turn_step = 2
                            pcs.selection = 100
            if pcs.turn_step > 1:
                if main_click_coords in pcs.red_locations:
                    pcs.selection = pcs.red_locations.index(main_click_coords)
                    if pcs.turn_step == 2:
                        pcs.turn_step = 3
                if main_click_coords in valid_moves and pcs.selection != 100:
                    pcs.red_locations[pcs.selection] = main_click_coords
                    chop.red_options = chop.check_options(pcs.pieces, pcs.red_locations, 'red')
                    chop.blue_options = chop.check_options(pcs.pieces, pcs.blue_locations, 'blue')
                    pcs.turn_step = 0
                    pcs.selection = 100
                    valid_moves = []
    pg.display.flip()
pg.quit()
