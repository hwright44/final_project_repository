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
            if self.shot == Play(duck_pos):
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
    
    def main(name, score):
        """Runs and displays name and score for a user
        Attributes: str name, represents user input for their name.
        int score, which represents the score based on the amount
        of times the user hit the duck.
        
        Side Effects: prints user name and user score to console.
        """
        print(f"{name} : {score}XP")