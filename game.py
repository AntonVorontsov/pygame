import pygame
import time
from datetime import datetime

pygame.init()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя программа')
img = pygame.image.load('photo.jpeg')
pygame.display.set_icon(img)

font = pygame.font.SysFont('microsofttaile', 32)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

t = time.localtime()
date_text = str(time.strftime("%H:%M:%S", t))

greet = font.render('Смотри, как я могу!', 1, RED)
date = font.render(date_text, 1, BLUE)
width_greet, height_greet = greet.get_size()
width_date, height_date = date.get_size()

x, y = 0, 0
direct_x = 1
direct_y = 1

x1, y1 = 0, 300
direct_x1 = 1
direct_y1 = 1

clock = pygame.time.Clock()
FPS = 180

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    clock.tick(FPS)
    screen.fill(BLACK)
    screen.blit(greet, (x, y))
    x += direct_x
    y += direct_y
    if x + width_greet >= 600 or x < 0:
        direct_x = - direct_x

    if y + height_greet >= 400 or y < 0:
        direct_y = - direct_y

    screen.blit(date, (x1, y1))
    x1 += direct_x1
    y1 += direct_y1
    if x1 + width_date >= 600 or x1 < 0:
        direct_x1 = - direct_x1

    if y1 + height_date >= 400 or y1 < 0:
        direct_y1 = - direct_y1
    pygame.display.update()