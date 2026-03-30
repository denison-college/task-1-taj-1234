print("""
     1. select how many rows you want and how may colums you want
     2. select between the range defind to drop your marker into the colum
      default connect 4 have 6 rows and 7 columns.
      """)
# ROWS = int(input('how many rows: '))
# COLS = int(input('how many colums: '))

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(str(i) for i in range(COLS)))

    for row in board:
        print(" | " + " | ".join(row) + " |")

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

# checks if board is full
def board_full(board):
    return all(board[0][c] != " " for c in range(COLS))

# allows player to play again
def play_again():
   print("if you want to play again enter again if you want to exit enter exit.")
   i = 1
   again = input("enter hear: ")
   while i == 1:
    if again == "again":
        i = 0
        return True
    if again == "exit":
        i = 0
        return False
    else:
        print("invalid word try again")
        again = input("enter hear: ")


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
            return turn
            break

        if board_full(board):
            print("It's a tie!")
            break

        turn = 1 - turn  # Switch players
    
    # if play_again() == True:
    #     play_game()
p1_score = 0
p2_score = 0
if __name__ == "__main__":
    while True:
        ROWS = int(input('how many rows: '))
        COLS = int(input('how many colums: '))
        y = play_game()
        if y == 0:
            p1_score = p1_score +1
        elif y == 1:
            p2_score = p2_score +1
        print(f"scores", p1_score,p2_score)
        if play_again() == False:
            break
