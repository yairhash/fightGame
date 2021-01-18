import random
from .win_or_lose import win_or_lose
              
def attack(player,opponent,online_user): 
        if player.wepon_power>opponent.shield_power:
                new_life=opponent.full_life-player.wepon_power
                x=(f'you hurt your opponent. opponent\'s life is {new_life}') 
                setattr(opponent,'full_life',new_life)
                win_or_lost=win_or_lose(player,opponent,online_user)
                if win_or_lose != None:
                        return win_or_lost
                else:
                        return x
                
        
        if opponent.wepon_power>player.shield_power:
                new_life=player.full_life-opponent.wepon_power
                x=(f'opponent hurt you,your life is {new_life}')
                setattr(player,'full_life',new_life)
                win_or_lose(player,opponent,online_user)
                if win_or_lose != None:
                        return win_or_lost
                else:
                        return x
                
        

          
        
        

        


