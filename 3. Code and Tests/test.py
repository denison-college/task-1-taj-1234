ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]


def print_board(board):
    print("\n  " + "   ".join(str(i) for i in range(COLS)))

    for row in board:
        print(" | " + " | ".join(row) + " |")

    print()
board = create_board()

print_board(board)