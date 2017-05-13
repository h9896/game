# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:25:09 2017

@author: Edison Song
"""
import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bricks')
black = pygame.Color(0, 0, 0)

#bat init
#find a png u like as a bat 
#I use 55*11 pixels as a bat
bat = pygame.image.load('C:/Users/Edison Song/Desktop/pyg/Object Oriented Programming/bat.png')
playerY = 540
batRect = bat.get_rect()
mousex, mousey = (0, playerY)
#ball init
#find a png u like as a ball 
#I use 8*8 pixels as a ball
ball =pygame.image.load('C:/Users/Edison Song/Desktop/pyg/Object Oriented Programming/ball.png')
ballRect = ball.get_rect()
ballStartY = 200
ballSpeed = 3
ballServed = False
bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx, by)
#brick init
#find a png u like as a brick
#I use 31*16 pixels as a brick
brick = pygame.image.load('C:/Users/Edison Song/Desktop/pyg/Object Oriented Programming/brick.png')
bricks = []
for y in range(5):
    brickY = (y*24) + 100
    for x in range(10):
        brickX = (x*31) + 245
        bricks.append(Rect(brickX, brickY, brick.get_width(), brick.get_height()))
while True:
    mainSurface.fill(black)
    #brick draw
    for b in bricks:
        mainSurface.blit(brick, b)
    #bat and ball draw
    mainSurface.blit(bat, batRect)
    mainSurface.blit(ball, ballRect)
    #events
    for events in pygame.event.get():
        if events.type == QUIT:
            pygame.quit()
            sys.exit()
        elif events.type == MOUSEMOTION:
            mousex, mousey = events.pos
            if (mousex < 800 - 55):
                batRect.topleft = (mousex, playerY)
            else:
                batRect.topleft = ( 800 - 55, playerY)
        elif events.type == MOUSEBUTTONUP:
            if not ballServed:
                ballServed = True
    #main game logic
    if ballServed:
        bx +=sx
        by +=sy
        ballRect.topleft = (bx, by)
    if (by <= 0):
        by = 0
        sy *= -1
    if (by >= 600 - 8):
        ballServed = False
        bx, by = (24, ballStartY)
        ballRect.topleft = (bx, by)
    if (bx <= 0):
        bx = 0
        sx *= -1
    if (bx >= 800 -8):
        bx = 800 - 8
        sx *= -1
    if ballRect.colliderect(batRect):
        by = playerY -8
        sy *= -1
    #collision devtion
    pygame.display.update()
    fpsClock.tick(30)
    #collision detection
    brickHitIndex = ballRect.collidelist(bricks)
    if brickHitIndex >= 0:
        hb = bricks[brickHitIndex]
        mx = bx +4
        my = by +4
        if mx > hb.x + hb.width or mx <hb.x:
            sx *= -1
        else:
            sy *= -1
        del(bricks[brickHitIndex])