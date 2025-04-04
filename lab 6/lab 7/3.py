import pygame
import datetime

pygame.init()
H, W = 700, 700
screen = pygame.display.set_mode((H, W))
pygame.display.set_caption("AIU Clock")


clock_face = pygame.image.load("clock.png")  
min_hand = pygame.image.load("min_hand.png")  
sec_hand = pygame.image.load("sec_hand.png")  


clock_face = pygame.transform.scale(clock_face, (H, W))


scale_factor = 1.2

min_hand = pygame.transform.scale(min_hand, (int(min_hand.get_width() * scale_factor), int(min_hand.get_height() * scale_factor)))
sec_hand = pygame.transform.scale(sec_hand, (int(sec_hand.get_width() * scale_factor), int(sec_hand.get_height() * scale_factor)))


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(x, y))
    return rotated_image, new_rect


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minute = now.minute
    second = now.second


    angle_min = (-6 * minute) % 360
    angle_sec = (-6 * second) % 360


    rot_min_hand, min_rect = rot_center(min_hand, angle_min, H // 2, W // 2)
    rot_sec_hand, sec_rect = rot_center(sec_hand, angle_sec, H // 2, W // 2)


    screen.blit(clock_face, (0, 0))  
    screen.blit(rot_min_hand, min_rect.topleft)  
    screen.blit(rot_sec_hand, sec_rect.topleft)  

    pygame.display.update()
    clock.tick(60)  

pygame.quit()
