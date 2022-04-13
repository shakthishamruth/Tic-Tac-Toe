import pygame
import random

pygame.init()

# Window
screen = pygame.display.set_mode((800, 675))
pygame.display.set_caption('XO')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

player = 1

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

player1Score = 0
player2score = 0

x = 0
y = 0

win = 0


def check(a, b):
    global board, player
    if board[a - 1][b - 1] == 0:
        board[a - 1][b - 1] = player
        print(board)
        if player == 1:
            player = 2
        elif player == 2:
            player = 1


def mouse_input(x1, y1, a, b):
    global x, y, player, p, board
    x2 = x1 + 180
    y2 = y1 + 180
    if x1 < x < x2 and y1 < y < y2:
        if player == 1:
            check(a, b)
        elif player == 2:
            check(a, b)


def check_win():
    global board
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            win = board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            win = board[0][i]
        if board[0][i] == board[1][i] == board[2][i]:
            win = board[0][i]


# Program loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            mouse_input(130, 50, 1, 1)
            mouse_input(310, 50, 1, 2)
            mouse_input(490, 50, 1, 3)
            mouse_input(130, 230, 2, 1)
            mouse_input(310, 230, 2, 2)
            mouse_input(490, 230, 2, 3)
            mouse_input(130, 410, 3, 1)
            mouse_input(310, 410, 3, 2)
            mouse_input(490, 410, 3, 3)
    pygame.display.update()
