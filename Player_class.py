import pygame
import random
import os


#make player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, w, h, pcolor):
        self.w = w
        self.h = h
        pygame.sprite.Sprite.__init__(self)
        # make img of sprite size 50x40
        self.image = pygame.Surface((50,40))
        self.image.fill(pcolor)
        self.rect = self.image.get_rect()
        self.rect.centerx = w / 2
        self.rect.bottom = h - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > self.w:
            self.rect.right = self.w
        if self.rect.left < 0:
            self.rect.left = 0
