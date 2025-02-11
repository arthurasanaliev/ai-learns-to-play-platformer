import pygame
from config import *

class Player:
    def __init__(self):
        self.velocity = 0
        self.on_ground = False
        self.x = PLAYER_ORIGIN_X
        self.y = PLAYER_ORIGIN_Y

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            self.jump()

        self.on_ground = False
        self.velocity += GRAVITY
        self.y += self.velocity

        for platform in platforms:
            if pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT).colliderect(platform.rect):
                if self.y <= platform.rect.top:
                    self.velocity = 0
                    self.on_ground = True
                    self.y = platform.rect.y - PLAYER_HEIGHT

    def move_left(self):
        self.x = max(0, self.x - PLAYER_MOVEMENT)

    def move_right(self):
        self.x = min(WIDTH - PLAYER_WIDTH, self.x + PLAYER_MOVEMENT)

    def jump(self):
        if self.on_ground:
            self.velocity = -PLAYER_JUMP
            self.on_ground = False

    def render(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT))