import pytest
import connect_4


@pytest.fixture
def board():
    return connect_4.create_board(6, 7)


def test_create_board(board):
    assert len(board) == 6
    assert all(len(row) == 7 for row in board)
    assert all(cell == " " for row in board for cell in row)


def test_drop_piece(board):
    connect_4.drop_piece(board, 0, "X")
    assert board[5][0] == "X"


def test_drop_piece_stack(board):
    connect_4.drop_piece(board, 0, "X")
    connect_4.drop_piece(board, 0, "O")
    assert board[5][0] == "X"
    assert board[4][0] == "O"


def test_drop_piece_full_column(board):
    for _ in range(6):
        connect_4.drop_piece(board, 0, "X")
    assert connect_4.drop_piece(board, 0, "O") is False


def test_is_valid_location(board):
    assert connect_4.is_valid_location(board, 0) is True

    for _ in range(6):
        connect_4.drop_piece(board, 0, "X")

    assert connect_4.is_valid_location(board, 0) is False


def test_horizontal_win(board):
    for c in range(4):
        connect_4.drop_piece(board, c, "X")
    assert connect_4.winning_move(board, "X")


def test_vertical_win(board):
    for _ in range(4):
        connect_4.drop_piece(board, 0, "X")
    assert connect_4.winning_move(board, "X")


def test_diagonal_positive(board):
    connect_4.drop_piece(board, 0, "X")

    connect_4.drop_piece(board, 1, "O")
    connect_4.drop_piece(board, 1, "X")

    connect_4.drop_piece(board, 2, "O")
    connect_4.drop_piece(board, 2, "O")
    connect_4.drop_piece(board, 2, "X")

    connect_4.drop_piece(board, 3, "O")
    connect_4.drop_piece(board, 3, "O")
    connect_4.drop_piece(board, 3, "O")
    connect_4.drop_piece(board, 3, "X")

    assert connect_4.winning_move(board, "X")


def test_diagonal_negative(board):
    connect_4.drop_piece(board, 3, "X")

    connect_4.drop_piece(board, 2, "O")
    connect_4.drop_piece(board, 2, "X")

    connect_4.drop_piece(board, 1, "O")
    connect_4.drop_piece(board, 1, "O")
    connect_4.drop_piece(board, 1, "X")

    connect_4.drop_piece(board, 0, "O")
    connect_4.drop_piece(board, 0, "O")
    connect_4.drop_piece(board, 0, "O")
    connect_4.drop_piece(board, 0, "X")

    assert connect_4.winning_move(board, "X")


def test_board_full(board):
    for c in range(7):
        for _ in range(6):
            connect_4.drop_piece(board, c, "X")

    assert connect_4.board_full(board)


def test_board_not_full(board):
    connect_4.drop_piece(board, 0, "X")
    assert not connect_4.board_full(board)