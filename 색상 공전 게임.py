import pygame
import sys
import random
import math
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Orbit Game")

COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0)]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
