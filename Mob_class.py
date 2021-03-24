import pygame
import random
import os

class Mob(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        self.w = width
        self.h = height
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.w - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > self.h + 10 or self.rect.left < -25 or self.rect.right > self.w + 20:
            self.rect.x = random.randrange(self.w - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)
