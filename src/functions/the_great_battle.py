import random
from .wepon_second_choise import wepon_second_choise
from db.mongo import Db

def the_great_battle(player,opponent):  
        print("attack")
        print(f'your wepon:{player.wepon_name},power:{player.wepon_power}. your shield:{player.shield_name} power:{player.shield_power}. your life status:{player.full_life}')
        print(f'your opponent is:{opponent.char_type},opponent wepon:{opponent.wepon_name} power:{opponent.wepon_power} opponent shield:{opponent.shield_name} power: {opponent.shield_power}. life status: {opponent.full_life}')
        attack(player,opponent)
              
def attack(player,opponent): 
        input('press ENTER to attack')
        opponent_speed_attack,opponent_defed_speed=random.randint(1,100),random.randint(1,100)
        player_speed_attack,player_defed_speed=random.randint(1,100),random.randint(1,100)
        
        if player_speed_attack>opponent_defed_speed:
                new_life=opponent.full_life-player.wepon_power
                print(f'you were faster then your opponent.opponent\'s life is {new_life}') 
                setattr(opponent,'full_life',new_life)
                
        if opponent_speed_attack>player_defed_speed:
                print('opponrnt was faster then you')
                new_life=player.full_life-opponent.wepon_power
                print(f'{new_life}') 
                setattr(player,'full_life',new_life)   
        
                
                # rand_num1=random.randint(1,100),random.randint(1,100)
                # rand_num2=random.randint(1,100),random.randint(1,100)
                # if rand_num1>rand_num2:      
                #         wepon_second_choise(player)
                #         # reattack(player,opponent)
                # else:
                #        attack(player,opponent) 
                         
        if player_speed_attack>opponent_speed_attack and player.wepon_power<opponent.shield_power:
                print('you were faster then your opponent.your apponent still blocked your attack!!') 
                

        if player_speed_attack<opponent_speed_attack and opponent.wepon_power<player.shield_power:
                print(f'your opponent was faster then you.you managed to block his attack')        
        reattack(player,opponent)                

        
def reattack(player,opponent): 

        if player.full_life <20 :
                print('you lost!')
                losts=player.losts+1
                setattr(player,'losts',losts)
                                                         
        elif opponent.full_life <20 :
                print('you won!')
                wins=player.wins+1
                setattr(player,'wins',wins)
        else:
                attack(player,opponent)
        

        

