import pygame as pg

pg.init()
WIDTH = 1200
HEIGHT = 900
font = pg.font.Font('freesansbold.ttf', 30)
screen = pg.display.set_mode([WIDTH, HEIGHT])

# rotate images
left_rotate = pg.transform.scale(pg.image.load('img/left_rotate.png'), (50, 45))
left_rotate.set_colorkey((250, 224, 202))
right_rotate = pg.transform.scale(pg.image.load('img/right_rotate.png'), (48, 53))
right_rotate.set_colorkey((250, 224, 202))

def draw_board():
    # draw board
    pg.draw.rect(screen, (226, 200, 182), [0, 0, 1000, 800], 0, 30)
    for i in range(10):
        pg.draw.line(screen, (255, 239, 226), (0, 100 * i), (1000, 100 * i), 3)
        pg.draw.line(screen, (255, 239, 226), (100 * i, 0), (100 * i, 800), 3)

    # draw blocked locations
    for i in range(7):
        pg.draw.rect(screen, (167, 205, 255), (925, 100 * i + 25, 50, 50), 0, 15)
        pg.draw.circle(screen, (116, 177, 255), (950, 100 * i + 50), 13)
    pg.draw.rect(screen, (167, 205, 255), (125, 25, 50, 50), 0, 15)
    pg.draw.circle(screen, (116, 177, 255), (150, 50), 13)
    pg.draw.rect(screen, (167, 205, 255), (125, 725, 50, 50), 0, 15)
    pg.draw.circle(screen, (116, 177, 255), (150, 750), 13)
    for i in range(1, 8):
        pg.draw.rect(screen, (255, 177, 177), (25, 100 * i + 25, 50, 50), 0, 15)
        pg.draw.circle(screen, (255, 134, 134), (50, 100 * i + 50), 13)
    pg.draw.rect(screen, (255, 177, 177), (825, 25, 50, 50), 0, 15)
    pg.draw.circle(screen, (255, 134, 134), (850, 50), 13)
    pg.draw.rect(screen, (255, 177, 177), (825, 725, 50, 50), 0, 15)
    pg.draw.circle(screen, (255, 134, 134), (850, 750), 13)

    # draw rotate button
    pg.draw.rect(screen, (222, 201, 184), (1050, 250, 150, 300), 0, 25)
    screen.blit(font.render('Rotate', True, (138, 124, 113)), (1076, 280))
    pg.draw.line(screen, (250, 224, 202), (1070, 425), (1180, 425), 5)
    pg.draw.circle(screen, (250, 224, 202), (1125, 370), 35)
    pg.draw.circle(screen, (250, 224, 202), (1125, 480), 35)
    screen.blit(left_rotate, (1102, 346))
    screen.blit(right_rotate, (1101, 453))
