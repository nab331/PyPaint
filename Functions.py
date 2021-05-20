import pygame
import math
from Colors import *


def full_quit():
    pygame.quit()
    quit()


def message_to_screen(window, msg, color=Colors.cloud, x=0, y=0, fontsize=20, bold=False, italic=False):
    message_font = pygame.font.SysFont("SimHei", fontsize, bold, italic)
    screen_text = message_font.render(msg, True, color)
    window.blit(screen_text, [x, y])
    return


def mouse_pos_distance(vec_a, vec_b):
    return math.sqrt(math.pow(vec_a[0] - vec_b[0], 2) + math.pow(vec_a[1] - vec_b[1], 2))


def forward_a_step(vec_a, vec_b, v_size):
    vec_diff = [vec_b[0] - vec_a[0], vec_b[1] - vec_a[1]]
    vec_diff_m = math.sqrt(math.pow(vec_diff[0], 2) + math.pow(vec_diff[1], 2)) + 1e-20
    vec_diff_n = [vec_diff[0] / vec_diff_m, vec_diff[1] / vec_diff_m]
    ret = [vec_a[0] + vec_diff_n[0] * v_size, vec_a[1] + vec_diff_n[1] * v_size]
    return ret
