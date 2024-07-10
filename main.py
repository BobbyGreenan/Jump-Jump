## PowerPoint: https://1drv.ms/p/s!AqwryYlOoBF9bJyaynIr-H2xtsY?e=pWSFY3

## Imports
import random

import pygame
from pygame.locals import (
    K_ESCAPE,
    K_LEFT,
    K_RIGHT,
    K_UP,
    KEYDOWN,
)

## Code to allow spike to fall
frameCount = 0
spike_fall_time = []
for i in range(11):
    spike_fall_time.append(random.randint(1, 600))

backgroundColour = (152, 150, 152)

screen_width = 385
screen_height = 600
## Initialise the window
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jump! Jump!")
programIcon = pygame.image.load("star.png")

pygame.display.set_icon(programIcon)
pygame.init()


## Define the Spike class
class Spike(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Sets x and y coordinates of the spike
        self.x = x
        self.y = y
        # Loads the image of the spike
        self.image = pygame.image.load("spike.png")
        # Sets the rectangle of the spike
        self.rect = self.image.get_rect(center=(x, y))

    def fall(self, time):
        # Checks if the frame count is greater than or equal to the time
        if frameCount >= time:
            # Moves the spike down
            return True
        else:
            return False


spikes = []
for i in range(11):
    # Appends a new spike to the spikes list
    spikes.append(Spike((i * 35) + 17, 35))


## Define the Star class
class Star(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Sets x and y coordinates of the star
        self.x = x
        self.y = y
        # Loads the image of the star
        self.image = pygame.image.load("star.png")
        # Sets the rectangle of the star
        self.rect = self.image.get_rect(center=(x, y))


star = Star(70, 180)


## Defines the Platform class
class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Sets x and y coordinates of the platform
        self.x = x
        self.y = y
        # Loads the image of the platform
        self.image = pygame.image.load("platform.png")
        # Sets the rectangle of the platform
        self.rect = self.image.get_rect(center=(x, y))


platforms = []
# Appends 2 platforms to the platforms list
for i in range(2):
    platforms.append(Platform((i + 1) * 140, 550 - (i * 90)))
# Appends 2 platforms to the platforms list
for i in range(2):
    platforms.append(Platform(210 - ((i + 0)) * 140, 320 - (i * 90)))


## Define the Player class
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        # Sets x and y coordinates of the player
        self.x = x
        self.y = y
        # Sets the initial y velocity of the player
        self.y_velocity = 0
        # Sets the initial x velocity of the player
        self.x_velocity = 0
        # Sets the initial jump status of the player
        self.is_jumping = False
        # Sets the initial moving status of the player
        self.is_moving = False
        # Loads the image of the player and scales it
        self.image = pygame.transform.scale(pygame.image.load("player.png"),
                                            (35, 70))
        # Sets the rectangle of the player
        self.rect = self.image.get_rect(center=(x, y))

    def update_player(self, pressed_keys):
        # Calculates the next y coordinate of the player
        self.next_y = (self.rect.midbottom) + (int(self.y_velocity), 0)
        # Iterates through the platforms list
        for platform in platforms:
            # Checks if the player is colliding with a platform
            if platform.rect.top - player.y_velocity <= player.rect.bottom <= platform.rect.center[
                    1] + player.y_velocity:
                if platform.rect.left - player.x_velocity <= player.rect.right <= platform.rect.right + player.x_velocity:
                    # Sets the y velocity of the player to 0
                    self.y_velocity = 0
                    # Sets the jump status of the player to False
                    self.is_jumping = False

            # Checks if the player is colliding with a platform from the top
            elif platform.rect.center[
                    1] - player.y_velocity <= player.rect.top <= platform.rect.bottom + player.y_velocity:
                if platform.rect.left - player.x_velocity <= player.rect.right <= platform.rect.right + player.x_velocity:
                    # Sets the y velocity of the player to 5
                    self.y_velocity = 5
                    # Sets the jump status of the player to True
                    self.is_jumping = True

            # Checks if the player is colliding with a platform from the right
            if platform.rect.center[
                    0] - player.x_velocity <= player.rect.right <= platform.rect.right - player.x_velocity:
                if platform.rect.top - player.y_velocity <= player.rect.bottom <= platform.rect.center[
                        1] + player.y_velocity:
                    # Sets the x velocity of the player to 0
                    self.x_velocity = 0
            else:
                # Checks if the player is not moving
                if not self.is_moving:
                    # Checks if the left key is pressed
                    if pressed_keys[K_LEFT]:
                        # Sets the x velocity of the player to -5
                        self.x_velocity = -5

            # Checks if the player is colliding with a platform from the left
            if platform.rect.left - player.x_velocity <= player.rect.left <= platform.rect.center[
                    0] - player.x_velocity:
                if platform.rect.top - player.y_velocity <= player.rect.bottom <= platform.rect.center[
                        1] + player.y_velocity:
                    # Sets the x velocity of the player to 0
                    self.x_velocity = 0
            else:
                # Checks if the player is not moving
                if not self.is_moving:
                    # Checks if the right key is pressed
                    if pressed_keys[K_RIGHT]:
                        # Sets the x velocity of the player to 5
                        self.x_velocity = 5

        # Checks if the up key is pressed and the player is not jumping
        if pressed_keys[K_UP] and not self.is_jumping:
            # Sets the y velocity of the player to -14
            self.y_velocity = -14
            # Sets the jump status of the player to True
            self.is_jumping = True

        # Increases the y velocity of the player
        self.y_velocity += 0.53
        #if world.check_move(player, target, filter):
        # Moves the player
        self.rect.move_ip(self.x_velocity, self.y_velocity)

        # Decreases the x velocity of the player if it is less than or equal to 0
        if self.x_velocity <= 0:
            self.x_velocity += 0.5

        # Increases the x velocity of the player if it is greater than or equal to 0
        if self.x_velocity >= 0:
            self.x_velocity -= 0.5
        if self.x_velocity >= 0:
            self.x_velocity -= 0.5

        # Checks if the player has fallen off the screen
        if self.rect.bottom >= screen_height:
            # Sets the bottom of the player to the bottom of the screen
            self.rect.bottom = screen_height
            # Sets the jump status of the player to False
            self.is_jumping = False

        # Checks if the player has gone off the left side of the screen
        if self.rect.left < 0:
            # Sets the left side of the player to 0
            self.rect.left = 0
        # Checks if the player has gone off the right side of the screen
        if self.rect.right > screen_width:
            # Sets the right side of the player to the screen width
            self.rect.right = screen_width
        # Checks if the player has gone off the top of the screen
        if self.rect.top <= 0:
            # Sets the top of the player to 0
            self.rect.top = 0


player = Player(platforms[0].rect.midbottom[0], 503)

## Main game loop
running = True
clock = pygame.time.Clock()

frameCount = 0
while running:
    # Increments the frame count
    frameCount += 1
    ## Set background colour
    # Fills the screen with the background color
    window.fill(backgroundColour)
    # Draws the spikes to the screen
    for spike in spikes:
        window.blit(spike.image, spike.rect)
    ## Draws platforms
    # Draws the platforms to the screen
    for platform in platforms:
        window.blit(platform.image, platform.rect)
    # Draws the star to the screen
    window.blit(star.image, star.rect)
    # Draws the player to the screen
    window.blit(player.image, player.rect)
    # Iterates through the platforms list
    for platform in platforms:
        # Checks if the player is colliding with a platform
        if player.rect.colliderect(platform.rect):
            # Sets the y velocity of the player to 0
            player.y_velocity = 0
            # Sets the jump status of the player to False
            player.is_jumping = False
            # Sets the moving status of the player to False
            player.is_moving = False
    # Sets i to 0
    i = 0
    # Iterates through the spikes list
    for spike in spikes:
        # Calls the fall function of the spike
        if spikes[i].fall(spike_fall_time[i]):
            # Moves the spike down
            spikes[i].rect.move_ip(0, 10)
        i += 1
        # Checks if the player is colliding with a spike
        if player.rect.colliderect(spike.rect):
            # Prints "You hit a spike"
            print("You hit a spike")
            # Sets running to False
            running = False

    # Checks if the player is colliding with the star
    if player.rect.colliderect(star.rect):
        # Prints "You collected a star"
        print("You collected a star")
        # Sets running to False
        running = False

    # Checks if the player has fallen off the screen
    if player.rect.bottom >= screen_height:
        # Prints "You fell of the map"
        print("You fell of the map")
        # Sets running to False
        running = False

    # UP = False

    # player.rect.center = pygame.mouse.get_pos()

    # for s in collide:
    #     pygame.draw.rect(window, (255, 255, 255), s.rect, 5, 1)

    ## Check for events
    # Iterates through the event list
    for event in pygame.event.get():
        ## Check if the user has pressed the escape key
        # Checks if the event type is KEYDOWN and the key pressed is escape
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            # Sets running to False
            running = False

    # Gets the pressed keys
    pressed_keys = pygame.key.get_pressed()
    # Calls the update_player function of the player
    player.update_player(pressed_keys)

    ## Update the display
    # Updates the display
    pygame.display.flip()

    ## Sets FPS
    # Sets the FPS to 42
    clock.tick(42)

# Quits pygame
pygame.quit()
