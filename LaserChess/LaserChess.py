import pygame as pg
import draw_board as db
import pieces as pcs

pg.init()
WIDTH = 1200
HEIGHT = 900
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Two-Player Laser Chess')
font = pg.font.Font('freesansbold.ttf', 20)
big_font = pg.font.Font('freesansbold.ttf', 50)
timer = pg.time.Clock()
fps = 60


destroyed_blue_pieces = []
destroyed_red_pieces = []
valid_moves = []



turn_step = 0
selection = 100

# valid options on board
def check_options():
    pass

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill((255, 239, 226))
    db.draw_board()
    pcs.draw_pieces()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords in pcs.blue_locations:
                    selection = pcs.blue_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    pcs.blue_locations[selection] = click_coords
                    if click_coords in pcs.red_locations:
                        pcs.red_piece = pcs.red_locations.index(click_coords)
                        pcs.captured_pieces_blue.append(pcs.red_pieces[[pcs.red_piece]])
                        pcs.red_pieces.pop(pcs.red_piece)
                        pcs.red_locations.pop(pcs.red_piece)
                    red_options = check_options(pcs.red_pieces, pcs.red_locations, 'red')
                    blue_options = check_options(pcs.blue_pieces, pcs.blue_locations, 'red')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords in pcs.red_locations:
                    selection = pcs.red_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    pcs.red_locations[selection] = click_coords
                    if click_coords in pcs.blue_locations:
                        pcs.blue_piece = pcs.blue_locations.index(click_coords)
                        pcs.captured_pieces_red.append(pcs.blue_pieces[[pcs.blue_piece]])
                        pcs.blue_pieces.pop(pcs.blue_piece)
                        pcs.blue_locations.pop(pcs.blue_piece)
                    red_options = check_options(pcs.red_pieces, pcs.red_locations, 'red')
                    blue_options = check_options(pcs.blue_pieces, pcs.blue_locations, 'red')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
    pg.display.flip()
pg.quit()