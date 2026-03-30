import connect_4

def test_create_board():
    result = connect_4.create_board
    under_board = [[" " for _ in range(connect_4.COLS)] for _ in range(connect_4.ROWS)]
    assert result == under_board

