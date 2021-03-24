import pygame
import random
import os

def game(FPS, screen, back_color, clock, all_sprites):
    running = True
    while running: # game cycle

        clock.tick(FPS) # set cycle speed

        for event in pygame.event.get(): # now we can close screen
            if event.type == pygame.QUIT:
                running = False

        #update
        all_sprites.update()
        screen.fill(back_color) # rendering
        all_sprites.draw(screen)
        pygame.display.flip() # flip screen

    pygame.quit() # close screen