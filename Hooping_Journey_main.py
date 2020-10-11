import cmd
import textwrap
import sys
import os
import random

screen_width = 100

# Basic Player Info
class Player:

    def __init__(self):

        self.name = first_name
        self.last_name = last_name
        self.weight= weight
        # lbs
        self.height = height
        # inches
        self.wingspan = wingspan
        # inches
        self.homecity = homecity
        self.location = 'start'
        # percentage are shots
        self.open_3_point= 30
        self.contested_3_point = 20

        self.open_midrange = 40
        self.contested_midrange = 25

        self.open_layup = 85
        self.contested_layup= 50

        # defense basic stats

        self.perimeter_defense = 50
        self.interior_defense = 50
        # percentage
        self.steal = 15
        self.block = 15

        self.offensive_rebounding = 20
        self.defensive_rebounding = 20  
      
    # make function with iq, shot percentage, outside/ inside defense, 
        # offense basic stats




    # def perimter_defense(self):
    #   p_defense =int(((self.height*0.5)+((self.speed)*0.75))+((self.wingspan)*0.3)-20)
    #   return p_defense

    # def interior_defense(self):
    #     i_defense= int((self.height*0.75)+(self.speed*0.1)+(self.wingspan*0.6)-20)
    #     return i_defense
         
        
    # def steal(self,defensive_rate):
    #     pass
    
    # def defensive_rating(self,perimter_defense,interior_defense):
    #     rating = (perimter_defense+interior_defense)/2
    #     return rating

#Title Screen
def title_screen_selections():
    title = True
    while title == True:
        option = input("> ")
        if option.strip.lower() == ("play"):
            title == False
            start_game() #placeholder
            
        elif option.strip.lower() == ("help"):
            title == False
            help_menu()
        elif option.strip.lower() == ("quit"):
            title == False
            sys.exit
        
def title_screen():
    # os.system('clear')
    # Check to see if the game runs fine without the os.system('clear)
    print('-----------------------------')
    print('Welcome to Hoops Journey 2.0!')
    print('-----------------------------')
    print('       -Play-       ')
    print('       -Help-       ')
    print('       -Quit-       ')
    title_screen_selections()

def help_menu():
    print('-----------------------------')
    print('Welcome to Hoops Journey 2.0!')
    print('-----------------------------')
    print('Inputs are NOT case sensitive')
    title_screen_selections()

#### Game Functionality ####
def start_game()



#### Map ####
# --------------
# |cL| p | cR |
# --------------
# |wL| m | wR |
# --------------
# |  | t |    |
# --------------
# KEY BELOW
# L = left
# R = right
# # c = corner
# # w = wing
# p = paint
# m = mid
# t = top of key


# answers
answers = {1:'Yes', 2:'No'}

# intro

print('Please answer a few questions to help us design your charachter')


first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Please round the nearest whole number')
weight = input('What is your weight? (In lbs)')
height = input('What is height? (In Inches)')
wingspan = input('What is your wingspan? (In Inches)')
homecity = input('What city are you repping?')

main_player = Player()      

# def three_point_specialist():
#     main_player.open_3_point + 20
#     main_player.open_midrange + 25
#     print(main_player.open_3_point)
#     print(main_player.open_midrange)


# positions
positions = {1:'Point Guard', 2:'Shooting Guard',3:'Small Forward', 4:'Power Forward', 5:'Center'}
# abilities
types = {'A':'3-POINT SNIPER\n As the title describes', 'B':'GLASS CLEANER\n Cleaning the glass A.K.A Rebounder', 'C':'HANDLE GOD \n Crossover killer', 'D':'LOCKDOWN DEFENDER \n You got gold clamps', 'E':'ATHELETIC FINISHER \n Interior finisher' }
attributes = {'A':(main_player.open_3_point+20,main_player.open_midrange+20,main_player.contested_3_point+15,main_player.contested_midrange+20),'B':(main_player.defensive_rebounding+25,main_player.offensive_rebounding+25),'C':(main_player.contested_layup+10,main_player.contested_midrange+10,main_player.open_layup+5,main_player.open_midrange+15),'D':(main_player.perimeter_defense+25,main_player.interior_defense+25,main_player.steal+20,main_player.block+20),'E':(main_player.open_layup+15,main_player.contested_layup+20)}


# ask what position you want to play
loop = True
while loop == True: 

    print('What position do you play?')
    for number,position in positions.items():
     print(str(number)+'.'+position)
    try:
        position= int(input())
    except:
        print('Please type a valid answer!')
    if position in positions :
        print('Is a '+positions[position]+' correct?')
        for number, response in answers.items():
            print(str(number)+'.'+response)
        answer = int(input())
        if answer == 1:
            loop = False
        else:
            print('Please choose a new position')
        
print('Awesome!')
print('Now what kind of player are you?')

classs = True
while classs == True:
    print('Please choose 1 option')
    for letter,type in types.items():
        print(letter+ '.'+type)
    
    try:
        chosen_type =str(input())
        chosen_type.upper()
        
      
    except:
        print(' Please choose a valid option')
    
    
    if chosen_type in attributes:
         classs = False

print('Continue')  


attributes.get(chosen_type)
print(main_player.open_3_point)
    


# test_player2= Player('Luis',186,71,73)

# test_player3= Player('Josh',109,67,69)

# print(test_player1.interior_defense())
# print(test_player2.interior_defense())
# print(test_player3.interior_defense())

