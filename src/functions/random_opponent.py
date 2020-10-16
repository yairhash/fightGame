import random
import sys
import os
from characters.goblin import Goblin
from characters.robot import Robot
from wepons.wepons import Wepon


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
