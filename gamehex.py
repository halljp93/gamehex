from time import sleep
from random import shuffle
import sys
import pygame

pygame.init()

if len(sys.argv) == 2:
    size = int(1500 / 1388 * int(sys.argv[1])), int(sys.argv[1])
elif len(sys.argv) == 3:
    size = int(sys.argv[1]), int(sys.argv[2])
else:
    size = 1500, 1388

window = pygame.Surface((1500, 1388))
screen = pygame.display.set_mode(size)

#dimensions/key vertices of hex in its rect
TOP_LEFT = [60, 123]
TOP_RIGHT = [360, 123]
TOP = [210, 36]
HEX_WIDTH = 300
EDGE_LEN = 175
V_OFFSET = 260
H_PAD = 60
V_PAD = 36
#jhwe;l[p omwasm ][iuu jwre njy gayus

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

board = [
            [
                [HEX_WIDTH - H_PAD, -V_PAD],
                [HEX_WIDTH * 2 - H_PAD, -V_PAD],
                [HEX_WIDTH * 3 - H_PAD, -V_PAD]
            ],

            [

                [HEX_WIDTH / 2 - H_PAD, V_OFFSET - V_PAD],
                [HEX_WIDTH * 1.5  - H_PAD, V_OFFSET - V_PAD],
                [HEX_WIDTH * 2.5 - H_PAD, V_OFFSET - V_PAD],
                [HEX_WIDTH * 3.5 - H_PAD, V_OFFSET - V_PAD],
            ],

            [
                
                [-H_PAD, V_OFFSET * 2 - V_PAD],
                [HEX_WIDTH - H_PAD, V_OFFSET * 2 - V_PAD],
                [HEX_WIDTH * 2 - H_PAD, V_OFFSET * 2 - V_PAD],
                [HEX_WIDTH * 3 - H_PAD, V_OFFSET * 2 - V_PAD],
                [HEX_WIDTH * 4 - H_PAD, V_OFFSET * 2 - V_PAD],
            ],

            [
                
                [HEX_WIDTH / 2 - H_PAD, V_OFFSET * 3 - V_PAD],
                [HEX_WIDTH * 1.5 - H_PAD, V_OFFSET * 3 - V_PAD],
                [HEX_WIDTH * 2.5 - H_PAD, V_OFFSET * 3 - V_PAD],
                [HEX_WIDTH * 3.5 - H_PAD, V_OFFSET * 3 - V_PAD],
            ],

            [
                
                [HEX_WIDTH - H_PAD, V_OFFSET * 4 - V_PAD],
                [HEX_WIDTH * 2 - H_PAD, V_OFFSET * 4 - V_PAD],
                [HEX_WIDTH * 3 - H_PAD, V_OFFSET * 4 - V_PAD],
            ]
        ]

def put_number(coords):
    coords[0] += 185
    coords[1] += 185
    window.blit(pygame.image.load("pieces/numbers/%s.png" % numbers.pop()), coords)

def put_hex(coords):
    type = tiles.pop()
    window.blit(pygame.image.load("pieces/tiles/%s.png" % type), coords)
    if type != "desert":
        put_number(coords)
    else:
        pass

window.blit(pygame.image.load("pieces/ocean.jpg"), (0,0))

#draw tiles
for row in board:
    for position in row:
        put_hex(position)

def valid(row, tile):
    if tile > 0:
        if row > 0:
            if [row-1][tile-1] == "6" or [row-1][tile-1] == "8":
                return false
            elif [row - 1] [tile] == "6" or [row - 1][tile] == "8":
                return false
            else:
                pass
        else:
            pass
    elif [row][tile -1] == "6" or [row][tile -1] == "8":
        return false
    else:
            pass
    return true

newWindow = pygame.Surface(size)
pygame.transform.scale(window, size, newWindow)

screen.blit(newWindow, (0, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
