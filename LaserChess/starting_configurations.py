import pygame as pg
from variables import screen
import pieces as pcs

font = pg.font.Font('freesansbold.ttf', 18)
big_font = pg.font.Font('freesansbold.ttf', 70)
start_background = pg.transform.scale(pg.image.load('img/start_background.jpg'), (1400, 900))
classic = pg.transform.scale(pg.image.load('img/classic.png'), (380, 304))
imhotep = pg.transform.scale(pg.image.load('img/imhotep.png'), (380, 304))
dynasty = pg.transform.scale(pg.image.load('img/dynasty.png'), (380, 304))

def starting_configurations(choice, configuration):
    if not choice:
        return

    else:
        if configuration == 'classic':
            return

        if configuration == 'imhotep':

            pcs.blue_images = [pcs.blue_laser, pcs.blue_deflector90, pcs.blue_deflector, pcs.blue_deflector, \
                pcs.blue_deflector90, pcs.blue_deflector180, pcs.blue_deflector90, pcs.blue_deflector, \
                pcs.blue_defender, pcs.blue_defender, pcs.blue_switch90, pcs.blue_switch90, pcs.blue_king]

            pcs.red_images = [pcs.red_laser, pcs.red_deflector270, pcs.red_deflector180, pcs.red_deflector270, \
                pcs.red_deflector180, pcs.red_deflector180, pcs.red_deflector270, pcs.red_deflector, \
                pcs.red_defender, pcs.red_defender,pcs.red_switch90, pcs.red_switch90, pcs.red_king]

            pcs.blue_locations = [(9, 7), (9, 4), (9, 3), (3, 2), (3, 5), (4, 3), (1, 3), 
                                (1, 4), (3, 7), (5, 7), (4, 4), (2, 7), (4, 7)]

            pcs.red_locations = [(0, 0), (0, 3), (0, 4), (6, 2), (6, 5), (8, 3), (8, 4), 
                                (5, 4), (4, 0), (6, 0), (5, 3), (7, 0), (5, 0)]

            pcs.blue_rotates = [0, 90, 0, 0, 90, 180, 90, 0, 0, 0, 90, 90, 0]

            pcs.red_rotates = [0, -90, 180, -90, 180, 180, -90, 0, 0, 0, 90, 90, 0]

            return

        if configuration == 'dynasty':

            pcs.blue_images = [pcs.blue_laser, pcs.blue_deflector90, pcs.blue_deflector, pcs.blue_deflector180, \
                pcs.blue_deflector, pcs.blue_deflector270, pcs.blue_deflector270, pcs.blue_deflector, \
                pcs.blue_defender, pcs.blue_defender, pcs.blue_switch90, pcs.blue_switch, pcs.blue_king]

            pcs.red_images = [pcs.red_laser, pcs.red_deflector270, pcs.red_deflector180, pcs.red_deflector, \
                pcs.red_deflector180, pcs.red_deflector90, pcs.red_deflector90, pcs.red_deflector180, \
                pcs.red_defender, pcs.red_defender,pcs.red_switch, pcs.red_switch90, pcs.red_king]

            pcs.blue_locations = [(9, 7), (9, 5), (9, 4), (6, 3), (4, 3), (5, 5), (5, 7), 
                                (3, 7), (4, 5), (4, 7), (3, 5), (7, 4), (4, 6)]

            pcs.red_locations = [(0, 0), (0, 2), (0, 3), (3, 4), (5, 4), (4, 2), (4, 0), 
                                (6, 0), (5, 0), (5, 2), (2, 3), (6, 2), (5, 1)]

            pcs.blue_rotates = [0, 90, 0, 180, 0, -90, -90, 0, 0, 0, 90, 0, 0]

            pcs.red_rotates = [0, -90, 180, 0, 180, 90, 90, 180, 0, 0, 0, 90, 0]

            return

        screen.blit(start_background, (0, 0))
        screen.blit(classic, (80, 100))
        screen.blit(big_font.render(f'Classic', True, 'white'), (143, 440))
        screen.blit(imhotep, (510, 100))
        screen.blit(big_font.render(f'Imhotep', True, 'white'), (563, 440))
        screen.blit(dynasty, (940, 100))
        screen.blit(big_font.render(f'Dynasty', True, 'white'), (990, 440))

