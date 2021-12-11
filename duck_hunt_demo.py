from threading import Event, Thread
from time import sleep
import random
import pprint

class Board:
    def __init__(self, board):
        self.board = board
        board = []
        for i in range(0,10):
            board.append("_|_|" * 10)
        for row in board:
            print(" ".join(row))
        print(board)
    
    def rand_duck(self):
        """Places a "duck" in a random position on the board
        Side effects: prints grid to the console
        """
        duck = "\u26BD"
        for i in range(4):
                x_coordinate = random.randrange(10)
                y_coordinate = random.randrange(10)
                self.board[x_coordinate][y_coordinate] = duck
        pprint.pprint(self.board)
        
    def get_coordinate(self, x_coordinate, y_coordinate):
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate
        columns = len(self.board[0])
        self.y_coordinate = self.board[(columns - 1) - y_coordinate]
        rows = self.board[self.y_coordinate][x_coordinate]
        return rows
         

#def move_duck():
#        """Currently a placeholder for method which will move the duck.
#        
#        Side effects:
#                Causes 1 second delay of terminal and prints that the duck is moving.
#        """
#        print("the duck is moving")
#        sleep(1)

def play(duck_pos, difficulty = 4):
        """Play a round of duck hunt. The user must input the location of the duck before 
        the time limit.
        Args:
             duck_pos(str): The location of the duck on the board.
             difficulty(int): The time limit before the duck moves.
        Side effects:
                Prints that the player must shoot the duck within the time limit and 
                prompts the user to input the user for it's location. If the user
                exceeds the time limit it will print again and ask for another input.
                Repeats until the user gets the duck or the duck moves off the grid.
        """
        cancel_event = Event()
        wip_event = Event()

        def worker():
                """Worker method that starts the timer and prompts the user to shoot it.
                Side effects:
                        Prints that the user must shoot the duck within a specified
                        time limit. Starts the timer.
                        
                """
                timeout = difficulty
                try:
                        while not cancel_event.is_set():
                                wip_event.set()
                                move_duck()
                                print("Shoot the duck within %d secs!" % timeout)
                                wip_event.clear()
                                cancel_event.wait(timeout)
                finally:
                        wip_event.clear()

        worker_thread = Thread(target=worker)
        worker_thread.start()
        try:
                while not cancel_event.is_set():
                        try:
                                if input() == str(duck_pos) and not wip_event.is_set():
                                        cancel_event.set()
                        except KeyboardInterrupt:
                                pass
        finally:
                cancel_event.set()
                worker_thread.join()
class Shooter():
    """placeholder function for user input"""
    def __init__(self, ammo, shot):
        """intializes int ammo which is going to be used for an ammo
        counter where the user has 6 shots per round and ammo is
        reduced by one every shot. Also intializes the shot which
        is a user input of where they placed the shot.git
        """
        self.ammo = ammo
        self.shot = shot
        
    def shoot(self, hits):
        """Action of shooting.
        
        Attributes: int hits counts the number of times the user hit
        the duck.
        
        Side Effects: Prints message to user when they run out of 
        ammo
        
        Returns: amount of times (out of 6) the user hit the duck
        """
        self.ammo = 6
        hits = 0
        while self.ammo > 0:
            if self.shot == play(duck_pos):
                self.ammo -= 1
                return hits + 1
            else:
                self.ammo -= 1
        print("Good shooting!")
        print("Yer out of lead!")
        
class Scoreboard():
    """Takes the Username and tallies score"""
    def __init__(self, name, score = 0):
        """Intializes attributes.
        
        Attributes: str name which represents the users name. int
        score which represents the score based on the amount of times
        the user hit the duck.
        """
        self.name = name
        self.score = score
    
    def get_score(self, score, hits):
        """Calculates the score for the user based off of hits
        
        Attributes: int score, which represents the score based
        on the amount of times the user hit the duck.
        
        Returns: The calculated score for the user.
        """
        score = 0
        if Shooter(hits) > 0 == True:
            score = Shooter(hits) * 100
        elif Shooter(hits) < 0 == True:
            score = Shooter(hits) * 100
            score = score * -1
        else:
            score = 0
        return score