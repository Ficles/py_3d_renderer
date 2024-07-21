import pygame
import renderMath
SCREEN_X = 1920
SCREEN_Y = 1080
pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()
running = True
cube1 = renderMath.Cuboid(2, 2, 2, 2, 2, 2, (255, 0, 0))
cube2 = renderMath.Cuboid(-2, 0, 2, 2, 2, 2, (0, 255, 0))
cube3 = renderMath.Cuboid(2, 0, 2, 2, 2, 2, (0, 0, 255))
cube4 = renderMath.Cuboid(0, 0, 2, 2, 2, 2, (127, 0, 127))
cubes = [cube1, cube2, cube3, cube4]
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        for cube in cubes:
            cube.add_x(-0.2)
    if keys[pygame.K_d]:
        for cube in cubes:
            cube.add_x(0.2)
    if keys[pygame.K_SPACE]:
        for cube in cubes:
            cube.add_y(-0.2)
    if keys[pygame.K_LSHIFT]:
        for cube in cubes:
            cube.add_y(0.2)
    if keys[pygame.K_w]:
        for cube in cubes:
            cube.add_z(0.2)
    if keys[pygame.K_s]:
        for cube in cubes:
            cube.add_z(-0.2)
    if keys[pygame.K_ESCAPE]:
        running = False

    outList = []
    for cube in cubes:
        polygons = cube.project_polygons(20)
        for i in range(0, len(polygons)):
            polygons[i].append(cube.color)
            outList.append(polygons[i])
    polygonList = []
    while len(outList) > 0:
        highestFound = outList[0]
        for i in outList:
            if i[1] >= highestFound[1]:
                highestFound = i
        outList.remove(highestFound)
        polygonList.append(highestFound)
    for polygon in polygonList:
        pygame.draw.polygon(screen, polygon[2], polygon[0])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
exit(0)
