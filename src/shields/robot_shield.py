import random
class Robot_shield():
      
    robot_shield_obj={
                        'wood shield':random.randint(40,80),
                        'metal shield':random.randint(40,80),
                        'stone shield':random.randint(40,80),
                        'super shield':random.randint(40,80)      
                            }

    def robot_shield(self,robot_shield_obj):
        shield_choise = random.randint(1,4)
        i=1
        for key in robot_shield_obj:
            if i == shield_choise:
                val=robot_shield_obj[key]
                return key ,val
            i=i+1
            