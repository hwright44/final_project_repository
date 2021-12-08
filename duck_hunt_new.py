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
            print("INVALID: x-coordinate has to be letters a through g!")
        elif player_input[1] not in Y_VALUES:
            print("INVALID: y-coordinate has to be a number 1 through 7!")
        else:
            player_response = player_input[0] + player_input[1]
            return player_response
   
class Shooter():
    """placeholder function for user input"""
    def __init__(self, ammo, shot):
        """intializes int ammo which is going to be used for an ammo
        counter where the user has 6 shots per round and ammo is
        reduced by one every shot. Also intializes the shot which
        is a user input of where they placed the shot.git"""
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
        
an = Player()
player_attempts = list()
while True:
    attempt = an.player_coordinates()
    player_attempts.append(attempt)
    if len(player_attempts) >= 7:
        break
print(player_attempts)