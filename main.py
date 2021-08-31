import pygame
pygame.init()
import random
from start_screen_func import *
from const import *


def game_over():
    screen = pygame.display.set_mode((size*sq, size*sq))
    pygame.display.set_caption("Сапёр")
    clock = pygame.time.Clock()

    screen.fill(WHITE)
    f = pygame.font.Font(None, 100)
    text = f.render('GAME OVER', True, BLACK)
    screen.blit(text, (100, 200))
    
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                ng = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                ng = True

        pygame.display.flip()
    if ng:
        new_game()


def win_screen():
    screen = pygame.display.set_mode((size*sq, size*sq))
    pygame.display.set_caption("Сапёр")
    clock = pygame.time.Clock()

    screen.fill(WHITE)
    f = pygame.font.Font(None, 100)
    text = f.render('YOU WIN', True, BLACK)
    screen.blit(text, (100, 200))
    
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                ng = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                ng = True

        pygame.display.flip()
    if ng:
        new_game()
    pygame.quit()


def is_win(player_board, board):
    for y in range(size):
        for x in range(size):
            if player_board[y][x] is None and board[y][x] != -1:
                return False
            elif player_board[y][x] == 10 and board[y][x] != -1:
                return False
    return True


def start_screen(screen):
    screen.fill(WHITE)
    for y in range(size):
        for x in range(size):
            pygame.draw.rect(screen, BLACK, (x*sq, y*sq, sq, sq), 1)


def draw_screen(screen, board):
    for y in range(size):
        for x in range(size):
            pygame.draw.rect(screen, BLACK, (x*sq, y*sq, sq, sq), 1)
            pygame.draw.rect(screen, WHITE, (x*sq+1, y*sq+1, sq-1, sq-1))
            t = board[y][x]
            if t is None:
                continue
            if t == 10:
                pygame.draw.rect(screen, RED, (x*sq, y*sq, sq, sq))
                continue
            if t < 4:
                color = GREEN
            elif t < 7:
                color = BLUE
            else:
                color = RED
            
            f = pygame.font.Font(None, 50)
            text = f.render(str(t), True, color)
            screen.blit(text, (x*sq + 20, y*sq + 15))


def new_game():
    screen = pygame.display.set_mode((size*sq, size*sq))
    pygame.display.set_caption("Сапёр")
    clock = pygame.time.Clock()


    board = create_nums(create_bombs(size, bombs))
    player_board = [[None] * size for i in range(size)]


    running = True
    start_screen(screen)
    go = win = False
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = event.pos[0] // sq
                    y = event.pos[1] // sq
                    if player_board[y][x] == 10:
                        continue
                    if board[y][x] != -1:
                        player_board[y][x] = board[y][x]
                    else:
                        running = False
                        go = True
                elif event.button == 3:
                    x = event.pos[0] // sq
                    y = event.pos[1] // sq
                    if player_board[y][x] is None:
                        player_board[y][x] = 10
                    elif player_board[y][x] == 10:
                        player_board[y][x] = None
                    
                        
        
        draw_screen(screen, player_board)
        pygame.display.flip()

        if is_win(player_board, board):
            running = False
            win = True

    if go:
        game_over()
    elif win:
        win_screen()
    pygame.quit()


if __name__ == '__main__':
    new_game()
    
