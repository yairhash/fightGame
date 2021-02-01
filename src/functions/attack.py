import random
   
                           
def attack(player,opponent): 
        if player.wepon_power>opponent.shield_power:
                new_life=opponent.full_life-player.wepon_power
                x=f'you hurt your opponent. opponent\'s life is {new_life}'
                setattr(opponent,'full_life',new_life)
                update_wepon_power(player,opponent)
                return x
        
        if opponent.wepon_power>player.shield_power:
                new_life=player.full_life-opponent.wepon_power
                x=f'opponent hurt you,your life is {new_life}'
                setattr(player,'full_life',new_life)
                update_wepon_power(player,opponent)
                return x
                
        if player.wepon_power==opponent.shield_power or opponent.wepon_power==player.shield_power:
                update_wepon_power(player,opponent)
                return 'nothing happend'

          
def update_wepon_power(player,opponent):
        setattr(player,'wepon_power',random.randint(40,80))
        setattr(opponent,'wepon_power',random.randint(40,80))
                
        
        

        


