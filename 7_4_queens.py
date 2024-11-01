def solve(board, col, n):
    if col >= n:
        print_board(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve(board, col + 1, n) or res
            board[i][col] = 0
    return res

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

N = int(input("Enter the number of queens: "))
board = [[0] * N for _ in range(N)]
if not solve(board, 0, N):
    print("Solution does not exist")




def solve(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

N = int(input("Enter the number of queens: "))
board = [[0] * N for _ in range(N)]
if solve(board, 0, N):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
else:
    print("Solution does not exist")
