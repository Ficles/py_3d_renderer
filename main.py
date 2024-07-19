import pygame
from renderMath import *

SCREEN_X = 720
SCREEN_Y = 720
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()
running = True
cube = Cuboid([
    Vector3(1, 1, 2),
    Vector3(3, 1, 2),
    Vector3(1, 1, 4),
    Vector3(3, 1, 4),
    Vector3(1, -1, 2),
    Vector3(3, -1, 2),
    Vector3(1, -1, 4),
    Vector3(3, -1, 4)
])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pixelList = cube.project(1)
    for pixel in pixelList:
        pygame.draw.circle(screen, (255, 0, 0), (pixel.x*20+360, pixel.y*20+360), 5)
    lineList = cube.project_lines(1)
    for line in lineList:
        a = Vector2()
        b = Vector2()
        a.x = line[0].x * 20 + 360
        a.y = line[0].y * 20 + 360
        b.x = line[1].x * 20 + 360
        b.y = line[1].y * 20 + 360
        pygame.draw.line(screen, (255, 0, 0), a, b)

    pygame.display.flip()
    clock.tick(30)
