# final_project_repository
final project repository

The purpose of our Duck_Hunt_final.py file is to create a rendention of the popular NES game of the same name. Instead of being a p2p shooter, our program takes a user input fron the keyboard and prompts the user to shoot the coordinates of ducks in an alotted time based on a chosen difficulty. 

To run our program: simply enter into the command line: Duck_Hunt_final.py This will also create a scoreboard.csv file in the repository.

The output of the program first prints the number of ducks, the number of hits, how long it took to complete the round, the final score, and the location of a bonus goose. It prompts the user to input their initals which will then be saved in a csv file along with their aforementioned stats. From this csv file two graphs will be generated one of which being a bar graph which displays the highscores of users on easy difficulty. The second graph shows the distribution of the scores for all difficulties. 

duckposition() - duck position from duck class; Hunter Wright

Goose() - random position selected for goose; Hunter Wright

Player coordinates() - in the Player class(); Ryan Dwight

Hits() - function; Ryan Dwight

Scoring() - function; Hunter Riportella

Difficulty() - function; Farhan Quader

Scoreboard() - function; Hunter Wright

Scoreboard Graphs() - pandas function; Hunter Riportella

Welcome() - mostly print function; Everyone

Main() - function; Farhan Quader


Annotated Bibliography:
Hunter Wright: Scoreboard function
"I managed to write this function due to the help I found on this website:
    https://stackoverflow.com/questions/61708596/how-to-avoid-repeating-header-when-writing-to-csv-in-loop"
    
 I used similar code to write to a csv file multiple times without creating another header.
 If the file did not exist, we created one. If it did exist we just simply added to the existing file.
 I neede help from this website in order to make the code function properly. 


