import cmd
import textwrap
import sys
import os
import random

screen_width = 100

# Basic Player Info
class Player:

    def __init__(self,first_name,last_name,weight,height,wingspan,homecity):
# ,name,last_name,weight,wingspan,homecity,location
        self.first_name = first_name
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
        self.open_3_point = 30
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

### CLASS OPTIONS ###      
    def three_point_specialist(self):
        main_player.open_3_point += 20
        main_player.open_midrange += 25
        main_player.contested_3_point += 15
        main_player.contested_midrange += 20
    
    def glass_cleaner(self):
        main_player.defensive_rebounding += 25
        main_player.offensive_rebounding += 25
    
    def handle_god(self):
        main_player.contested_layup += 10
        main_player.contested_midrange += 10
        main_player.open_layup += 5
        main_player.open_midrange += 15

    def lockdown_defender(self):
        main_player.perimeter_defense += 25
        main_player.interior_defense += 25
        main_player.steal += 20
        main_player.block += 20
    
    def athletic_finisher(self):
        main_player.open_layup += 15
        main_player.contested_layup += 20

### Counter Class Options ###
    def subtract_three_point_specialist(self):
        main_player.open_3_point -= 20
        main_player.open_midrange -= 25
        main_player.contested_3_point -= 15
        main_player.contested_midrange -= 20
    
    def subtract_glass_cleaner(self):
        main_player.defensive_rebounding -= 25
        main_player.offensive_rebounding -= 25
    
    def subtract_handle_god(self):
        main_player.contested_layup -= 10
        main_player.contested_midrange -= 10
        main_player.open_layup -= 5
        main_player.open_midrange -= 15

    def subtract_lockdown_defender(self):
        main_player.perimeter_defense -= 25
        main_player.interior_defense -= 25
        main_player.steal -= 20
        main_player.block -= 20
    
    def subtract_athletic_finisher(self):
        main_player.open_layup -= 15
        main_player.contested_layup -= 20


#NOTE: Can take a look into calling attributes as its own class and just refrence it as a class

main_player = Player('default ','okayer','150','68','70','Streamwood')  
# first_name,last_name,weight,height,wingspan,homecity,location

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
        option = input("> ")  # the input ('>'). putting something inside the input just lets you prompt a message before the inpout
        
        if option.strip().lower() == ("play"):
            title == False 
            start_game() #placeholder
            
        elif option.strip().lower() == ("help"):
            title == False
            help_menu()
        elif option.strip().lower() == ("quit"):
            title == False
            sys.exit()
        
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



# start_game()

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
def answer():
    while True:
        answers = {'A':'Yes', 'B':'No'}
        print('\nIs this correct?')
        for option, answer in answers.items():
            print(option + ':' + answer)
        
        response = input()
            # response.strip().upper()
        if response.strip().upper() == 'A':
            break
        if response.strip().upper() == 'B':
            return False

        if response.strip().upper() != 'A' or 'B':
            print('Please type a valid answer!')
            



# positions
positions = {1:'Point Guard', 2:'Shooting Guard',3:'Small Forward', 4:'Power Forward', 5:'Center'}
# abilities
types = {'A':'3-POINT SNIPER\n As the title describes', 'B':'GLASS CLEANER\n Cleaning the glass A.K.A Rebounder', 'C':'HANDLE GOD \n Crossover killer', 'D':'LOCKDOWN DEFENDER \n You got gold clamps', 'E':'ATHLETIC FINISHER \n Interior finisher' }

attributes = {
    'A':main_player.three_point_specialist,
    'B':main_player.glass_cleaner,
    'C':main_player.handle_god,
    'D':main_player.lockdown_defender,
    'E':main_player.athletic_finisher

}
negative_attributes = {
    'A':main_player.subtract_three_point_specialist,
    'B':main_player.subtract_glass_cleaner,
    'C':main_player.subtract_handle_god,
    'D':main_player.subtract_lockdown_defender,
    'E':main_player.subtract_athletic_finisher

}


# ask what position you want to play
def position_selection():
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
        
            loop = False
            if answer() == False :
                loop = True
                print('Please choose a new position')
                


def player_class():
    # this function selects the class for the player
    print('Awesome!')
    print('Now what kind of player are you?')

            
    x = True    
    while x == True:
        
        print('Please choose 1 option')
        # prints out all the classes and takes an input
        for letter,type in types.items(): 
            print(letter+ '.'+type)
        
        chosen_type = input()
        chosen_type = chosen_type.upper().strip()
        # if a valid input then  runs the corresponding function via the attribute dictionary 
        if str(chosen_type) in attributes:
            # attributes.get(chosen_type)()
            x = False #exits the loop

            if answer() == False :
                    # Subtract the chosen type attribute 
                # negative_attributes.get(chosen_type)() <-- I think dont need this because changed it so it doesnt call till after
                print('Please re-enter your response')
                print(main_player.open_3_point)
                x = True #Reruns the loop
            else:
                attributes.get(chosen_type)()
                print(main_player.open_3_point)

        else:
            print('Please enter a valid option') 
                    
       
        
        
        



#### Game Functionality ####
def start_game():
    # title_screen()
    
    # intro
    while True:
        print('Please answer a few questions to help us design your charachter')
        #takes the inputs for the players basic charateristics 
        main_player.first_name = input('What is your first name? ')
        main_player.last_name = input('What is your last name? ')
        print('Please round the nearest whole number')
        main_player.weight = input('What is your weight? (In lbs)')
        main_player.height = input('What is height? (In Inches)')
        main_player.wingspan = input('What is your wingspan? (In Inches)')
        main_player.homecity = input('What city are you repping?')

        
        names = { #dictionary for the name and its associated value
        'First name':main_player.first_name ,
        'Last name':main_player.last_name,
        'Weight':main_player.weight,
        'Height':main_player.height,
        'Wingspan':main_player.wingspan,
        'Homecity':main_player.homecity
        }
        
        print('Are these correct?')
        # names = [x for x in str(value_names) x.strip('main_player.') ]
      
        for charaterstic, charaterstic_value  in names.items() :
            print(charaterstic + ' : ' +charaterstic_value)
        # # three_point_specialist()
        # print('This is open 3'+str(main_player.open_3_point))
        # print('THis is contested 3'+str(main_player.contested_3_point))
        # answer()
        if answer() == False :
            print('Please re-enter your response')

        else : 
            return False
        
    # position_selection()
    # player_class()
            

        # intial_selection = [x for x in names] 
        # print(intial_selection)

        # if select

    


# test_player2= Player('Luis',186,71,73)

# test_player3= Player('Josh',109,67,69)

# print(test_player1.interior_defense())
# print(test_player2.interior_defense())
# print(test_player3.interior_defense())
# print(dir(main_player))
# title_screen()

start_game()
position_selection()
player_class()