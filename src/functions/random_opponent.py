import random
from characters.character import Character
from wepon.wepon import Wepon

def your_random_opponent(player):
    archer=Character('archer',250,'',0,'',0,0,0)
    robot=Character('robot',250,'',0,'',0,0,0)
    goblin=Character('goblin',250,'',0,'',0,0,0)
    wizard=Character('wizard',250,'',0,'',0,0,0)
    opponents_list=[archer,robot,goblin,wizard]
    actual_opponents=[]
    for opponent in opponents_list:
        if player!=opponent.char_type:
            actual_opponents.append(opponent)
    opponent=random.choice(actual_opponents)
    char_type=opponent.char_type
    wepon_class=Wepon()
    wepon_obj_list=wepon_class.wepon_list
    for wepon_obj in wepon_obj_list:
        if char_type==wepon_obj['name']:
            wepon_name,wepon_power=random.choice(list(wepon_obj.items())[1:5])
    shield_obj_list=wepon_class.shield_list
    for shield_obj in shield_obj_list:
        if char_type==shield_obj['name']:
            shield_name,shield_power=random.choice(list(shield_obj.items())[1:5])
            
    setattr(opponent,'wepon_name',wepon_name)
    setattr(opponent,'wepon_power',wepon_power)  
    setattr(opponent,'shield_name',shield_name)   
    setattr(opponent,'shield_power',shield_power)   
    return opponent   
 
  