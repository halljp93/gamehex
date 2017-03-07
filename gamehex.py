from time import sleep
from random import shuffle
import sys
import pygame

pygame.init()
BLUE = 0, 0, 255
size = 1366, 768
screen = pygame.display.set_mode(size)

#dimensions/key vertices of hex in its rect
TOP_LEFT = [60, 123]
TOP_RIGHT = [360, 123]
TOP = [210, 36]
HEX_WIDTH = 300
EDGE_LEN = 175
VERT_OFFSET = 260


tiles = [
        "brick",
        "brick",
        "brick",
        "ore",
        "ore",
        "ore",
        "sheep",
        "sheep",
        "sheep",
        "sheep",
        "wood",
        "wood",
        "wood",
        "wood",
        "wheat",
        "wheat",
        "wheat",
        "wheat",
        "desert"
        ]
numbers = [
        "2",
        "2",
        "3",
        "3",
        "4",
        "4",
        "5",
        "5",
        "6",
        "6",
        "8",
        "8",
        "9",
        "9",
        "10",
        "10",
        "11",
        "11",
        "12"
        ]
shuffle(tiles)
shuffle(numbers)

tile = 0
number = 0

#maybe will simplify placement on screen, currently unused
board = [
        #first row
        [HEX_WIDTH - 60, -36],
        [HEX_WIDTH * 2 - 60, -36],
        [HEX_WIDTH * 3 - 60, -36],
        #second row
        [HEX_WIDTH / 2 - 60, 224],
        [HEX_WIDTH - 60, 224],
        [HEX_WIDTH * 3 / 2 - 60, 224],
        [HEX_WIDTH * 2 - 60, 224],
        #third row
        [HEX_WIDTH - 60, 484],
        [HEX_WIDTH * 2 - 60, 484],
        [HEX_WIDTH * 3 - 60, 484],
        [HEX_WIDTH * 4 - 60, 484],
        [HEX_WIDTH * 5 - 60, 484],
        #fourth row
        [HEX_WIDTH / 2 - 60, 744],
        [HEX_WIDTH - 60, 224],
        [HEX_WIDTH * 3 / 2 - 60, 744],
        [HEX_WIDTH * 2 - 60, 744],
        #fifth row
        [HEX_WIDTH - 60, 1004],
        [HEX_WIDTH * 2 - 60, 1004],
        [HEX_WIDTH * 3 - 60, 1004],
        ]

screen.fill(BLUE)

#draws first three rows of board accounting for dead space in png
for i in range(1, 4):
    screen.blit(pygame.image.load("pieces/tiles/%s.png" % tiles[tile]), (HEX_WIDTH * i - 60, -36))
    tile += 1
for i in range(1, 5):
    screen.blit(pygame.image.load("pieces/tiles/%s.png" % tiles[tile]), ((HEX_WIDTH * i) - (HEX_WIDTH / 2) - 60, 224))
    tile += 1
for i in range(0, 6):
    screen.blit(pygame.image.load("pieces/tiles/%s.png" % tiles[tile]), ((HEX_WIDTH * i) - 60, 484))
    tile += 1

#testing number image
#screen.blit(pygame.image.load("pieces/numbers/%s.png" % numbers[number]), (50, 50))



pygame.display.flip()

while True:
    pygame.time.wait(1000) # don't know if this would reduce CPU
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
