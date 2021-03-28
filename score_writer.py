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
