from threading import Event, Thread
from time import sleep

def move_duck():
        """Currently a placeholder for method which will move the duck.
        
        Side effects:
                Causes 1 second delay of terminal and prints that the duck is moving.
        """
        print("the duck is moving")
        sleep(1)

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