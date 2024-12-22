import pygame
import LaserChess2

pygame.init()
WIDTH = 1200
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Laser Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# pieces
blue_pieces = LaserChess2.get_pieces()
blue_locations = []
red_pieces = LaserChess2.get_pieces()
red_locations =[]


def draw_board():
    for i in range(40):
        column = i % 5
        row = i // 5
        if row % 2 == 0:
            pygame.draw.rect(screen, (226, 200, 182), [800 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, (226, 200, 182), [900 - (column * 200), row * 100, 100, 100])

run = True
while run:
    timer.tick(fps)
    screen.fill((255, 239, 226))
    draw_board()
    # test2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()