#A quick and dirty usage of pygame's screen and event system to create movement
#Animation and tile-maps to be added shortly

import os
import pygame
import time
print(pygame.__path__)
pygame.init()

#--------------------Set some variables-------------------
width = 480
height = 640
size = width, height
screen = pygame.display.set_mode(size)  #opens the physical screen

#-----------------------Load images-----------------------
img = pygame.image.load('s1.png').convert()
images = ['s1.png','s2.png','s3.png','s4.png','s5.png','s6.png','s7.png','s8.png']
img.convert_alpha()
background = pygame.image.load('8-bit-Google-Maps.png').convert()
background = pygame.transform.scale(background, (1280,720))
background.convert_alpha()

#----------------------Set the Rects----------------------
bRect = background.get_rect()
imgRect = img.get_rect()

#-------------Position the images in the world------------
imgRect.center = (int(480/2), int(640/2))
bRect.center = (int(480/2), int(640/2))

##---------------------Game Loop--------------------------
counter = 0
while 1:
    key = pygame.key.get_pressed()  #gets a list of the states of all keys (0=>not pressed; 1=>pressed)
    if key[pygame.K_DOWN]:
        bRect.y-=1
        time.sleep(.10)    #sleep slows it down, will be replaced with pygame.Clock
        img = pygame.image.load(images[counter]).convert()
        img.convert_alpha()
        imgRect = img.get_rect()
        imgRect.center = (int(480/2),int(640/2))
        counter = (counter + 1) % len(images)
    if key[pygame.K_UP]:
        bRect.y+=1
        time.sleep(.10)
        img = pygame.image.load(images[counter]).convert()
        img.convert_alpha()
        imgRect = img.get_rect()
        imgRect.center = (int(480/2),int(640/2))
        counter = (counter + 1) % len(images)
    if key[pygame.K_DOWN]:
        img = pygame.image.load(images[counter]).convert()
        img.convert_alpha()
        imgRect = img.get_rect()
        imgRect.center = (int(480/2),int(640/2))
        counter = (counter + 1) % len(images)
    if key[pygame.K_LEFT]:
        bRect.x+=1
        time.sleep(.10)
        img = pygame.image.load(images[counter]).convert()
        img.convert_alpha()
        imgRect = img.get_rect()
        imgRect.center = (int(480/2),int(640/2))
        counter = (counter + 1) % len(images)
    if key[pygame.K_RIGHT]:
        bRect.x-=1
        time.sleep(.10)
        img = pygame.image.load(images[counter]).convert()
        img.convert_alpha()
        imgRect = img.get_rect()
        imgRect.center = (int(480/2),int(640/2))
        counter = (counter + 1) % len(images)
    for event in pygame.event.get():    #event handler, just used to quit for now
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0,0,0))
    screen.blit(background,bRect)
    screen.blit(img, imgRect)
    pygame.display.flip()   #displays the images onto the screen


'''Some experimenting with wrapping the character around the screen
    if imgRect.top > height:
        bRect.bottom=0
    if imgRect.bottom < 0:
        bRect.top=height
    if imgRect.left > width:
        bRect.right=0
    if imgRect.right < 0:
        bRect.left = width
'''
