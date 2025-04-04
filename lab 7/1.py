import pygame

pygame.init()


WIDTH, HEIGHT = 500, 500
RADIUS = 25
STEP = 20


x, y = WIDTH // 2, HEIGHT // 2


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

running = True
while running:
    pygame.time.delay(50)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - RADIUS - STEP >= 0:
                y -= STEP
            elif event.key == pygame.K_DOWN and y + RADIUS + STEP <= HEIGHT:
                y += STEP
            elif event.key == pygame.K_LEFT and x - RADIUS - STEP >= 0:
                x -= STEP
            elif event.key == pygame.K_RIGHT and x + RADIUS + STEP <= WIDTH:
                x += STEP
   
    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, (255, 0, 0), (x, y), RADIUS) 
    pygame.display.update()

pygame.quit()
