import random

X_VALUES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
Y_VALUES = ['1', '2', '3', '4', '5', '6', '7']

class Duck:
    def __init__(self, duck):
        self.duck = duck
    
    def duck_position(self, duck_position):
        self.duck_position = duck_position
        x_coordinate = random.choice(X_VALUES)
        y_coordinate = random.choice(Y_VALUES)
        duck_position = x_coordinate + y_coordinate
        return duck_position
    
class Player:
    def __init__(self):
        pass
    
    def player_coordinates(self):
        player_input = input("Quick! Shoot the duck! Enter the coordinates: ")
        if len(player_input) > 2:
            print("INVALID: coordinate entered too long!")
        elif len(player_input) < 2:
            print("INVALID: coordinate entered too short!")
        elif player_input[0].isdigit():
            print("INVALID: x-value of coordinate cannot be a digit!")
        elif player_input[1].isalpha():
            print("INVALID: y-value of coordinate cannot be a letter!")
        elif player_input[0] not in X_VALUES:
            print("x-coordinate cannot has to be letters a through g!")
        else:
            player_response = player_input[0] + player_input[1]
            return player_response