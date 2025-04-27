import pygame

print("Startup")
pygame.init()
pygame.key.set_repeat(500, 500)
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

while True:

    print("Update")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Shutdown")
            pygame.quit()
            exit()
            break

    print("Render")
    surface.fill((0, 0, 0))
    pygame.draw.rect(surface, (0, 255, 0), (10, 10, 100, 100))
    pygame.display.update()
    clock.tick(30)
