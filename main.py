import pygame

pygame.init()

# Window
screen = pygame.display.set_mode((800, 675))
pygame.display.set_caption('XO')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
