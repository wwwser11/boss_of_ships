import random
import pygame


class improve(pygame.sprite.Sprite):
    def __init__(self, center, height, powerup_images, colors):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(colors['BLACK'])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2
        self.height = height

    def update(self):
        self.rect.y += self.speedy
        # if it gone down the screen it will be killed
        if self.rect.top > self.height:
            self.kill()
