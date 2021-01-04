# Hooping_Journey
 Text-based basketball game

 GOAL: Post game onto a website (selfmade) 

Plan
    Design Charachter

    Design in game an option to go 5 positions on the court ( if you are at the top of the key, you hav eoption to drive towards paint, go to wing , go to corner, etc)
    May change how many positions
    Would like to add graphic of where you are at

    Design match
        Figure out what the right amount of turns there should be in a game
        Have a pool off different scenarios that are randomly chosen
    
    Scenario
    Have one for being a guard, wing, center
        Its a championship game and your a rookie finally getting to start trying to prove you are worthy of the time and attention.




7/6
Currently implemented:
    Asking player bio
    Asking position

Currently working on:
    Player charachteristics 

7/7
Currently combing abilities and desciption into one dictionary instead of a dictionary and a list. 

7/9
Finished combining ablitiles and desciption
currently trying to figure out if can use a function to add stats to attributes
works if I manually add them to the value of dictionary, but does not work if I call a function for the value

7/10
Finished attributes dictionary

7/11 
changed to input to captilzation

8/11
added try and except
attributes except doesn't work

8/14
.upper for classs doesn't work
need to get attribute values added to main player

10/10
REealize need to create mmultiple files and then can just import data from each of them as needed

Added title screen option
Added map drawing
Deleted init ( self.1 , self.2 , etc)

10/11
To add to values inside the class USE += number for whatever we want to add
Added court file ( not integrated in game yet)

10/12 
changed all the values in the dicitionary to functions for CODE REUSIBILITY.

11/19 
trying to fix error with main player ... possible missing arugments

11/26
temporarily fixed main player (Unsure if I am actually addressing the inputs to be the new values of the main_player or I am creating new variables)
Adding answer function 
created dictionary that houses the players basic attributes
CURRENT ISSUE: The player class function is not ending 
  - The chosen class is not running the function 
  
12/24 
Issue resolved.Error was that the code was not captilizing the input. Needed to set chosen_type = chosen_type.upper() instead of writing by itself. 

Fixed answer selction for current code. If the input is not one of the choices then it redos the loop
CURRENT WORKING: Trying to get the chosen type's corresponind class to actually run its function
 - Suspect that the get method is not getting from dictionary
   - Need to test if the get method not working or when we call the key of dictionary the value(function) is not working
   - think the dictionary is running the function before us calling it


12/30 
- working on feet and inch converter 

1/1
Fixed dictionary automatically running function. 
Create counter function in case the user selects NO on their class selection

In the works : 
    -
    - working on feet and inch converter

1/4
Deleted counter function and made an "else" statement that calls the dictionary. So no longer need counter ( Need to test)