import random
import time
import csv
import os

X_VALUES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
Y_VALUES = ['1', '2', '3', '4', '5', '6', '7']

class Duck:
    def __init__(self):
        pass
    
    def duck_position(self, num_ducks):
        """ Provides the Duck object a list of locations for the ducks. 
            The coordinates for each duck's location is randomized from the 
            'X_VALUES' and 'Y_VALUES' constants.
            
        Args:
            num_ducks(int): the number of ducks in the round.
            
        Returns:
            duck_list(list): the list of coordinates for each duck's location.
            
        Side effects:
            The "duck list" empty list are filled with random duck positons.
        """
        duck_list = []
        while len(duck_list) < num_ducks:
            x_coordinate = random.choice(X_VALUES)
            y_coordinate = random.choice(Y_VALUES)
            duck_position = x_coordinate + y_coordinate
            duck_list.append(duck_position)
        return duck_list
    
    def goose(self, duck_list):
        goose = random.choice(duck_list)
        return goose
        
class Player:
    def __init__(self):
        self.hits = 0
        self.time = 0
        #self.score = 0
    
    def player_coordinates(self, num_ducks, play_time):
        """ A user inputs the coordinates they think the duck is located at.
            The user stops after the time is is finished and/or their input is
            long enough.
        
        Args:
            num_ducks(int): The number of ducks in the round.
            playtime(int): The time it took the player to complete the round.
            
        Returns:
            input_list(list): The list of coordinates the user input for targeting
            the ducks.
            
        Side effects:
            The empty list 'input_list' has user input, the coordinates, 
            appended to 'input_list'
            The 'total_time' variable is set to the difference of
            the 'time.time()' and 'start_time'
        """
        input_list = []
        total_time = 0
        while len(input_list) < num_ducks and total_time < play_time:
            start_time = time.time()
            player_input = input("Quick! Shoot the duck! Enter the coordinates: ")
            if len(player_input) > 2:
                print("INVALID INPUT: coordinate entered too long!")
            elif len(player_input) < 2:
                print("INVALID INPUT: coordinate entered too short!")
            elif player_input[0].isdigit():
                print("INVALID INPUT: x-value of coordinate cannot be a digit!")
            elif player_input[1].isalpha():
                print("INVALID INPUT: y-value of coordinate cannot be a letter!")
            elif player_input[0] not in X_VALUES:
                print("INVALID INPUT: x-coordinate must be in the range of letters a through g!")
            elif player_input[1] not in Y_VALUES:
                print("INVALID INPUT: y-coordinate has to be a number 1 through 7!")
            else:
                player_response = player_input[0] + player_input[1]
                total_time += (time.time() - start_time)
                print(round(total_time, 2))
                round_calc = input_list.append(player_response)
        if total_time > play_time:
            print(f"Ran out of time, total time:{round(total_time, 2)}")
            input_list.pop(len(input_list) - 1)
        return input_list

def hits(i, num_ducks, play_time):
    """Represents a round of duck hunt. Creates a list of the positions of
    as many ducks need to be created. Assigns a goose. Gets a list of the player's shot
    coordinates and finds which ducks got shot. Prints the round stats.
    
    Args:
        play_time(int): The time limit for the round.
        num_ducks(int): The number of ducks in the round.
        
    Side effects:
        Prints the list of player shots, the number of ducks, the number of
        hits the user got, how long they played for, the user's final score
        and the location of the goose.
    """
    d = Duck()
    d_list = d.duck_position(num_ducks)
    goose = d.goose(d_list)
    print(d_list)
    #i = Player()
    start = time.time()
    i_list = i.player_coordinates(num_ducks, play_time)
    end = time.time()
    player_time = end - start
    same = set(d_list).intersection(set(i_list))
    num_hits = (len(same))
    if goose in i_list:
        num_hits += 3
    score = scoring(num_hits, player_time, num_ducks)
    i.hits += num_hits
    i.time += player_time
    print(i_list)
    print(f"This is the number of ducks: {num_ducks}")
    print(f"This is the number of hits you got: {num_hits}")
    print(f"This is how long it took you to complete the round: {round(player_time, 2)}")
    print(f"This is your final score: {score}")
    print(f"This is the goose: {goose}")
    return num_hits, player_time, score 

def scoring(num_hits, player_time, num_ducks):
    """Calculates the player's score after playing a round.
    
    Args:
    num_hits(int): The number of ducks the player hit.
    player_time(int): The time it took the player to complete the round.
    num_ducks(int): The number of ducks in the round.
    
    Returns:
        int: The user's score for the round.
    """
    score = num_hits * (1 / player_time)
    final_score = score * 1000
    if num_hits >= num_ducks:
        final_score *= 1.2
    return round(final_score)

def difficulty():
    """Prompts the user for a difficulty selection and assigns the playtime and
    number of ducks in the round based off of the chosen difficulty.
    
    Returns:
        play_time(int): The number of seconds the player has to shoot
        all the ducks in the round.
        num_ducks(int): The number of ducks for the user to shoot in the
        round.
        
    Side effects:
        Prints a question asking the user which difficulty they would like
        to play on. Creates an input box for the user to answer in.
    """
    num_ducks = 0
    diff_input = input("Which difficulty would you like to play on: Easy, Medium, or Hard? ")
    if diff_input == "Easy":
        play_time = 15
        num_ducks = 5
    elif diff_input == "Medium":
        play_time = 10
        num_ducks = 6
    elif diff_input == "Hard":
        play_time = 8
        num_ducks = 7
    return play_time, num_ducks, diff_input

def scoreboard(player, score, diff_input):
    """I managed to write this function due to the help I found on this website:
    https://stackoverflow.com/questions/61708596/how-to-avoid-repeating-header-when-writing-to-csv-in-loop
    """
    initials = input("Please enter your initials: ")
    column_names = ['Initials', 'Ducks_Hit', 'Time', 'Score', 'Difficulty']
    dict_rows = {'Initials': str(initials), 'Ducks_Hit': int(player.hits), 'Time': float(round(player.time,2)),
                'Score': int(score), 'Difficulty': str(diff_input)}
    file = "test2.csv"
    if os.path.isfile(file):
        with open(file, "a+", encoding = 'utf-8', newline = "") as f:
            writing_file = csv.DictWriter(f, fieldnames = column_names)
            writing_file.writerow(dict_rows)
    else:
        with open(file, "w+", encoding = "utf-8", newline = "") as f:
            writing_file = csv.DictWriter(f, fieldnames = column_names)
            writing_file.writeheader()
            writing_file.writerow(dict_rows)

def main():
    """ The user is prompted to start a game with a select number of rounds.
        Then, the user is asked to select the difficulty. The game will start
        with finding the ducks until the rounds are over.
        
    Side effects:
        The number of rounds decrement as the user finishes one round after
        another.
        The 'hits()' function outputs many statements reviewing the user's
        actions in the game. 
    """
    p = Player()
    num_rounds = int(input("How many rounds would you like to play? "))
    play_time, num_ducks, diff_input = difficulty()
    num_hits = 0
    while num_rounds > 0:
        num_rounds -= 1
        hits(p, num_ducks, play_time)
    scoreboard(p, scoring(p.hits, p.time, num_ducks), diff_input)

if __name__ == "__main__":
    main()