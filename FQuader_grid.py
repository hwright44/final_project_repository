board = []

for i in range(0,10):
        board.append("_|_|" * 10)
    
def print_board(board):
    for row in board:
        print(" ".join(row))
print_board(board)
