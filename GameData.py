import pygame
import math
from Colors import *
from Functions import *


class BaseGame:
    def __init__(self):
        pygame.init()

        # Window
        self.window_width = 960
        self.window_height = 700
        self.window_size = (self.window_width, self.window_height)
        self.window = pygame.display.set_mode(self.window_size)  # pygame.NOFRAME

        # Game info
        pygame.display.set_caption("Map Painter")

        self.clock = pygame.time.Clock()
        self.FPS = 1000
        self.font = pygame.font.SysFont("Century Gothic", 25)

        # Border
        self.border_width = 10

        # Toolbar
        self.toolbar_x = self.border_width
        self.toolbar_y = self.border_width
        self.toolbar_w = 250
        self.toolbar_h = self.window_height - 2 * self.border_width

        # Canvas
        self.canvas_x = self.border_width + self.toolbar_w + self.border_width
        self.canvas_y = self.border_width
        self.canvas_w = self.window_width - self.canvas_x - self.border_width
        self.canvas_h = self.window_height - 2 * self.border_width

        # Info box
        self.infobox_w = self.toolbar_w - 2 * self.border_width
        self.infobox_h = 50
        self.infobox_x = 2 * self.border_width
        self.infobox_y = self.window_height - 2 * self.border_width - self.infobox_h

        return
