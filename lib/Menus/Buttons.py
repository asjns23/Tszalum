import pygame

class Button:
    def __init__(self, left, top, width, height, bcolor, tcolor, text, font):
        self.position = (left, top)
        self.size = (width, height)
        self.background_color = bcolor
        self.text_color = tcolor
        self.text = text
        self.font = font
        self.rect = pygame.Rect(self.position, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, self.rect)

    def is_clicked(self, mouse_position):
        return self.button.collidepoint(mouse_position)
        
