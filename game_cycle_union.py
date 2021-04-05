# MUSIC Give credits to - Fato Shadow
# Art from Kenney.nl
# FuturaRound *Arsenal Company © 1997* FAX: (095)924-3775; e-Mail: arsenal@itco.msk.su;

from Player_class import *
from Mob_class import *
from Laser_class import *
from os import path
from score_writer import *
from Explosion_class import *
from player_improve import *
import time


# size
WIDTH = 480
HEIGHT = 600
FPS = 60
POWER_UP_TIME = 5000

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
    # give ways to pics, music
    img_dir = path.join(path.dirname(__file__), 'img')
    snd_dir = path.join(path.dirname(__file__), 'snd')
    meteors_img = path.join(path.dirname(__file__), 'img/meteors')
    explosion_img = path.join(path.dirname(__file__), 'img/explosion')
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
    player_img_mini = pygame.transform.scale(player_img, (25, 19))
    player_img_mini.set_colorkey(colors['BLACK'])
    bullet_img = pygame.image.load(path.join(img_dir, "laserGreen11.png")).convert()
    meteor_img = []
    meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png',
                   'meteorBrown_med1.png', 'meteorBrown_med3.png',
                   'meteorBrown_small1.png', 'meteorBrown_small2.png',
                   'meteorBrown_tiny1.png', 'meteorGrey_big1.png', 'meteorGrey_med1.png',
                   'meteorGrey_med1.png', 'meteorGrey_med2.png',
                   'meteorGrey_small1.png', 'meteorGrey_small2.png',
                   'meteorGrey_tiny1.png']
    for img in meteor_list:
        meteor_img.append(pygame.image.load(path.join(meteors_img, img)).convert())
    explosion_anim = {'large': [], 'small': [], 'player' : []}
    for i in range(9):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load(path.join(explosion_img, filename)).convert()
        img.set_colorkey(colors['BLACK'])
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['large'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32, 32))
        explosion_anim['small'].append(img_sm)
        filename2 = 'sonicExplosion0{}.png'.format(i)
        img2 = pygame.image.load(path.join(explosion_img, filename2)).convert()
        img.set_colorkey(colors['BLACK'])
        explosion_anim['player'].append(img2)
    powerup_images = {}
    powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
    powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png'))
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    player = Player(WIDTH, HEIGHT, player_img, all_sprites, bullets, bullet_img, colors, shoot_sound, POWER_UP_TIME)
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
        for hit in hits:
            player.shield -= hit.radius * 2
            random.choice(explosion_sound).play()
            explosion = Explosion(hit.rect.center, 'small', explosion_anim)
            all_sprites.add(explosion)
            newmob()
            if player.shield <= 0:
                death_explosion = Explosion(player.rect.center, 'player', explosion_anim)
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -= 1
                player.shield = 100
        if player.lives == 0 and not death_explosion.alive():
            running = False


        hits2 = pygame.sprite.groupcollide(mobs, bullets, True, True)
        # hit to mob
        for hit in hits2:
            score += 45 - hit.radius
            random.choice(explosion_sound).play()
            explosion = Explosion(hit.rect.center, 'large', explosion_anim)
            all_sprites.add(explosion)
            # add chance to get power up(gun or more health)
            if random.random() > 0.9:
                pow = improve(hit.rect.center, HEIGHT, powerup_images,colors)
                all_sprites.add(pow)
                powerups.add(pow)
            newmob()
        # hit powerup icon
        hits3 = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits3:
            if hit.type == 'shield':
                player.shield += random.randrange(10, 30)
                if player.shield >= 100:
                    player.shield = 100
            if hit.type == 'gun':
                player.powerup()

        screen.fill(colors['BLACK'])  # rendering
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH / 2, 10, colors)
        draw_lives(screen, WIDTH - 100, 5, player.lives,
                   player_img_mini)
        draw_health(screen, 5, 5, player.shield, colors)
        pygame.display.flip()  # flip screen


    # close screen
    pygame.quit()


game(FPS, WIDTH, HEIGHT, colors)
