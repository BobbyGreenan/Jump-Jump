## Imports
import pygame
from pygame.locals import (
    K_ESCAPE,
    K_LEFT,
    K_RIGHT,
    K_UP,
    KEYDOWN,
)


## the spike class
class Spike(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("spike.png")
        self.rect = self.image.get_rect(center=(x, y))


spikes = []
for i in range(11):
    spikes.append(Spike((i * 35) + 17, 35))
    #world.add(spikes[])





## Define the Star class
class Star(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect(center=(x, y))


star = Star(70, 180)


## Define the Player class
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_velocity = 0
        self.x_velocity = 0
        self.is_jumping = False
        self.is_moving = False
        self.image = pygame.transform.scale(pygame.image.load("player.png"),
                                            (35, 70))
        self.rect = self.image.get_rect(center=(x, y))

    def update_player(self, pressed_keys):
        self.next_y = (self.rect.midbottom) + (int(self.y_velocity), 0)
        for platform in platforms:
            print(platform.rect.top)
            print(player.rect.bottom)
            if platform.rect.colliderect(player.rect):
                if player.y >= platform.rect.top + player.y_velocity:
                    if player.y <= platform.rect.bottom + player.y_velocity:
                        player.y = platform.rect.top
                if player.x >= platform.rect.left + player.x_velocity:
                    if player.x <= platform.rect.right + player.x_velocity:
                        player.x = platform.rect.right
                
                
            
            if pressed_keys[K_UP] and not self.is_jumping:
                self.y_velocity = -13
                self.is_jumping = True

        if not self.is_moving:
            if pressed_keys[K_LEFT]:
                self.x_velocity = -5
            if pressed_keys[K_RIGHT]:
                self.x_velocity = 5

        self.y_velocity += 0.53
        #if world.check_move(player, target, filter):
        self.rect.move_ip(self.x_velocity, self.y_velocity)

        if self.x_velocity <= 0:
            self.x_velocity += 0.5

        if self.x_velocity >= 0:
            self.x_velocity -= 0.5
        if self.x_velocity >= 0:
            self.x_velocity -= 0.5

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.is_jumping = False

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0



player = Player(103, 503)


## Defines the Platform class
class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("platform.png")
        self.rect = self.image.get_rect(center=(x, y))


platforms = []
for i in range(2):
    platforms.append(Platform((i + 1) * 140, 550 - (i * 100)))
for i in range(2):
    platforms.append(Platform(210 - ((i + 0)) * 140, 300 - (i * 80)))

##platform = Platform(50, 575)

backgroundColour = (150, 150, 150)

screen_width = 385
screen_height = 600
## Initialise the window
window = pygame.display.set_mode((screen_width, screen_height))
pygame.init()

## Main game loop
running = True
clock = pygame.time.Clock()

allSprites = pygame.sprite.Group()
for platform in platforms:
    allSprites.add(platform)
    
    
frameCount = 0
while running:
    frameCount += 1
    ## Set background colour
    window.fill(backgroundColour)
    ## Draws platforms
    for platform in platforms:
        window.blit(platform.image, platform.rect)
    for spike in spikes:
        window.blit(spike.image, spike.rect)
    window.blit(star.image, star.rect)
    window.blit(player.image, player.rect)

    for platform in platforms:
        if player.rect.colliderect(platform.rect):
            print("Collision")
            player.y_velocity = 0
            player.x_velocity = 0
            player.is_jumping = False
            player.is_moving = False

    for spike in spikes:
        if player.rect.colliderect(spike.rect):
            print("You hit a spike")
            running = False

    if player.rect.colliderect(star.rect):
        print("You collected a star")
        running = False

    if player.rect.bottom >= screen_height:
        print("You fell of the map")
        running = False

    UP = False
    
    player.rect.center = pygame.mouse.get_pos()
    collide = pygame.sprite.spritecollide(player, test_group, False)

    for s in collide:
        pygame.draw.rect(window, (255, 255, 255), s.rect, 5, 1)
        
    ## Check for events
    for event in pygame.event.get():
        ## Check if the user has pressed the escape key
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update_player(pressed_keys)

    ## Update the display
    pygame.display.flip()

    ## Sets FPS
    clock.tick(30)

pygame.quit()