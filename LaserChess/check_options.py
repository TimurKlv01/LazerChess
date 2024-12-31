import pygame as pg
import pieces as pcs

WIDTH = 1300
HEIGHT = 900
screen = pg.display.set_mode([WIDTH, HEIGHT])

destroyed_blue_pieces = []
destroyed_red_pieces = []

def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'reflector':
            moves_list = check_normal_piece(location, turn)
        elif piece == 'defender':
            moves_list = check_normal_piece(location, turn)
        elif piece == 'king':
            moves_list = check_normal_piece(location, turn)
        elif piece == 'key':
            moves_list = check_normal_piece(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# check valid reflector, king and defender moves
blocked_blue_coords = [(8, 0), (8, 7)]
blocked_red_coords = [(1, 0), (1, 7)]

def check_normal_piece(position, color):
    moves_list = []
    if color == 'blue':
        enemies_list = pcs.red_locations
        friends_list = pcs.blue_locations
    if color == 'red':
        friends_list = pcs.red_locations
        enemies_list = pcs.blue_locations
    targets = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if color == 'blue' and target not in friends_list and target not in enemies_list and target not in blocked_blue_coords and 1 <= target[0] <= 9 and 0 <= target[1] <= 7:
            moves_list.append(target)
        if color == 'red' and target not in friends_list and target not in enemies_list and target not in blocked_red_coords and 0 <= target[0] <= 8 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

blue_options = check_options(pcs.pieces, pcs.blue_locations, 'blue')
red_options = check_options(pcs.pieces, pcs.red_locations, 'red')

# check for valid moves for just selected piece
def check_valid_moves():
    if pcs.turn_step < 2:
        options_list = blue_options
    else:
        options_list = red_options
    valid_options = options_list[pcs.selection]
    return valid_options

# draw valid moves on screen
def draw_valid(moves):
    if pcs.turn_step < 2:
        color = 'yellow'
    else:
        color = 'black'
    for i in range(len(moves)):
        pg.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)