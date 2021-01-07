import random
import sys
import os
from characters.character import Character
from wepon.wepon import Wepon


def your_random_opponent(player):
    archer=Character('archer',250,'',0,'',0,0,0)
    robot=Character('robot',250,'',0,'',0,0,0)
    goblin=Character('goblin',250,'',0,'',0,0,0)
    wizard=Character('wizard',250,'',0,'',0,0,0)
    opponents_list=[archer,robot,goblin,wizard]
    actual_opponent=[]
    for opponent in opponents_list:
        if player!=opponent.char_type:
            actual_opponent.append(opponent)
    character=random.choice(actual_opponent)
    character_type = character.char_type
    opponent_wepon=Wepon(character_type)
    wepon_name,wepon_power,shield_name,shield_power=opponent_wepon.get_wepon(False,True)
    setattr(character,'wepon_name',wepon_name)
    setattr(character,'wepon_power',wepon_power)  
    setattr(character,'shield_name',shield_name)   
    setattr(character,'shield_power',shield_power)   
    return character   
 
