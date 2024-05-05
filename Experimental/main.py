import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

def projection_3d():
    return 0

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    
    screen.fill("purple")

    pygame.draw.circle(screen, "blue", player_pos, 20)

    keys = pygame.key.get_pressed()

    match keys:
        case pygame.K_a:
            player_pos.x -= 300 * dt
        case pygame.K_d:
            player_pos.x += 300 * dt
        case pygame.K_s:
            player_pos.y -= 300 * dt
        case pygame.K_w:
            player_pos += 300 * dt

    pygame.display.flip()

    dt = clock.tick(120) / 1000

pygame.quit()