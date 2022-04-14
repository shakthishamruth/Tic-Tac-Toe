# pip install pygame
import pygame
import time

pygame.init()

# Window
screen = pygame.display.set_mode((800, 675))
pygame.display.set_caption('XO')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

# font
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 128)

player = 1

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
xo = [['', '', ''], ['', '', ''], ['', '', '']]

player1score = 0
player2score = 0

x = 0
y = 0

win = 0
winner = ''

reset = False


def show_player_turn_score():
    global player, player1score, player2score
    if player == 1:
        text_player_turn = font.render('Player1 Turn', True, (27, 140, 60))
        screen.blit(text_player_turn, (301, 16))
    elif player == 2:
        text_player_turn = font.render('Player2 Turn', True, (3, 17, 138))
        screen.blit(text_player_turn, (301, 16))
    text_player1_score = font.render(str(player1score), True, (27, 140, 60))
    screen.blit(text_player1_score, (85, 311))
    text_player2_score = font.render(str(player2score), True, (3, 17, 138))
    screen.blit(text_player2_score, (751, 311))


'''def reset(t):
    global board, xo, win
    win = 0
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    for i in range(3):
        for j in range(3):
            board[i][j] = 0
            xo[i][j] = ''
'''


def mouse_input_reset(x1, y1):
    global x, y, player, board, xo, win
    x2 = x1 + 50
    y2 = y1 + 50
    if x1 < x < x2 and y1 < y < y2:
        win = 0
        t = 1
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            time.sleep(1)
            t -= 1
        for i in range(3):
            for j in range(3):
                board[i][j] = 0
                xo[i][j] = ''


def check(a, b):
    global board, player
    if board[a - 1][b - 1] == 0:
        board[a - 1][b - 1] = player
        print(board)
        if player == 1:
            player = 2
            xo[a - 1][b - 1] = 'X'
        elif player == 2:
            player = 1
            xo[a - 1][b - 1] = 'O'


def check_win():
    global board, win, player1score, player2score, winner, reset
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            win = board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            win = board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        win = board[0][0]
    if board[2][0] == board[2][2] and board[2][2] == board[0][2] and board[2][0] != 0:
        win = board[2][0]
    if win != 0:
        if win == 1:
            player1score += 1
            winner = 'Player1 wins'
        if win == 2:
            player2score += 1
            winner = 'Player2 wins'
        print('player' + str(win) + ' won')
        reset = True

    else:
        draw_cont = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    draw_cont += 1
        if draw_cont == 9:
            print('DRAW')
            winner = 'DRAW'
            reset = True


def mouse_input(x1, y1, a, b):
    global x, y, player, board, xo, winner, reset, win
    x2 = x1 + 180
    y2 = y1 + 180
    if x1 < x < x2 and y1 < y < y2:
        if reset == True:
            for i in range(3):
                for j in range(3):
                    board[i][j] = 0
                    xo[i][j] = ''
            win = 0
            reset = False
        if player == 1:
            check(a, b)
        elif player == 2:
            check(a, b)
        winner = ''
        check_win()


def showXO(cordx, cordy, a, b):
    global xo
    if xo[a - 1][b - 1] == 'X':
        textX = font2.render('X', True, (27, 140, 60))
        screen.blit(textX, (cordx + 44, cordy + 38))
    elif xo[a - 1][b - 1] == 'O':
        text_player_turn = font2.render('O', True, (3, 17, 138))
        screen.blit(text_player_turn, (cordx + 44, cordy + 38))
    elif xo[a - 1][b - 1] == '':
        text_ = font2.render('', True, (255, 255, 255))
        screen.blit(text_, (cordx + 44, cordy + 38))


def showwinner():
    global winner
    textX = font.render(winner, True, (0, 0, 0))
    screen.blit(textX, (310 + 44, 500 + 38))


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
            mouse_input_reset(20, 630)
    showXO(130, 50, 1, 1)
    showXO(310, 50, 1, 2)
    showXO(490, 50, 1, 3)
    showXO(130, 230, 2, 1)
    showXO(310, 230, 2, 2)
    showXO(490, 230, 2, 3)
    showXO(130, 410, 3, 1)
    showXO(310, 410, 3, 2)
    showXO(490, 410, 3, 3)
    showwinner()
    show_player_turn_score()
    pygame.display.update()
