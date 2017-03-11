# this started out as clean code
# I don't know what happened, I'm sorry

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
HEX_WIDTH = 300
V_OFFSET = 260
H_PAD = 60
V_PAD = 36

#Tom's line of code
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

#in "alphabetical" order for spiral placement
numbers = [
        "11",
        "3",
        "6",
        "5",
        "4",
        "9",
        "10",
        "8",
        "4",
        "11",
        "12",
        "9",
        "10",
        "8",
        "3",
        "6",
        "2",
        "5"
        ]

shuffle(tiles)

board = [
            [
                [HEX_WIDTH - H_PAD, -V_PAD, False, tiles.pop()          ],
                [HEX_WIDTH * 2 - H_PAD, -V_PAD, False, tiles.pop()      ],
                [HEX_WIDTH * 3 - H_PAD, -V_PAD, False, tiles.pop()      ]
            ],

            [

                [HEX_WIDTH / 2 - H_PAD, V_OFFSET - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 1.5  - H_PAD, V_OFFSET - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 2.5 - H_PAD, V_OFFSET - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 3.5 - H_PAD, V_OFFSET - V_PAD, False, tiles.pop()]
            ],

            [
                
                [-H_PAD, V_OFFSET * 2 - V_PAD, False, tiles.pop()       ],
                [HEX_WIDTH - H_PAD, V_OFFSET * 2 - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 2 - H_PAD, V_OFFSET * 2 - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 3 - H_PAD, V_OFFSET * 2 - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 4 - H_PAD, V_OFFSET * 2 - V_PAD, False, tiles.pop()]
            ],

            [
                
                [HEX_WIDTH / 2 - H_PAD, V_OFFSET * 3 - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 1.5 - H_PAD, V_OFFSET * 3 - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 2.5 - H_PAD, V_OFFSET * 3 - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 3.5 - H_PAD, V_OFFSET * 3 - V_PAD, False, tiles.pop()]
            ],

            [
                
                [HEX_WIDTH - H_PAD, V_OFFSET * 4 - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 2 - H_PAD, V_OFFSET * 4 - V_PAD, False, tiles.pop()],
                [HEX_WIDTH * 3 - H_PAD, V_OFFSET * 4 - V_PAD, False, tiles.pop()]
            ]
        ]

port_locations = [
        {'path': "pieces/ports/port1.png", 'x': board[0][0][0], 'y': board[0][0][1]},
        {'path': "pieces/ports/port2.png", 'x': board[0][1][0], 'y': board[0][1][1]},
        {'path': "pieces/ports/port3.png", 'x': board[1][0][0], 'y': board[1][0][1]},
        {'path': "pieces/ports/port4.png", 'x': board[1][3][0], 'y': board[1][3][1]},
        {'path': "pieces/ports/port5.png", 'x': board[2][4][0], 'y': board[2][4][1]},
        {'path': "pieces/ports/port6.png", 'x': board[3][0][0], 'y': board[3][0][1]},
        {'path': "pieces/ports/port7.png", 'x': board[3][3][0], 'y': board[3][3][1]},
        {'path': "pieces/ports/port8.png", 'x': board[4][0][0], 'y': board[4][0][1]},
        {'path': "pieces/ports/port9.png", 'x': board[4][1][0], 'y': board[4][1][1]}
        ]

def put_number(row, tile):
    coords = (board[row][tile][0], board[row][tile][1])
    if board[row][tile][3] != "desert":
       window.blit(pygame.image.load("pieces/numbers/%s.png" % numbers.pop()), coords) 

def put_hex(row, tile):
    type = board[row][tile][3]
    board[row][tile].append(type)
    coords = (board[row][tile][0], board[row][tile][1])
    window.blit(pygame.image.load("pieces/tiles/%s.png" % type), coords)

window.blit(pygame.image.load("pieces/ocean.jpg"), (0,0))

#draw tiles
for row in range(len(board)):
    for tile in range(len(board[row])):
        put_hex(row, tile)

def put_ports():
    for port in port_locations:
       window.blit(pygame.image.load(port['path']), (port['x'], port['y']))

def valid(row, tile):
    try:
       return not board[row][tile][2]
    except IndexError:
        return False

def spiral(x, y):
    while valid(x, y):
        board[x][y][2] = True
        put_number(x, y)
        while valid(x + 1, y):
            x += 1
            board [x][y][2] = True
            put_number(x, y)
        while valid(x, y + 1):
            y += 1
            board[x][y][2] = True
            put_number(x, y)
        while valid(x - 1, y + 1):
            x -= 1
            y += 1
            board[x][y][2] = True
            put_number(x, y)
        while valid(x - 1, y - 1):
            x -= 1
            y -= 1
            board[x][y][2] = True
            put_number(x, y)
        while valid(x, y - 1):
            y -= 1
            board[x][y][2] = True
            put_number(x, y)
        x += 1


spiral(0, 0)

put_ports()

newWindow = pygame.Surface(size)
pygame.transform.scale(window, size, newWindow)

screen.blit(newWindow, (0, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
