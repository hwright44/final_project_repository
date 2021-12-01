import random
import pprint

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

def main():
    rand_duck()
    
if __name__ == "__main__":
    main()