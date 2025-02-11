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
        self.good_platforms = [
            Platform(0, HEIGHT - 20, WIDTH),
            Platform(200, 650),
            Platform(400, 500), 
            Platform(600, 350), 
            Platform(800, 200)
        ]
        self.bad_platforms = [
            Platform(200, HEIGHT - 20, color=RED),
            Platform(600, HEIGHT - 20, color=RED),
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if not self.player.update(self.good_platforms, self.bad_platforms):
            self.running = False

    def render(self):
        self.screen.fill(BLACK)
        for platform in self.good_platforms:
            platform.render(self.screen)
        for platform in self.bad_platforms:
            platform.render(self.screen)
        self.player.render(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)