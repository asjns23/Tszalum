import pygame
import sys
from lib.Defines import *

# Initialize Pygame
pygame.init()

# Set the screen size
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
    
    # Black screen
    screen.fill((0, 0, 0))

pygame.quit()
sys.exit()
