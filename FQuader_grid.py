import random
import pprint

board = []

for i in range(0,10):
        board.append("_|_|" * 10)
    
def print_board(board):
        """     Displays an output of a grid from the list variable 'board'
                
                Args: List - board
                
                Side effects: Output displays a grid"""
        for row in board:
                print(" ".join(row))
print_board(board)
