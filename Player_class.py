import pygame
# import random
# import os
from Laser_class import Laser


# make player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, w, h, player_img, all_sprites, bullets, bullet_img, colors, shoot_sound):
        self.w = w
        self.h = h
        self.speedx = 0
        self.shield = 100
        self.shoot_sound = shoot_sound
        # set time between shoots 250ms
        self.shoot_delay = 250
        # save time after last shoot
        self.last_shot = pygame.time.get_ticks()
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
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()


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
        if keystate[pygame.K_SPACE]:
            self.shoot()
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = self.w / 2
            self.rect.bottom = self.h - 10

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            laser_bullet = Laser(self.rect.centerx, self.rect.top, self.bullet_img, self.colors)
            self.all_sprites.add(laser_bullet)
            self.bullets.add(laser_bullet)
            self.shoot_sound.play()


    # just hide ship from screen
    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (self.w / 2, self.h + 200)

