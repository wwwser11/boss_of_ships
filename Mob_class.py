import pygame
import random


# import os


class Mob(pygame.sprite.Sprite):
    def __init__(self, meteor_img, width, height, colors):
        self.w = width
        self.h = height
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_img)
        self.image_orig.set_colorkey(colors['BLACK'])
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # circule of mobs body
        # pygame.draw.circle(self.image_orig, colors['RED'], self.rect.center, self.radius)
        self.rect.x = random.randrange(self.w - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)
        # set start rotation position
        self.rot = 0
        # set rotation speed
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    # rotation func
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > self.h + 10 or self.rect.left > self.w or self.rect.right < 0:
            self.rect.x = random.randrange(self.w - self.rect.width)
            # self.rect.y = random.randrange(-100, -40)
            self.rect.y = -100
            self.speedy = random.randrange(1, 5)

        self.rotate()
