import os
from Widgets import *


def create_buttons(output, painting):
    brush_water = MyButton(output, painting, os.path.join("Resources", "brush_water.png"),
                           25, 33, 50, 60,
                           ButtonData('normal_button', 15, Colors.water), '水域',
                           ['*PAINT COLORS*', ' ', 'Current Size : '], Colors.coolred)
    brush_neighborhood = MyButton(output, painting, os.path.join("Resources", "brush_neighborhood.png"),
                                  80, 33, 50, 60,
                                  ButtonData('normal_button', 15, Colors.neighborhood), '街区',
                                  ['*PAINT COLORS*', ' ', 'Current Size : '], Colors.coolred)
    brush_culture = MyButton(output, painting, os.path.join("Resources", "brush_culture.png"),
                             135, 33, 50, 60,
                             ButtonData('normal_button', 15, Colors.culture), '文化区',
                             ['*PAINT COLORS*', ' ', 'Current Size : '], Colors.coolred)
    brush_vegetation = MyButton(output, painting, os.path.join("Resources", "brush_vegetation.png"),
                                190, 33, 50, 60,
                                ButtonData('normal_button', 15, Colors.vegetation), '绿化区',
                                ['*PAINT COLORS*', ' ', 'Current Size : '], Colors.coolred)

    pencil_road0 = MyButton(output, painting, os.path.join("Resources", "pencil_road0.png"), 25, 95, 50, 60,
                            ButtonData('normal_button', 2, Colors.road_0), '小道',
                            ['*DRAW*', ' ', 'Current Size : '], Colors.carrot)
    pencil_road1 = MyButton(output, painting, os.path.join("Resources", "pencil_road1.png"), 80, 95, 50, 60,
                            ButtonData('normal_button', 8, Colors.road_1), '公路',
                            ['*DRAW*', ' ', 'Current Size : '], Colors.carrot)
    pencil_road2 = MyButton(output, painting, os.path.join("Resources", "pencil_road2.png"), 135, 95, 50, 60,
                            ButtonData('normal_button', 12, Colors.road_2), '高速公路',
                            ['*DRAW*', ' ', 'Current Size : '], Colors.carrot)
    pencil_road3 = MyButton(output, painting, os.path.join("Resources", "pencil_road3.png"), 190, 95, 50, 60,
                            ButtonData('normal_button', 12, Colors.road_3), '在建道路与其它道路',
                            ['*DRAW*', ' ', 'Current Size : '], Colors.carrot)
    # pencil_road1 = MyButton(output, painting, os.path.join("Resources", "pencil_road1.png"), 25, 150, 50, 60,
    #                  ButtonData('normal_button', 2, Colors.road_0), 'Pencil',
    #                  ['*DRAW*', ' ', 'Current Size : '], Colors.carrot)

    eraser = MyButton(output, painting, os.path.join("Resources", "eraser.png"), 30, 230, 50, 60,
                      ButtonData('function_button', None, None), 'Eraser',
                      ['*CLEARS SELECTED*', ' ', 'Current Size : '], Colors.coolblue)
    rbin = MyButton(output, painting, os.path.join("Resources", "bin.png"), 135, 230, 50, 60,
                    ButtonData('function_button', None, None), 'Clear',
                    ['*CLEARS ALL*', ' ', 'Current Size : '], Colors.cloud)
    bplus = MyButton(output, painting, os.path.join("Resources", "plus.png"), 31, 510, 35, 45,
                     ButtonData('function_button', None, None), 'Brush Size +',
                     ['**INCREASE SIZE**', 'Current Size : '], Colors.coolred)
    bminus = MyButton(output, painting, os.path.join("Resources", "minus.png"), 200, 510, 35, 50,
                      ButtonData('function_button', None, None), 'Brush Size -',
                      ['**DECREASE SIZE**', 'Current Size : '], Colors.coolblue)
    cplus = MyButton(output, painting, os.path.join("Resources", "plus.png"), 31, 450, 35, 45,
                     ButtonData('function_button', None, None), 'Darken Brush',
                     ['**INCREASE SIZE**', 'Current Size : '], Colors.coolred)
    cminus = MyButton(output, painting, os.path.join("Resources", "minus.png"), 200, 450, 35, 50,
                      ButtonData('function_button', None, None), 'Lighten Brush',
                      ['**DECREASE SIZE**', 'Current Size : '], Colors.coolblue)

    buttons = [brush_water, brush_neighborhood, brush_culture, brush_vegetation,
               pencil_road0, pencil_road1, pencil_road2, pencil_road3,
               eraser, rbin, bplus, bminus, cplus, cminus]

    return buttons


def create_color_button(output, painting):
    black_b = ColorButton(output, painting, Colors.black, 150, 330, 40, 50,
                          ButtonData('color_button', None, None), 'Black')
    white_b = ColorButton(output, painting, Colors.white, 190, 330, 40, 50,
                          ButtonData('color_button', None, None), 'White')
    red_b = ColorButton(output, painting, Colors.road_1, 50, 330, 20, 25,
                        ButtonData('color_button', None, None), 'Road_1')
    cred_b = ColorButton(output, painting, Colors.coolred, 50, 350, 20, 25,
                         ButtonData('color_button', None, None), 'Red')
    yellow_b = ColorButton(output, painting, Colors.yellow, 70, 330, 20, 25,
                           ButtonData('color_button', None, None), 'Yellow')
    cyellow_b = ColorButton(output, painting, Colors.coolyellow, 70, 350, 20, 25,
                            ButtonData('color_button', None, None), 'Yellow')
    blue_b = ColorButton(output, painting, Colors.blue, 90, 330, 20, 25,
                         ButtonData('color_button', None, None), 'Blue')
    cblue_b = ColorButton(output, painting, Colors.coolblue, 90, 350, 20, 25,
                          ButtonData('color_button', None, None), 'Blue')
    green_b = ColorButton(output, painting, Colors.green, 110, 330, 20, 25,
                          ButtonData('color_button', None, None), 'Green')
    cgreen_b = ColorButton(output, painting, Colors.coolgreen, 110, 350, 20, 25,
                           ButtonData('color_button', None, None), 'Green')
    skin_b = ColorButton(output, painting, (255, 160, 122), 50, 370, 20, 25,
                         ButtonData('color_button', None, None), 'Skin')
    pink_b = ColorButton(output, painting, (255, 105, 180), 70, 370, 20, 25,
                         ButtonData('color_button', None, None), 'Yellow')
    brown_b = ColorButton(output, painting, (139, 69, 19), 90, 370, 20, 25,
                          ButtonData('color_button', None, None), 'Blue')
    grey_b = ColorButton(output, painting, Colors.red, 110, 370, 20, 25,
                         ButtonData('color_button', None, None), 'Red')

    color_buttons = [black_b, white_b, red_b, cred_b,
                     yellow_b, cyellow_b, blue_b, cblue_b,
                     green_b, cgreen_b, skin_b, pink_b,
                     brown_b, grey_b]

    return color_buttons
