from Player_class import *
from Mob_class import *
from Laser_class import *
from os import path

# size
WIDTH = 480
HEIGHT = 600
FPS = 60

# colors (R, G, B)
colors = dict(
    BLACK=(0, 0, 0),
    WHITE=(255, 255, 255),
    RED=(255, 0, 0),
    GREEN=(0, 255, 0),
    BLUE=(0, 0, 255)
)


def game(fps, WIDTH, HEIGHT, colors):

    # add color of temporary player img rectangle and back
    back_color = colors['BLACK']
    pcolor = colors['GREEN']
    mcolor = colors['BLUE']
    lcolor = colors['RED']

    # turn on pygame
    pygame.init()
    # music
    pygame.mixer.init()
    # prog screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('BOSS_of_SHIPS')
    clock = pygame.time.Clock()
    # give way to pics
    img_dir = path.join(path.dirname(__file__), 'img')
    # take backpic
    background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
    background_rect = background.get_rect()
    player_img = pygame.image.load(path.join(img_dir, "Alien-Frigate.png")).convert()
    meteor_img = pygame.image.load(path.join(img_dir, "meteorGrey_med1.png")).convert()
    bullet_img = pygame.image.load(path.join(img_dir, "laserGreen11.png")).convert()

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player(WIDTH, HEIGHT, player_img, all_sprites, bullets, bullet_img, colors)
    all_sprites.add(player)

    for i in range(8):
        m = Mob(meteor_img, WIDTH, HEIGHT, colors)
        all_sprites.add(m)
        mobs.add(m)

    running = True
    while running:  # game cycle

        clock.tick(fps)  # set cycle speed

        for event in pygame.event.get():  # now we can close screen
            if event.type == pygame.QUIT:
                running = False
            # if tap space shoot happen
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # update
        all_sprites.update()
        # check collide of player and mob, dokill = False
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        if hits:
            # if hits not empty(collide done) game will stop
            running = False

        hits2 = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits2:
            m = Mob(meteor_img, WIDTH, HEIGHT, colors)
            all_sprites.add(m)
            mobs.add(m)

        screen.fill(back_color)  # rendering
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()  # flip screen
    # close screen
    pygame.quit()


game(FPS, WIDTH, HEIGHT, colors)