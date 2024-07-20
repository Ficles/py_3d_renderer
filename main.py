import pygame
import renderMath
SCREEN_X = 1920
SCREEN_Y = 1080
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()
running = True
cube = renderMath.Cuboid([
    renderMath.Vector3(1, 1, 0),
    renderMath.Vector3(3, 1, 0),
    renderMath.Vector3(1, 1, 2),
    renderMath.Vector3(3, 1, 2),
    renderMath.Vector3(1, -1, 0),
    renderMath.Vector3(3, -1, 0),
    renderMath.Vector3(1, -1, 2),
    renderMath.Vector3(3, -1, 2)
])

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        cube.add_x(-0.2)
    if keys[pygame.K_d]:
        cube.add_x(0.2)
    if keys[pygame.K_SPACE]:
        cube.add_y(-0.2)
    if keys[pygame.K_LSHIFT]:
        cube.add_y(0.2)
    if keys[pygame.K_w]:
        cube.add_z(0.2)
    if keys[pygame.K_s]:
        if cube.v1.z >= 0.2:
            cube.add_z(-0.2)
    if keys[pygame.K_ESCAPE]:
        running = False
    """
    pixelList = cube.project(0.4)
    for pixel in pixelList:
        pygame.draw.circle(screen, (255, 0, 0), pixel, 5)
    lineList = cube.project_lines(0.4)
    for line in lineList:
        pygame.draw.line(screen, (255, 0, 0), line[0], line[1])
    """
    polygonList = cube.project_polygons(20)
    for polygon in polygonList:
        pygame.draw.polygon(screen, (255, 0, 0), polygon)

    pygame.display.flip()
    clock.tick(30)
    print(cube.v1.z)

pygame.quit()
exit(0)
