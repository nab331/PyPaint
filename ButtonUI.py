import os
from Widgets import *


def create_buttons(output, painting):
    brush = MyButton(output, painting, os.path.join("Resources", "brush.png"), 25, 33, 100, 120, 'Brush',
                     ['*PAINT COLORS*', ' ', 'Current Size : '], Colors.coolred)
    pencil = MyButton(output, painting, os.path.join("Resources", "color_pencil.png"), 130, 39, 100, 120, 'Pencil',
                      ['*DRAW*', ' ', 'Current Size : '], Colors.carrot)
    eraser = MyButton(output, painting, os.path.join("Resources", "eraser.png"), 30, 176, 100, 120, 'Eraser',
                      ['*CLEARS SELECTED*', ' ', 'Current Size : '], Colors.coolblue)
    rbin = MyButton(output, painting, os.path.join("Resources", "bin.png"), 135, 176, 100, 120, 'Clear',
                    ['*CLEARS ALL*', ' ', 'Current Size : '], Colors.cloud)
    bplus = MyButton(output, painting, os.path.join("Resources", "plus.png"), 31, 510, 35, 45, 'Brush Size +',
                     ['**INCREASE SIZE**', 'Current Size : '], Colors.coolred)
    bminus = MyButton(output, painting, os.path.join("Resources", "minus.png"), 200, 510, 35, 50, 'Brush Size -',
                      ['**DECREASE SIZE**', 'Current Size : '], Colors.coolblue)
    cplus = MyButton(output, painting, os.path.join("Resources", "plus.png"), 31, 450, 35, 45, 'Darken Brush',
                     ['**INCREASE SIZE**', 'Current Size : '], Colors.coolred)
    cminus = MyButton(output, painting, os.path.join("Resources", "minus.png"), 200, 450, 35, 50, 'Lighten Brush',
                      ['**DECREASE SIZE**', 'Current Size : '], Colors.coolblue)

    buttons = [brush, pencil, eraser, rbin,
               bplus, bminus, cplus, cminus]

    return buttons


def create_color_button(output, painting):
    black_b = ColorButton(output, painting, Colors.black, 150, 330, 40, 50, 'Black')
    white_b = ColorButton(output, painting, Colors.white, 190, 330, 40, 50, 'White')
    red_b = ColorButton(output, painting, Colors.road_1, 50, 330, 20, 25, 'Road_1')
    cred_b = ColorButton(output, painting, Colors.coolred, 50, 350, 20, 25, 'Red')
    yellow_b = ColorButton(output, painting, Colors.yellow, 70, 330, 20, 25, 'Yellow')
    cyellow_b = ColorButton(output, painting, Colors.coolyellow, 70, 350, 20, 25, 'Yellow')
    blue_b = ColorButton(output, painting, Colors.blue, 90, 330, 20, 25, 'Blue')
    cblue_b = ColorButton(output, painting, Colors.coolblue, 90, 350, 20, 25, 'Blue')
    green_b = ColorButton(output, painting, Colors.green, 110, 330, 20, 25, 'Green')
    cgreen_b = ColorButton(output, painting, Colors.coolgreen, 110, 350, 20, 25, 'Green')
    skin_b = ColorButton(output, painting, (255, 160, 122), 50, 370, 20, 25, 'Skin')
    pink_b = ColorButton(output, painting, (255, 105, 180), 70, 370, 20, 25, 'Yellow')
    brown_b = ColorButton(output, painting, (139, 69, 19), 90, 370, 20, 25, 'Blue')
    grey_b = ColorButton(output, painting, Colors.red, 110, 370, 20, 25, 'Red')

    color_buttons = [black_b, white_b, red_b, cred_b,
                     yellow_b, cyellow_b, blue_b, cblue_b,
                     green_b, cgreen_b, skin_b, pink_b,
                     brown_b, grey_b]

    return color_buttons
