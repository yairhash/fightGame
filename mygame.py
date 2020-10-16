
import random

class User:
    def __init__(self, user_name, user_age, user_country, user_email):
        self.user_name = user_name
        self.user_age = user_age
        self.user_country = user_country
        self.user_email = user_email
user1 = User(input('enter your user name: '), input('enter your age:'),input('enter your country: '), input('enter your email: '))
print('welcome')


class Wepon():         
    wizard_wepon_obj={
                    'dragon':60,
                    'special wand':35,
                    'stones from the sky':50,
                    'mega powers':70,         
                    'broom':10
                        }
                        
    def wizard_wepon(self,wizard_wepon_obj):
        i=0
        while i<=5:  
            random_num=random.randint(10,80)          
            for key in wizard_wepon_obj:

                wepon_power=wizard_wepon_obj[key]
                if wepon_power>=random_num:
                    return (key,wepon_power)  
            i=i+1            
   
             
    archer_wepon_obj={
                    'regular bow':10,
                    'multy arrow attack':72,
                    'fire bow':40,
                    'tiny bombs':30,         
                    'ice arrow':25
                        }
            
    def archer_wepon(self,archer_wepon_obj):
        i=0
        while i<=5:  
            random_num=random.randint(10,80)          
            for key in archer_wepon_obj:
                wepon_power=archer_wepon_obj[key]
                if wepon_power>=random_num:
                    return (key,wepon_power)  
            i=i+1 
            
                    
    goblin_wepon_obj={
                    'dagger':30,
                    'axe':38,
                    'electro bomb':45,
                    'toxic breath':69,
                    'goblin bite' :25        
                        }
                
    def goblin_wepon(self,goblin_wepon_obj):
        i=0
        while i<=5:  
            random_num=random.randint(10,80)          
            for key in goblin_wepon_obj:
                wepon_power=goblin_wepon_obj[key]
                if wepon_power>=random_num:
                    return (key,wepon_power)  
            i=i+1 
            
    robot_wepon_obj={
                    'lazer eyes':44,
                    'rubber bullets':33,
                    'smoke screen':20,
                    'machine combo attack':71,
                    'gun shot':50         
                        }
            
    def robot_wepon(self,robot_wepon_obj):
        i=0
        while i<=5:  
            random_num=random.randint(10,80)          
            for key in robot_wepon_obj:
                wepon_power=robot_wepon_obj[key]
                if wepon_power>=random_num:
                    return (key,wepon_power)  
            i=i+1   
            
                          
class Wizard():
    def __init__(self, name,outfit,full_life,wepon_name,wepon_power):
        self.name = name
        self.outfit = outfit
        self.full_life = full_life
        self.wepon_name = wepon_name
        self.wepon_power = wepon_power


class Archer():
    def __init__(self, name,outfit,full_life,wepon_name,wepon_power):
        self.name = name
        self.outfit = outfit
        self.full_life = full_life
        self.wepon_name=wepon_name
        self.wepon_power=wepon_power
    


class Goblin():
    def __init__(self,name,wepon_name,wepon_power,full_life,char_type):
        self.name = name
        self.wepon_name = wepon_name
        self.wepon_power=wepon_power
        self.full_life=full_life
        self.char_type=char_type
    def get_type(self):
        return self.char_type    
            
class Robot():
    
    def __init__(self,name,wepon_name,wepon_power,full_life,char_type):
        self.name = name
        self.wepon_name=wepon_name
        self.wepon_power=wepon_power
        self.full_life = full_life
        self.char_type=char_type
        
    def get_type(self):
        return self.char_type 
    
        
def your_random_opponent():
    robot1=Robot('COVID-19',"",0,100,'robot')
    robot2=Robot('dark future',"",0,100,'robot') 
    goblin1=Goblin('The Green Goblin',"",0,100,'goblin') 
    goblin2=Goblin('DR G.O.B',"",0,100,'goblin') 
    opponents_list=[goblin1,goblin2,robot1,robot2]
    rand_num=random.randint(0,3)  
    actual_character=opponents_list[rand_num]
    actual_character_type = actual_character.get_type()

    if actual_character_type=='robot':
        opponent_wepon_class=Wepon()
        wepon_name,wepon_power=opponent_wepon_class.robot_wepon(opponent_wepon_class.robot_wepon_obj)
        setattr(robot1,'wepon_name',wepon_name)
        setattr(robot1,'wepon_power',wepon_power)
        setattr(robot2,'wepon_name',wepon_name)
        setattr(robot2,'wepon_power',wepon_power)
        
        print(f'local {wepon_power}')
      
    else:
        opponent_wepon_class=Wepon()
        wepon_name,wepon_power=opponent_wepon_class.goblin_wepon(opponent_wepon_class.goblin_wepon_obj)
        setattr(goblin1,'wepon_name',wepon_name)
        setattr(goblin1,'wepon_power',wepon_power)
        setattr(goblin2,'wepon_name',wepon_name)
        setattr(goblin2,'wepon_power',wepon_power)
    return actual_character   

    
print("which character you want , wizard or archer?")
choose_character = input('')
def your_choise(choose_character):
    if choose_character == 'archer':
        archer_name = input('enter archer name: ')
        archer_outfit = input('enter archer outfit: ')
        full_life = 100
        archer_wepon_class=Wepon()
        archer_wepon_name,archer_wepon_power=archer_wepon_class.archer_wepon(archer_wepon_class.archer_wepon_obj)
        class_name = Archer(archer_name,archer_outfit,full_life,archer_wepon_name,archer_wepon_power)
        the_great_battle(class_name, choose_character,archer_wepon_name,archer_wepon_power,full_life)
    else:
        wizard_name = input('enter wizard name: ')
        wizard_outfit = input('enter wizard outfit: ')
        full_life = 100
        wizard_wepon_class=Wepon()
        wizard_wepon_name,wizard_wepon_power=wizard_wepon_class.wizard_wepon(wizard_wepon_class.wizard_wepon_obj)
        class_name = Wizard( wizard_name, wizard_outfit,full_life,wizard_wepon_name,wizard_wepon_power)  # name is a class *****
        the_great_battle(class_name, choose_character,wizard_wepon_name,wizard_wepon_power,full_life)


def the_great_battle(class_character, choose_character,wepon_name,wepon_power,full_life):

    print("attack")
    if choose_character == 'archer':
        print(f'your are attackig wepon is {class_character.wepon_name} with power of {class_character.wepon_power}.your starting life status is {class_character.full_life}')
        opponent=your_random_opponent()
        print(f'your opponent is:{opponent.char_type},and his attacking wepon is {opponent.wepon_name} with the power of {opponent.wepon_power}.his starting life status is {opponent.full_life}')
        the_big_win(class_character.wepon_power,opponent.wepon_power,choose_character,class_character.full_life,opponent.full_life)
    else:
        print(f'your are attackig wepon is {class_character.wepon_name} with power of {class_character.wepon_power}.your starting life status is {class_character.full_life}')
        opponent=your_random_opponent()
        print(f'your opponent is {opponent.char_type},and his attacking wepon is{opponent.wepon_name} with the power of{opponent.wepon_power}.his starting life status is {opponent.full_life}')
        the_big_win(class_character.wepon_power,opponent.wepon_power,choose_character,class_character.full_life,opponent.full_life)


def the_big_win(character_wepon_power, opponent_wepon_power, choose_character, character_full_life, opponent_full_life):

    if character_wepon_power > opponent_wepon_power:
        print(f'your wepon\'s attack was stronger then your opponent. your new life satus is { character_full_life-opponent_wepon_power}')
        print(f'{choose_character} wins,you are on to the next fight')  
    else:
        print(f'your opponent\'s wepon attack was stronger then yours. your new life satus is {character_full_life-opponent_wepon_power}')
        print(f'{choose_character} you lost the battle')


##### main #####
your_choise(choose_character)
