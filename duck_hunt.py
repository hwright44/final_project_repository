import random
import time
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

X_VALUES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
Y_VALUES = ['1', '2', '3', '4', '5', '6', '7']

class Duck:
    """Class representing the ducks for the game of duck hunt."""
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
        """Chooses one duck from the list to be designated as the goose.
        
        Args:
            duck_list(list of str): List of all of the ducks' positions.
            
        Returns:
            goose(str): The position of the duck which has been labelled the goose."""
        goose = random.choice(duck_list)
        return goose
        
class Player: 
    """Class representing a player.
    
    Attributes:
        hits(int): The number of ducks successfully hit.
        time(int): The time it took for the player to shoot the ducks."""
    def __init__(self):
        self.hits = 0
        self.time = 0
        self.diff_input = ""
    
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
            print(f"Ran out of time!")
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
    print(f"Total number of ducks in round: {num_ducks}")
    print(f"This is the goose: {goose}")
    print(f"This is the number of hits you got: {num_hits}")
    print(f"This is how long you took: {round(player_time, 2)}")
    print(f"This is your final score: {score}")
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

def difficulty(self):
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
    self.diff_input = input("Which difficulty would you like to play on: Easy, Medium, or Hard? ")
    if self.diff_input.capitalize() == "Easy":
        play_time = 15
        num_ducks = 5
    elif self.diff_input.capitalize() == "Medium":
        play_time = 10
        num_ducks = 6
    elif self.diff_input.capitalize() == "Hard":
        play_time = 8
        num_ducks = 7
    return play_time, num_ducks, self.diff_input


def scoreboard(player, score, diff_input, counter_rounds):
    """Creates a scoreboard that contains the player's statistics. The statistics include
    the number of ducks they hit, the amount of time it took to complete the round, the 
    score they recieved, they difficulty they played on, and the number of rounds they played. 
    Args:
    player: a Player class object. Contains the hits (int) a player earned and the amount of time (float)
    it took the player to complete the round
    diff_input (str): represents the difficulty the player played on
    counter_rounds (int): represents the number of rounds the player played
    Side Effects:
    Creates a new CSV file called "scoreboard.csv" if the file does not already exist. Information is added
    to this file everytime the code is executed.  
    
    I (Hunter Wright) managed to write this function due to the help I found on this website:
    https://stackoverflow.com/questions/61708596/how-to-avoid-repeating-header-when-writing-to-csv-in-loop
    I used code from the website as guidance on how to write the conditional that creates the file.
    """
    initials = input("Please enter your initials: ")
    column_names = ['Initials', 'Ducks_Hit', 'Time', 'Score', 'Difficulty', 'Rounds']
    dict_rows = {'Initials': str(initials), 'Ducks_Hit': int(player.hits), 'Time': float(round(player.time,2)),
                'Score': int(score), 'Difficulty': str(diff_input), 'Rounds': int(counter_rounds)}
    file = "scoreboard.csv"
    if os.path.isfile(file):
        with open(file, "a+", encoding = 'utf-8', newline = "") as f:
            writing_file = csv.DictWriter(f, fieldnames = column_names)
            writing_file.writerow(dict_rows)
    else:
        with open(file, "w+", encoding = "utf-8", newline = "") as f:
            writing_file = csv.DictWriter(f, fieldnames = column_names)
            writing_file.writeheader()
            writing_file.writerow(dict_rows)
            
def scoreboard_graphs(self):
    """This function creates two graphs based on the scoreboard csv. 
    One of the graph is a bar graph that displays the scores of players on easy
    difficulty. The other graph displays a histogram of the score distrubution based on frequency.
    Side Effects:
    Creates two graphs that are present after the program has been executed.
    """
    scoreboard_df = pd.read_csv("scoreboard.csv")
    df = self.diff_input
    if df == "Easy" or  df == "easy" or df == "Medium" or df == "medium" or df == "Hard" or df == "hard" :
        bar_chart = scoreboard_df[(scoreboard_df["Difficulty"] == df)].plot.bar(x = "Initials", y = 'Score')
        histogram = scoreboard_df.hist(column = 'Score', bins = 5, grid = False, color = '#FFCF56')
        plt.show()
    
def welcome():
    """Welcome function meant to orient the user and give them information about the 
    game while giving them ample time to read
    
    Side Effects: Several Print statements and the implementation of the time module, 
    which delays the printing of each line by 3 seconds.
    """
    print("Welcome to Duck Hunt!")
    time.sleep(3)
    print("You will first select the number of rounds you want to play.")
    time.sleep(3)
    print("You will then select the difficulty. The greater the difficulty, the greater number of ducks and the less amount of time to shoot them!")
    time.sleep(3)
    print("After you select your difficulty, you will be presented with a list of randomly positioned ducks.")
    time.sleep(3)
    print("In order to hit the ducks, you must type in their position correctly in the allotted amount of time.")
    time.sleep(3)
    print("In the list of ducks, one of them is secretly a goose! A goose is worth 3 hits, while a duck is worth one!")
    time.sleep(3)
    print("Good Luck and Happy Shooting!")
    
    
            
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
    welcome()
    num_rounds = int(input("How many rounds would you like to play? "))
    play_time, num_ducks, diff_input = difficulty(p)
    num_hits = 0
    counter_rounds = 0
    while num_rounds > 0:
        num_rounds -= 1
        hits(p, num_ducks, play_time)
        counter_rounds += 1
    scoreboard(p, scoring(p.hits, p.time, num_ducks), diff_input, counter_rounds)
    scoreboard_graphs(p)
    


if __name__ == "__main__":
    main()