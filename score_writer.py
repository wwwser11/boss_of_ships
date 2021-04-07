import pygame

# func to draw score
def draw_text(surf, text, size, x, y, colors):
    font = pygame.font.Font('font/a_FuturaRound Bold.ttf', size)
    # 'True' turn on anti-aliased
    text_surface = font.render(text, True, colors['WHITE'])
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_health(surf, x, y, player_shiald, colors):
    if player_shiald < 0:
        player_shiald = 0
    bar_lenght = 100
    bar_height = 10
    # make % viewed line
    fill = (player_shiald / 100) * bar_lenght
    outline_rect = pygame.Rect(x, y, bar_lenght, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, colors['GREEN'], fill_rect)
    pygame.draw.rect(surf, colors['WHITE'], outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x +30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def show_gо_screen(screen,background, background_rect, width, height, fps, clock, colors ):
    screen.blit(background, background_rect)
    draw_text(screen, 'boss_of_ships', 64, width / 2, height / 4, colors)
    draw_text(screen, "Arrow keys move, Space to fire", 22,
              width / 2, height / 2, colors)
    draw_text(screen, "Press a key to begin", 18, width / 2, height * 3 / 4, colors)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
