import pygame
import math
from Colours import *
from Functions import *



pygame.init()

window_size = window_width , window_height = 1000,800
window = pygame.display.set_mode(window_size)#, pygame.NOFRAME )

pygame.display.set_caption("Project MAN")

clock = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont( "Century Gothic" , 25 )

