import random
import time

X_VALUES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
Y_VALUES = ['1', '2', '3', '4', '5', '6', '7']

class Duck:
    def __init__(self):
        pass
    
    def duck_position(self, num_ducks):
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
        pass
    
    def player_coordinates(self, num_ducks):
        input_list = []
        while len(input_list) < num_ducks:
            player_input = input("Quick! Shoot the duck! Enter the coordinates: ")
            if len(player_input) > 2:
                print("too long")
            elif len(player_input) < 2:
                print("too short")
            elif player_input[0].isdigit():
                print("can't be int")
            elif player_input[1].isalpha():
                print("can't be a letter")
            elif player_input[0] not in X_VALUES:
                print("x-coordinate must be in the range of letters a through g!")
            elif player_input[1] not in Y_VALUES:
                print("INVALID: y-coordinate has to be a number 1 through 7!")
            else:
                player_response = player_input[0] + player_input[1]
                round_calc = input_list.append(player_response)
        return input_list

def hits(num_ducks, play_time):
    d = Duck()
    d_list = d.duck_position(num_ducks)
    goose = d.goose(d_list)
    print(d_list)
    i = Player() 
    start = time.time()
    i_list = i.player_coordinates(num_ducks)
    end = time.time()
    player_time = end - start
    same = set(d_list).intersection(set(i_list))
    num_hits = (len(same))
    if goose in i_list:
        num_hits += 3
    score = scoring(num_hits, player_time, num_ducks)
    print(f"This is the number of ducks: {num_ducks}")
    print(num_hits)
    print("This is how long it took the function to run: ", player_time)
    print(score)
    print(f"This is the goose: {goose}")

def scoring(num_hits, player_time, num_ducks):
    score = num_hits * (1 / player_time)
    final_score = score * 1000
    if num_hits >= num_ducks:
        final_score *= 1.2
    return round(final_score)

def difficulty():
    num_ducks = 0
    diff_input = input("Which difficulty would you like to play on: Easy, Medium, or Hard?")
    if diff_input == "Easy":
        play_time = 15
        num_ducks = 5
    elif diff_input == "Medium":
        play_time = 10
        num_ducks = 6
    elif diff_input == "Hard":
        play_time = 5
        num_ducks = 7
    return play_time, num_ducks


def main():
    num_rounds = input("How many rounds would you like to play?")
    while num_rounds > 0:
        num_rounds -= 1
            
    