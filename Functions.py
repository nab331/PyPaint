import pygame
from Colors import *


def full_quit():
    pygame.quit()
    quit()


def message_to_screen(window, msg, colour=Colors.cloud, x=0, y=0, fontsize=25, bold=False, italic=False):
    message_font = pygame.font.SysFont("Century Gothic", fontsize, bold, italic)
    screen_text = message_font.render(msg, True, colour)
    window.blit(screen_text, [x, y])
