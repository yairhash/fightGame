from .random_opponent import your_random_opponent
from characters.wizard import Wizard
from characters.archer import Archer
from wepons.archer_wepon import Archer_wepon
from wepons.wizard_wepon import Wizard_wepon
from shields.wizard_shield import Wizard_shield
from shields.archer_shield import Archer_shield



def the_great_battle(class_character, choose_character,wepon_name,wepon_power,full_life,shield_name,shield_power):

    print("attack")
    if choose_character == 'archer':
        print(f'your are attackig wepon is {class_character.wepon_name} with power of {class_character.wepon_power}. your starting life status is {class_character.full_life}')
        print(f'you are equiped with {class_character.shield_name} with the power of {class_character.shield_power}' )
        opponent=your_random_opponent()
        print(f'your opponent is: {opponent.char_type} named {opponent.name}, and his attacking wepon is {opponent.wepon_name} with the power of {opponent.wepon_power}. his starting life status is {opponent.full_life}')
        print(f'your opponent equiped with {opponent.shield_name} with the power of {opponent.shield_power}')
   
        
    else:
        print(f'your are attackig wepon is {class_character.wepon_name} with power of {class_character.wepon_power}. your starting life status is {class_character.full_life}')
        print(f'you are equiped with {class_character.shield_name} with the power of {class_character.shield_power}')
        opponent=your_random_opponent()
        print(f'your opponent is {opponent.char_type} named {opponent.name},and his attacking wepon is{opponent.wepon_name} with the power of{opponent.wepon_power}. his starting life status is {opponent.full_life}')
        print(f'your opponent equiped with {opponent.shield_name} with power of {opponent.shield_power}')
        
        
        
        
        
        
        
        
        
        
        
              
              
       