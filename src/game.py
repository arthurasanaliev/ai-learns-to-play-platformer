import pygame
from entities.player import Player
from entities.platform import Platform
from config import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2d platformer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.platforms = [
            Platform(0, HEIGHT - 20, WIDTH, 20),
            Platform(200, 650, 150, 20),
            Platform(400, 500, 150, 20), 
            Platform(600, 350, 150, 20), 
            Platform(800, 200, 150, 20)
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update(self.platforms)

    def render(self):
        self.screen.fill(BLACK)
        for platform in self.platforms:
            platform.render(self.screen)
        self.player.render(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)