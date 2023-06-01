import pygame

WIDTH = 550
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)

grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve_sudoku(board):
    if not find_empty_cell(board):
        return True

    row, col = find_empty_cell(board)

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid_move(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True



def escape():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return


def DrawGrid():
    win = pygame.display.set_mode((WIDTH, WIDTH))
    win.fill(background_color)
    my_font = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] != 0:
                value = my_font.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))

    pygame.display.update()

    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 6)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 6)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()


def main():
    pygame.font.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("CH02")
    win.fill(background_color)
    ### Call your solver algorithm here ###
    #######################################
    solve_sudoku(grid)
    DrawGrid()
    while True:
        escape()


main()
