#!/usr/bin/python3
# squong.py
# Squash version of pong.

import pygame

#Variables
DEBUG = 1

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH / 2)

PITCH_COLOR = "green4"

BORDER_WIDTH = int(SCREEN_WIDTH / 100)
BORDER_COLOR = "white"

ball_radius = int(SCREEN_WIDTH / 60)
ball_color = "white"

paddle_width = int(SCREEN_WIDTH / 120)
paddle_height = int(SCREEN_WIDTH / 10)
paddle_color = "blue"

window_caption = "Squong - a SocketWrench production"
window_caption_short = "Squong"

# tests
if DEBUG > 0:
    print("SCREEN_WIDTH:", SCREEN_WIDTH)
    print("SCREEN_HEIGHT:", SCREEN_HEIGHT)
    print("BORDER_WIDTH:", BORDER_WIDTH)
    print("BORDER_COLOR:", BORDER_COLOR)
    print("ball_radius:", ball_radius)
    print("ball_color:", ball_color)
    print("paddle_width:", paddle_width)
    print("paddle_color:", paddle_color)

pygame.init()
pygame.display.set_caption(window_caption, window_caption_short)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(pygame.Color(PITCH_COLOR))

pygame.draw.rect(screen, pygame.Color(BORDER_COLOR),
                 pygame.Rect((0, 0), (SCREEN_WIDTH, BORDER_WIDTH)))
pygame.draw.rect(screen, pygame.Color(BORDER_COLOR),
                 pygame.Rect((0, 0), (BORDER_WIDTH, SCREEN_HEIGHT)))
pygame.draw.rect(
    screen, pygame.Color(BORDER_COLOR),
    pygame.Rect((0, SCREEN_HEIGHT - BORDER_WIDTH),
                (SCREEN_WIDTH, BORDER_WIDTH)))
pygame.draw.rect(
    screen, pygame.Color(paddle_color),
    pygame.Rect(((SCREEN_WIDTH - paddle_width),
                 ((SCREEN_HEIGHT / 2) - (paddle_height / 2))),
                (paddle_width, paddle_height)))
pygame.draw.circle(screen, pygame.Color(ball_color),
                   (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)),
                   ball_radius)

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

pygame.quit()

print("Thanks for playing!")
