import pygame
import sys
from lib.Defines.ScreenDefines import *
from lib.Defines.ColorDefines import *
from lib.Menus.Buttons import Button


# Initialize Pygame
pygame.init()

# Set the screen size
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
screen.fill(RED)
pygame.display.set_caption("Test Game")

# Create buttons
font = pygame.font.SysFont(None, 60)
button_height = height // 12
button_width = width // 4
play_button = Button(0, 0, button_width, button_height, GRAY, GRAY, "PLAY", font)
quit_button = Button(0, button_height, button_width, button_height, YELLOW, YELLOW, "QUIT", font)

def render_text(button):
    text = button.text
    rect = button.rect
    font = button.font
    color = button.text_color
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_button.is_clicked(pygame.mouse.get_pos()):
                running = False

    # Draw buttons
    quit_button.draw(screen)
    play_button.draw(screen)
    render_text(quit_button)
    render_text(play_button)

    pygame.display.flip()

pygame.quit()
sys.exit()
