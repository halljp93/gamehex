from time import sleep
from random import shuffle
import sys
import pygame

pygame.init()
BLUE = 0, 0, 255
size = 1500, 1388
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
board = [
            [
                [HEX_WIDTH - 60, -36],
                [HEX_WIDTH * 2 - 60, -36],
                [HEX_WIDTH * 3 - 60, -36]
            ],

            [

                [HEX_WIDTH / 2 - 60, 224],
                [HEX_WIDTH * 1.5  - 60, 224],
                [HEX_WIDTH * 2.5 - 60, 224],
                [HEX_WIDTH * 3.5 - 60, 224],
            ],

            [
                
                [-60, 484],
                [HEX_WIDTH - 60, 484],
                [HEX_WIDTH * 2 - 60, 484],
                [HEX_WIDTH * 3 - 60, 484],
                [HEX_WIDTH * 4 - 60, 484],
            ],

            [
                
                [HEX_WIDTH / 2 - 60, 744],
                [HEX_WIDTH * 1.5 - 60, 744],
                [HEX_WIDTH * 2.5 - 60, 744],
                [HEX_WIDTH * 3.5 - 60, 744],
            ],

            [
                
                [HEX_WIDTH - 60, 1004],
                [HEX_WIDTH * 2 - 60, 1004],
                [HEX_WIDTH * 3 - 60, 1004],
            ]
        ]

def put_number(coords):
    coords[0] += 185
    coords[1] += 185
    screen.blit(pygame.image.load("pieces/numbers/%s.png" % numbers.pop()), coords)

def put_hex(coords):
    type = tiles.pop()
    screen.blit(pygame.image.load("pieces/tiles/%s.png" % type), coords)
    if type != "desert":
        put_number(coords)
    else:
        pass

screen.blit(pygame.image.load("pieces/ocean.jpg"), (0,0))

#draw tiles
for row in board:
    for position in row:
        put_hex(position)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
