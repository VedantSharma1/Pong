# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 03:07:17 2021

@author: LENOVO
"""


#SETUP - GAME DATA , LOGIC
#LOOP - DRAWING AND UPDATE

import pygame,sys,random
#sys provides various functions for manipulation

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x +=ball_speed_x
    ball.y +=ball_speed_y
    if ball.top <= 0 or ball.bottom >=screen_height:
        pygame.mixer.Sound.play(plob_sound)
        ball_speed_y *=-1
    if ball.left <=0 or ball.right >=screen_width:
        pygame.mixer.Sound.play(plob_sound)
        ball_speed_x *=-1
        
    #for the paddles
    if ball.colliderect(player) or ball.colliderect(opponent): #returns a true or false value
        pygame.mixer.Sound.play(plob_sound)
        ball_speed_x *=-1
        
    #player score
    if ball.left <=0:
        pygame.mixer.Sound.play(score_sound)
        ball_start()
        player_score +=1
        
    #opponent score
    if ball.right >=screen_width:
        pygame.mixer.Sound.play(score_sound)
        ball_start()
        opponent_score +=1
        
def player_animation():
    player.y +=player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >=screen_height:
        player.bottom = screen_height
        
        
def opponent_animation():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed  
        
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >=screen_height:
        opponent.bottom = screen_height
        
def ball_start():
    global ball_speed_x , ball_speed_y
    ball.center = (screen_width/2-10,screen_height/2-10)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))


pygame.init() #initate all pygame modeules
clock = pygame.time.Clock()

screen_width = 960
screen_height = 480

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong2')

#DRAWING ON THE DISPLAY SURFACE , we have two options
#rect or surface , we will use rects becuase they are easy
#to manipulate,each rect has top , bottom left right and center
#attributes

ball = pygame.Rect(screen_width/2-10,screen_height/2-10,20,20)
player = pygame.Rect(screen_width-30,screen_height/2-40,10,80)
opponent = pygame.Rect(20,screen_height/2-40,10,80)

#COLOR
bg_co = (0,0,0) #black (rgb values)
white = (250,250,250) #rgb values for white color

#ADDING MOVEMENT
ball_speed_x = 7
ball_speed_y = 7

player_speed = 0
opponent_speed = 7

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 18)

#SOUNDS
plob_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")


while True:
    for event in pygame.event.get(): #EVENTS -These are the user interactions
        if event.type == pygame.QUIT: #so if we press the close button in top
            pygame.quit()
            sys.exit() #the system quits
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:

                player_speed +=7
            if event.key == pygame.K_UP:
               
                player_speed -=7
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_speed = 0
        
       
    
    #COLLISION DETECTION
    ball_animation()
    player_animation()
    opponent_animation()
     
        
    #background
    screen.fill(bg_co)#BE careful not to draw bg later, it should come first
    #middle line,anti aliasing line
    pygame.draw.aaline(screen, white,(screen_width/2,0),(screen_width/2,screen_height))
    #DRAWING THE RECTS
    pygame.draw.rect(screen,white,player)
    pygame.draw.rect(screen,white,opponent)
    pygame.draw.ellipse(screen,white,ball)
    
    #SCORES
    player_text = basic_font.render(f'{player_score}',False,white)
    screen.blit(player_text,(screen_width/2-20,screen_height/2-13))
    
    opponent_text = basic_font.render(f'{opponent_score}',False,white)
    screen.blit(opponent_text,(screen_width/2+13,screen_height/2-13))
    
    
    pygame.display.flip() #updating the window , drawing the picture
    clock.tick(60) #limits the number of FPS in this case 60