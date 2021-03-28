import pygame
# import random
# import os
from Laser_class import Laser


# make player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, w, h, player_img, all_sprites, bullets, bullet_img, colors):
        self.w = w
        self.h = h
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.bullet_img = bullet_img
        self.colors = colors
        pygame.sprite.Sprite.__init__(self)
        # make img of sprite size 50x40
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (70, 58))
        self.image.set_colorkey(colors['BLACK'])
        self.rect = self.image.get_rect()
        self.radius = 25
        # circle of player body
        # pygame.draw.circle(self.image, colors['RED'], self.rect.center, self.radius)
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

    def shoot(self):
        laser_bullet = Laser(self.rect.centerx, self.rect.top, self.bullet_img, self.colors)
        self.all_sprites.add(laser_bullet)
        self.bullets.add(laser_bullet)

