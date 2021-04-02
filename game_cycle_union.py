# MUSIC Give credits to - Fato Shadow
# Art from Kenney.nl

from Player_class import *
from Mob_class import *
from Laser_class import *
from os import path
from score_writer import *

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
    def newmob():
        m = Mob(meteor_img, WIDTH, HEIGHT, colors)
        all_sprites.add(m)
        mobs.add(m)
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
    # give way to music
    snd_dir = path.join(path.dirname(__file__), 'snd')
    meteors_img = path.join(path.dirname(__file__), 'img/meteors')
    shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'Laser_Shoot1_best.wav'))
    explosion_sound = []
    for snd in ['Explosion_met.wav', 'Explosion4_ship.wav', 'Explosion7.wav']:
        explosion_sound.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
    pygame.mixer.music.load(path.join(snd_dir, 'MUSIC1.mp3'))
    pygame.mixer.music.set_volume(0.7)
    # take backpic
    background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
    background_rect = background.get_rect()
    player_img = pygame.image.load(path.join(img_dir, "Alien-Frigate.png")).convert()
    bullet_img = pygame.image.load(path.join(img_dir, "laserGreen11.png")).convert()
    meteor_img = []
    meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png',
                   'meteorBrown_med1.png', 'meteorBrown_med3.png',
                   'meteorBrown_small1.png', 'meteorBrown_small2.png',
                   'meteorBrown_tiny1.png']
    for img in meteor_list:
        meteor_img.append(pygame.image.load(path.join(meteors_img, img)).convert())

    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player(WIDTH, HEIGHT, player_img, all_sprites, bullets, bullet_img, colors, shoot_sound)
    all_sprites.add(player)

    for i in range(8):
        newmob()

    score = 0
    pygame.mixer.music.play(loops=-1)
    running = True
    while running:  # game cycle

        clock.tick(fps)  # set cycle speed

        for event in pygame.event.get():  # now we can close screen
            if event.type == pygame.QUIT:
                running = False

        # update
        all_sprites.update()
        # check collide of player and mob, dokill = False(dont delete mob)
        # when dokill True collide of player and mob delete mob
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        # if hits:
        #     # if hits not empty(collide done) game will stop
        #     running = False
        for hit in hits:
            player.shield -= hit.radius * 2
            random.choice(explosion_sound).play()
            newmob()
            if player.shield <= 0:
                running = False


        hits2 = pygame.sprite.groupcollide(mobs, bullets, True, True)
        # hit to mob
        for hit in hits2:
            score += 45 - hit.radius
            random.choice(explosion_sound).play()
            newmob()

        screen.fill(colors['BLACK'])  # rendering
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH / 2, 10, colors)
        draw_health(screen, 5, 5, player.shield, colors)
        pygame.display.flip()  # flip screen

    # close screen
    pygame.quit()


game(FPS, WIDTH, HEIGHT, colors)
