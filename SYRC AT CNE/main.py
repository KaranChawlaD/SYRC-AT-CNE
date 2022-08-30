import random
import pygame
from pygame.locals import *

#pygame init
pygame.init()

#pygame window name
pygame.display.set_caption("SYRC AT CNE")

#creating surface dimension
surface = pygame.display.set_mode(( 500, 900 ))

#import font
font = pygame.font.Font('freesansbold.ttf', 30)

#running variable
running = True

#ball coordinates
ballX = 250
ballY = 880
ballRadius = 20

#target coordinates
targetX = random.randint(0, 420)
targetY = random.randint(0, 600)

#score int
score = 0

#bounces number
bounces = random.randint(1, 4)
bounced = 0

#shoot boolean
shoot = False

#scored boolean
scored = False

#invert x integer
invertX = 1

def shootBall(mouseX, mouseY): #function to calculate slope
    return (880-mouseY) / (mouseX - 250)

#miss boolean
miss = False

while running: #while True loop

    #background colour
    surface.fill((50, 68, 118))

    #even tracking
    for event in pygame.event.get():

        if event.type == QUIT: #If Press Quit, Then Shut Down Window
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN: #taking in user's mouse coordinates
            shoot = True
            mouse = pygame.mouse.get_pos()

    if not scored and bounced == bounces: #scoring tracking
        if (targetX < ballX + 20 < targetX + 80) and (targetY < ballY - 20 < targetY + 80): #if statement to detect ball contact with target
            scored = True
            score += 1
        elif (targetX < ballX + 20 < targetX + 80) and (targetY < ballY + 20 < targetY + 80): #if statement to detect ball contact with target
            scored = True
            score += 1
        elif (targetX < ballX - 20 < targetX + 80) and (targetY < ballY - 20 < targetY + 80): #if statement to detect ball contact with target
            scored = True
            score += 1
        elif (targetX < ballX - 20 < targetX + 80) and (targetY < ballY + 20 < targetY + 80): #if statement to detect ball contact with target
            scored = True
            score += 1

    if ballX == 20 or ballX == 480:
        bounced += 1
        invertX *= -1 #inverting ball when it hits the edge

    if shoot: #shooting ball
        ballX += invertX * ((mouse[0] - 250) / abs(mouse[0] - 250)) #calculating the ball's x movement
        ballY -= abs(shootBall(mouse[0], mouse[1])) #calculating the ball's y movement
    
    if ballY <= 20 or scored: #resetting ball after it goes out of screen
        if not scored:
            score = 0
            miss = True
        else:
            miss = False

        bounced = 0
        bounces = random.randint(1, 4)
        targetX = random.randint(0, 420)
        targetY = random.randint(0, 600)    
        invertX = 1
        scored = False
        shoot = False
        ballX = 250
        ballY = 880

    if miss:
        surface.blit(font.render("Miss!", True, ( 239, 198, 116 )), (220, 0))
    elif score != 0:
        surface.blit(font.render("Score!", True, ( 239, 198, 116 )), (220, 0))
        
    #ball display
    pygame.draw.circle(surface, (( 239,198,116 )), (( ballX, ballY )), ballRadius, 0)

    #target display
    pygame.draw.rect(surface, (( 46, 52, 87 )), (( targetX, targetY, 80, 80 )), 0)

    #score display
    surface.blit(font.render("Score: " + str(score), True, ( 239, 198, 116 )), (0, 870))

    #bounces display
    surface.blit(font.render("Bounces: " + str(bounces), True, ( 239, 198, 116 )), (330, 870))

    #update
    pygame.display.update()

pygame.quit()