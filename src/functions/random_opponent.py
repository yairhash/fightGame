import random
import sys
import os
from characters.goblin import Goblin
from characters.robot import Robot
from wepons.goblin_wepon import Goblin_wepon
from wepons.robot_wepon import Robot_wepon
from shields.robot_shield import Robot_shield
from shields.goblin_shield import Goblin_shield


def your_random_opponent():
    robot1=Robot('COVID-19',"",0,100,'robot',"",0)
    robot2=Robot('dark future',"",0,100,'robot',"",0) 
    goblin1=Goblin('The Green Goblin',"",0,100,'goblin',"",0) 
    goblin2=Goblin('DR G.O.B',"",0,100,'goblin',"",0) 
    opponents_list=[goblin1,goblin2,robot1,robot2]
    rand_num=random.randint(0,3)  
    actual_character=opponents_list[rand_num]
    actual_character_type = actual_character.get_type()

    if actual_character_type=='robot':
        opponent_wepon_class=Robot_wepon()
        wepon_name,wepon_power=opponent_wepon_class.robot_wepon(opponent_wepon_class.robot_wepon_obj)
        opponent_shield_class=Robot_shield()
        shield_name,shield_power=opponent_shield_class.robot_shield(opponent_shield_class.robot_shield_obj)
        setattr(robot1,'wepon_name',wepon_name)
        setattr(robot1,'wepon_power',wepon_power)
        setattr(robot2,'wepon_name',wepon_name)
        setattr(robot2,'wepon_power',wepon_power)
        setattr(robot1,'shield_name',shield_name)
        setattr(robot1,'shield_power',shield_power)
        setattr(robot2,'shield_name',shield_name)
        setattr(robot2,'shield_power',shield_power)      
    else:
        opponent_wepon_class=Goblin_wepon()
        wepon_name,wepon_power=opponent_wepon_class.goblin_wepon(opponent_wepon_class.goblin_wepon_obj)
        opponent_shield_class=Goblin_shield()
        shield_name,shield_power=opponent_shield_class.goblin_shield(opponent_shield_class.goblin_shield_obj)
        setattr(goblin1,'wepon_name',wepon_name)
        setattr(goblin1,'wepon_power',wepon_power)
        setattr(goblin2,'wepon_name',wepon_name)
        setattr(goblin2,'wepon_power',wepon_power)
        setattr(goblin1,'shield_name',shield_name)
        setattr(goblin1,'shield_power',shield_power)
        setattr(goblin2,'shield_name',shield_name)
        setattr(goblin2,'shield_power',shield_power)
        
    return actual_character   
