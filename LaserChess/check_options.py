import pygame as pg
import pieces as pcs
from variables import screen

def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        location = locations[i]
        piece = pieces[i]
        if piece == 'deflector':
            moves_list = check_piece_options(location, turn)
        elif piece == 'defender':
            moves_list = check_piece_options(location, turn)
        elif piece == 'king':
            moves_list = check_piece_options(location, turn)
        elif piece == 'switch':
            moves_list = check_switch_options(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

blocked_blue_coords = [(8, 0), (8, 7), (9, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 0)]
blocked_red_coords = [(1, 0), (1, 7), (0, 0), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (9, 0)]

# check valid deflector, king and defender moves
def check_piece_options(position, color):
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
        if color == 'blue' and target not in friends_list and target not in enemies_list and target \
            not in blocked_blue_coords and 0 <= target[0] <= 9 and 0 <= target[1] <= 7:
            moves_list.append(target)
        if color == 'red' and target not in friends_list and target not in enemies_list and target \
            not in blocked_red_coords and 0 <= target[0] <= 9 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_switch_options(position, color):
    moves_list = []
    targets = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    for i in range(8):
        f = True
        index = 0
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target in pcs.red_locations:
            index = pcs.red_locations.index(target)
            if pcs.red_pieces[index] == 'switch' or pcs.red_pieces[index] == 'king':
                f = False
        if target in pcs.blue_locations:
            index = pcs.blue_locations.index(target)
            if pcs.blue_pieces[index] == 'switch' or pcs.blue_pieces[index] == 'king':
                f = False
        if color == 'blue' and target not in blocked_blue_coords and 1 <= target[0] <= 9 and \
            0 <= target[1] <= 7 and target not in pcs.blue_locations and f:
            moves_list.append(target)
        if color == 'red' and target not in blocked_red_coords and 0 <= target[0] <= 8 and \
            0 <= target[1] <= 7 and target not in pcs.red_locations and f:
                moves_list.append(target)
    return moves_list

blue_options = check_options(pcs.blue_pieces, pcs.blue_locations, 'blue')
red_options = check_options(pcs.red_pieces, pcs.red_locations, 'red')


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
    for i in range(len(moves)):
        pg.draw.rect(screen, 'black', (moves[i][0] * 100 + 45, moves[i][1] * 100 + 45, 10, 10))