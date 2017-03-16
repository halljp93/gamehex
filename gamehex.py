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

class Tile():
    def __init__(self, x, y,):
        self.coords = (x, y)
        self.terrain = tiles.pop()
        self.visited = False
        self.number = None
        self.path = "pieces/tiles/%s.png" % self.terrain

    def draw(self):
        window.blit(pygame.image.load(self.path), self.coords)
        if self.number is not None:
            window.blit(pygame.image.load("pieces/numbers/%s.png" % self.number),
                    self.coords)

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
                Tile(HEX_WIDTH - H_PAD, -V_PAD),
                Tile(HEX_WIDTH * 2 - H_PAD, -V_PAD),
                Tile(HEX_WIDTH * 3 - H_PAD, -V_PAD),
            ],

            [

                Tile(HEX_WIDTH / 2 - H_PAD, V_OFFSET - V_PAD),
                Tile(HEX_WIDTH * 1.5  - H_PAD, V_OFFSET - V_PAD),
                Tile(HEX_WIDTH * 2.5 - H_PAD, V_OFFSET - V_PAD),
                Tile(HEX_WIDTH * 3.5 - H_PAD, V_OFFSET - V_PAD),
            ],

            [
                Tile(-H_PAD, V_OFFSET * 2 - V_PAD),
                Tile(HEX_WIDTH - H_PAD, V_OFFSET * 2 - V_PAD),
                Tile(HEX_WIDTH * 2 - H_PAD, V_OFFSET * 2 - V_PAD),
                Tile(HEX_WIDTH * 3 - H_PAD, V_OFFSET * 2 - V_PAD),
                Tile(HEX_WIDTH * 4 - H_PAD, V_OFFSET * 2 - V_PAD),
            ],

            [
                Tile(HEX_WIDTH / 2 - H_PAD, V_OFFSET * 3 - V_PAD),
                Tile(HEX_WIDTH * 1.5 - H_PAD, V_OFFSET * 3 - V_PAD),
                Tile(HEX_WIDTH * 2.5 - H_PAD, V_OFFSET * 3 - V_PAD),
                Tile(HEX_WIDTH * 3.5 - H_PAD, V_OFFSET * 3 - V_PAD),
            ],

            [
                Tile(HEX_WIDTH - H_PAD, V_OFFSET * 4 - V_PAD),
                Tile(HEX_WIDTH * 2 - H_PAD, V_OFFSET * 4 - V_PAD),
                Tile(HEX_WIDTH * 3 - H_PAD, V_OFFSET * 4 - V_PAD),
            ]
        ]

port_locations = [
        {'path': "pieces/ports/port1.png", 'coords': board[0][0].coords},
        {'path': "pieces/ports/port2.png", 'coords': board[0][1].coords},
        {'path': "pieces/ports/port3.png", 'coords': board[1][0].coords},
        {'path': "pieces/ports/port4.png", 'coords': board[1][3].coords},
        {'path': "pieces/ports/port5.png", 'coords': board[2][4].coords},
        {'path': "pieces/ports/port6.png", 'coords': board[3][0].coords},
        {'path': "pieces/ports/port7.png", 'coords': board[3][3].coords},
        {'path': "pieces/ports/port8.png", 'coords': board[4][0].coords},
        {'path': "pieces/ports/port9.png", 'coords': board[4][1].coords},
        ]

def put_number(row, tile):
    if board[row][tile].terrain != "desert":
        board[row][tile].number = numbers.pop()


def put_ports():
    for port in port_locations:
       window.blit(pygame.image.load(port['path']), port['coords'])

def valid(row, tile):
    try:
       return not board[row][tile].visited
    except IndexError:
        return False

def spiral(x, y):
    while valid(x, y):
        board[x][y].visited = True
        put_number(x, y)
        while valid(x + 1, y):
            x += 1
            board [x][y].visited = True
            put_number(x, y)
        while valid(x, y + 1):
            y += 1
            board[x][y].visited = True
            put_number(x, y)
        while valid(x - 1, y + 1):
            x -= 1
            y += 1
            board[x][y].visited = True
            put_number(x, y)
        while valid(x - 1, y - 1):
            x -= 1
            y -= 1
            board[x][y].visited = True
            put_number(x, y)
        while valid(x, y - 1):
            y -= 1
            board[x][y].visited = True
            put_number(x, y)
        x += 1


spiral(0, 0)

window.blit(pygame.image.load("pieces/ocean.jpg"), (0,0))

#draw tiles
for row in range(len(board)):
    for tile in range(len(board[row])):
        board[row][tile].draw()

put_ports()

newWindow = pygame.Surface(size)
pygame.transform.scale(window, size, newWindow)

screen.blit(newWindow, (0, 0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
