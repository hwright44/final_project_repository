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


def rand_duck():
        """Places a "duck" in a random position on the board
        Side effects: prints grid to the console
        """
        duck = "\u26BD"
        cells = [["0"] * 10 for i in range(10)]
        for i in range(4):
                x_coordinate = random.randrange(10)
                y_coordinate = random.randrange(10)
                cells[x_coordinate][y_coordinate] = duck
        pprint.pprint(cells)