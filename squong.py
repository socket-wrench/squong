#!/usr/bin/python3
# squong.py
# Squash version of pong.

import pygame

# Variables
DEBUG = 1

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH / 2)

PITCH_COLOR = pygame.Color("green4")

BORDER_WIDTH = int(SCREEN_WIDTH / 100)
BORDER_COLOR = pygame.Color("white")

BALL_COLOR = pygame.Color("white")
VELOCITY = 1
FRAMERATE = 960

PADDLE_WIDTH = int(SCREEN_WIDTH / 120)
PADDLE_HEIGHT = int(SCREEN_WIDTH / 10)
PADDLE_COLOR = pygame.Color("white")

WINDOW_CAPTION = "Squong - a SocketWrench production"
WINDOW_CAPTION_SHORT = "Squong"

# Classes
class Ball:
    RADIUS = int(SCREEN_WIDTH / 60)   
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def show(self,color):
        global screen
        pygame.draw.circle(screen,color,(self.x,self.y),self.RADIUS)
    def update(self):
        global PITCH_COLOR, BALL_COLOR
        newx = self.x + self.vx
        newy = self.y + self.vy
        if newx < BORDER_WIDTH+self.RADIUS:
            self.vx = - self.vx
        elif newy < BORDER_WIDTH+self.RADIUS or newy > SCREEN_HEIGHT-BORDER_WIDTH-self.RADIUS:
            self.vy = - self.vy
        elif (( newx + self.RADIUS ) > ( SCREEN_WIDTH - Paddle.WIDTH )) and (abs( newy - paddle_play.y ) < ( Paddle.HEIGHT // 2 )):
            self.vx = - self.vx
        else:
            self.show(PITCH_COLOR)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(BALL_COLOR)

class Paddle:
    WIDTH = PADDLE_WIDTH
    HEIGHT = PADDLE_HEIGHT
    COLOR = PADDLE_COLOR

    def __init__(self,y):
        self.y = y

    def show(self,color):
        global screen
        self.color = color
        pygame.draw.rect(
            screen, self.color,
            pygame.Rect(((SCREEN_WIDTH - self.WIDTH),
                        (self.y - (self.HEIGHT // 2) - (PADDLE_HEIGHT // 2))),
                        (PADDLE_WIDTH, PADDLE_HEIGHT)))
    def update(self):
        global PITCH_COLOR
        self.show(PITCH_COLOR)
        self.y = pygame.mouse.get_pos()[1]
        self.show(self.COLOR)

# objects
ball_play = Ball(SCREEN_WIDTH-Ball.RADIUS, SCREEN_HEIGHT//2,-VELOCITY,VELOCITY)
paddle_play = Paddle(SCREEN_HEIGHT//2)


# tests
if DEBUG > 0:
    print("SCREEN_WIDTH:", SCREEN_WIDTH)
    print("SCREEN_HEIGHT:", SCREEN_HEIGHT)
    print("BORDER_WIDTH:", BORDER_WIDTH)
    print("BORDER_COLOR:", BORDER_COLOR)
    print("BALL_COLOR:", BALL_COLOR)
    print("PADDLE_WIDTH:", PADDLE_WIDTH)
    print("PADDLE_COLOR:", PADDLE_COLOR)

pygame.init()
pygame.display.set_caption(WINDOW_CAPTION, WINDOW_CAPTION_SHORT)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(PITCH_COLOR)

pygame.draw.rect(screen, BORDER_COLOR,
                 pygame.Rect((0, 0), (SCREEN_WIDTH, BORDER_WIDTH)))
pygame.draw.rect(screen, BORDER_COLOR,
                 pygame.Rect((0, 0), (BORDER_WIDTH, SCREEN_HEIGHT)))
pygame.draw.rect(
    screen, BORDER_COLOR,
    pygame.Rect((0, SCREEN_HEIGHT - BORDER_WIDTH),
                (SCREEN_WIDTH, BORDER_WIDTH)))

ball_play.show(BALL_COLOR)
paddle_play.show(PADDLE_COLOR)

clock = pygame.time.Clock()


while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    clock.tick(FRAMERATE)

    pygame.display.flip()
    
    paddle_play.update()

    ball_play.update()
pygame.quit()

print("Thanks for playing!")
