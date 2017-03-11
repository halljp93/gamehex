# gamehex
Generates a "Settlers of Catan" game board to be used in a tabletop display.

## Dependencies:
- python 3
- pygame

## Usage
    $python gamehex.py
    $python gamehex.py <height>
    $python gamehex.py <width> <height>
    
If no arguments are given, the window size defaults to 1500x1388.
Because height is the smaller dimension on most displays, one argument will adjust to the specified height while preserving the aspect ratio.
Passing two arguments will stretch the board to the specified dimensions.
