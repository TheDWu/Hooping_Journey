class Player:

    def __init__(self, first_name,last_name, weight,height,wingspan,homecity):

        self.name = first_name
        self.last_name = last_name
        self.weight= weight
        # lbs
        self.height = height
        # inches
        self.wingspan = wingspan
        # inches
        self.homecity = homecity
        # 
      
    # make function with iq, shot percentage, outside/ inside defense, 
        # offense basic stats
# percentage are shots
    open_3_point= 30
    contested_3_point = 20

    open_midrange = 40
    contested_midrange = 25

    open_layup = 85
    contested_layup= 50

    # defense basic stats

    perimeter_defense = 50
    interior_defense = 50
        # percentage
    steal = 15
    block = 15
    


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




# answers
answers = {1:'Yes', 2:'No'}

# intro
print('Welcome to Hoops REVAMPED!')
print('Please answer a few questions to help us design your charachter')


first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Please round the nearest whole number')
weight = input('What is your weight? (In lbs)')
height = input('What is height? (In Inches)')
wingspan = input('What is your wingspan? (In Inches)')
homecity = input('What city are you repping?')

main_player = Player(first_name,last_name,height,weight,wingspan,homecity)      

def three_point_specialist():
    main_player.open_3_point + 20
    main_player.open_midrange + 25
    # print(main_player.open_3_point)
    # print(main_player.open_midrange)


# positions
positions = {1:'Point Guard', 2:'Shooting Guard',3:'Small Forward', 4:'Power Forward', 5:'Center'}
# abilities
types = {'A':'3-POINT SNIPER\n As the title describes', 'B':'GLASS CLEANER\n Cleaning the glass A.K.A Rebounder', 'C':'HANDLE GOD \n Crossover killer', 'D':'LOCKDOWN DEFENDER \n You got gold clamps', 'E':'ATHELETIC FINISHER \n Interior finisher','F':'ISO SPECIALIST \n Kobe' }
attributes = {'A':three_point_specialist()}


# ask what position you want to play
loop = True
while loop == True: 

    print('What position do you play?')
    for number,position in positions.items():
     print(str(number)+'.'+position)
    position= int(input())

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
    print(attributes.get('A'))
    
    chosen_type =input()
    


# test_player2= Player('Luis',186,71,73)

# test_player3= Player('Josh',109,67,69)

# print(test_player1.interior_defense())
# print(test_player2.interior_defense())
# print(test_player3.interior_defense())

