import pygame
import random
# import os


class Mob(pygame.sprite.Sprite):
    def __init__(self, meteor_img, width, height, colors):
        self.w = width
        self.h = height
        self.meteor_img = meteor_img
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image = pygame.transform.scale(meteor_img, (50, 38))
        self.image.set_colorkey(colors['BLACK'])
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
