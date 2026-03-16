ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(str(i) for i in range(COLS)))
    print(" +" + "---+" * COLS)
    for row in board:
        print(" | " + " | ".join(row) + " |")
        print(" +" + "---+" * COLS)
    print()

def drop_piece(board, col, piece):
    for row in reversed(range(ROWS)):
        if board[row][col] == " ":
            board[row][col] = piece
            return True
    return False

def is_valid_location(board, col):
    return board[0][col] == " "

def winning_move(board, piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    # Diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    return False

def board_full(board):
    return all(board[0][c] != " " for c in range(COLS))

def play_game():
    board = create_board()
    turn = 0  # 0 = Player 1, 1 = Player 2
    pieces = ["X", "O"]

    print("Welcome to Connect 4!")
    print_board(board)

    while True:
        piece = pieces[turn]
        print(f"Player {turn + 1}'s turn ({piece})")

        try:
            col = int(input("Choose a column (0-6): "))
            if col < 0 or col >= COLS:
                print("Invalid column.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        if not is_valid_location(board, col):
            print("Column is full.")
            continue

        drop_piece(board, col, piece)
        print_board(board)

        if winning_move(board, piece):
            print(f"Player {turn + 1} ({piece}) wins!")
            break

        if board_full(board):
            print("It's a tie!")
            break

        turn = 1 - turn  # Switch players

if __name__ == "__main__":
    play_game()
