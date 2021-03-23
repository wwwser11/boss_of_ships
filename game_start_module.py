import pygame
import random
from Player_class import *
from game_cycle import *

 # size
WIDTH = 480
HEIGHT = 600
FPS = 60

# color (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# add color of temporary player img rectangle and back
back_color = BLACK
pcolor = GREEN

pygame.init() # turn on pygame
pygame.mixer.init() # music
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # prog screen
pygame.display.set_caption('BOSS_of_SHIPS')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player(WIDTH, HEIGHT, pcolor)
all_sprites.add(player)

game(FPS, screen, back_color, clock, all_sprites)