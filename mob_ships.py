import pygame
import random
import time


# import os


class Mob_ships(pygame.sprite.Sprite):
    def __init__(self, ship_img, width, height, colors):
        self.w = width
        self.h = height
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = ship_img
        self.image_orig.set_colorkey(colors['BLACK'])
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # circule of mobs body
        # pygame.draw.circle(self.image_orig, colors['RED'], self.rect.center, self.radius)
        self.rect.x = random.randrange(20, width - 30)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 3)
        self.speedx = random.uniform(-1.5, 1.5)
        # set start rotation position
        self.rot = 0
        # set rotation speed
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()


    def update(self):
        self.rect.y += self.speedy
        for i in range(random.randrange(1, 5)):
            time.sleep = random.randrange(1, 3)
            self.rect.x += self.speedx
        if self.rect.top > self.h + 10 or self.rect.left > self.w or self.rect.right < 0:
            self.rect.x = random.randrange(self.w - self.rect.width)
            # self.rect.y = random.randrange(-100, -40)
            self.rect.y = -100
            self.speedy = random.randrange(1, 5)
