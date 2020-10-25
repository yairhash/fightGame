from .random_opponent import your_random_opponent
import random


        
def attack(class_character,choose_character,wepon_power,shield_power,full_life):
        character_speed_attack=random.randint(1,10)
        opponent_speed_attack=random.randint(1,10)
        opponent=your_random_opponent() 
        input('press ENTER to start attacking')
      
        if character_speed_attack>opponent_speed_attack and class_character.wepon_power>opponent.shield_power: 
                print(f'you were faster then your opponent and attacked first')
                print (f'your wepon was stronger then opponent\'s shield and his life is {opponent.full_life-class_character.wepon_power}')
                
        elif character_speed_attack>opponent_speed_attack and class_character.wepon_power<opponent.shield_power: 
                print('you were faster then your opponent and attacked first')
                print ('your apponent still blocked your attack')
                
        elif character_speed_attack==opponent_speed_attack:
                print("you both attacked at thr same time")
        
        elif character_speed_attack<opponent_speed_attack and opponent.wepon_power>class_character.shield_power:
                print(f'your opponent was faster then you and attacked first')
                print (f'his wepon was stronger then your shield and his life is {class_character.full_life-opponent.wepon_power}')
        
        elif character_speed_attack<opponent_speed_attack and opponent.wepon_power<class_character.shield_power:
                print(f'your opponent was faster then you and attacked first')
                print (f'you managed to block his attack')
                
                        
                
        
