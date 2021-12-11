import random
import time
import math

X_VALUES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
Y_VALUES = ['1', '2', '3', '4', '5', '6', '7']



class Duck:
    def __init__(self):
        pass
    
    def duck_position(self):
        duck_list = []
        while len(duck_list) < 5:
            x_coordinate = random.choice(X_VALUES)
            y_coordinate = random.choice(Y_VALUES)
            duck_position = x_coordinate + y_coordinate
            duck_list.append(duck_position)
        return duck_list

class Player:
    def __init__(self):
        pass
    
    def player_coordinates(self):
        input_list = []
        while len(input_list) < 5:
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

def hits():
    d = Duck()
    d_list = d.duck_position()
    print(d_list)
    i = Player() 
    start = time.time()
    i_list = i.player_coordinates()
    end = time.time()
    same = set(d_list).intersection(set(i_list))
    print(len(same))
    print("This is how long it took the function to run: ", end - start)
    
#def scoring():