import pygame
import random
import os

class Enemy_laser(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_img, colors, type):
        self.x = x
        self.y = y
        self.type = type
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image = pygame.transform.scale(bullet_img, (10, 15))
        self.image.set_colorkey(colors['BLACK'])
        self.rect = self.image.get_rect()
        self.rect.bottom = self.y
        self.rect.centerx = self.x
        self.speedy = 10

    def update(self):
            self.rect.y += self.speedy

            if self.rect.bottom < 0:
                self.kill()
