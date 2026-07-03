import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Screen with Elements")
font = pygame.font.SysFont(None, 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 128, 255), (200, 150, 400, 300))
    text = font.render("Hello, Pygame!", True, (255, 255, 255))
    screen.blit(text, (250, 100))
    pygame.display.flip()
