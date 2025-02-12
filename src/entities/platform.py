import pygame
from config import *

class Platform:
    def __init__(self, x, y, width=PLATFORM_WIDTH, height=PLATFORM_HEIGHT, color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)