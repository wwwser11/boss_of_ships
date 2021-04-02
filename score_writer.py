import pygame

# func to draw score
font_name = pygame.font.match_font('arial')



def draw_text(surf, text, size, x, y, colors):
    font = pygame.font.Font(font_name, size)
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