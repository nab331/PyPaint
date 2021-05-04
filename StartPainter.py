import os
import argparse
from Widgets import *
from Paint import *
from ButtonUI import *
from FileSystem import *


def main():
    parser = argparse.ArgumentParser(description='Map Painter')
    parser.add_argument('--startName', action='store', type=str, default='N30.300E115.005N30.310E115.015.png',
                        help='The file which is processed firstly')
    parser.add_argument('--inputDir', action='store', type=str, default='D:/Data/MapDatabase/StreetMaps',
                        help='Street map input directory')
    parser.add_argument('--outputDir', action='store', type=str, default='D:/Data/SketchMap',
                        help='Street map output directory')
    arg = parser.parse_args()

    base = BaseGame()
    file_system = FileSystem(arg.startName, arg.inputDir, arg.outputDir, blank=False)
    output = Output(base, Colors.mountain, (24, 39, 53), Colors.coolblue)  # The Background
    paint_data = PaintData()
    painting = Painting(output, paint_data)

    buttons = create_buttons(output, painting)

    color_buttons = create_color_button(output, painting)

    paint_loop(output, painting, file_system, buttons, color_buttons)

    return


if __name__ == '__main__':
    main()
