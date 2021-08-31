from random import randint


def get_around(x, y, size):
    points = [[x-1, y-1], [x, y-1], [x+1, y-1],
           [x-1, y], [x+1, y],
           [x-1, y+1], [x, y+1], [x+1, y+1]]
    res = []
    for i in points:
        if i[0] >= 0 and i[1] >= 0 and i[0] < size and i[1] < size:
            res.append(i)
    return res
    

def create_bombs(size, n):
    board = [[0] * size for i in range(size)]
    for i in range(n):
        x, y = randint(0, size - 1), randint(0, size - 1)
        while board[y][x] != 0:
            x, y = randint(0, size - 1), randint(0, size - 1)
        board[y][x] = -1
    return board


def create_nums(board):
    size = len(board)
    for y in range(size):
        for x in range(size):
            if board[y][x] == -1:
                continue
            points = get_around(x, y, size)
            n = 0
            for i in points:
                if board[i[1]][i[0]] == -1:
                    n += 1
            board[y][x] = n
    return board


def open_cell(board, player_board, x, y):
    if board[y][x] != 0:
        return palyer_board
    
