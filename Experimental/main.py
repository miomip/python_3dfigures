import pygame

pygame.init()
display = pygame.display
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

display.set_caption("Shape")

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

def projection_3d():
    return 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("lightblue")

    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()