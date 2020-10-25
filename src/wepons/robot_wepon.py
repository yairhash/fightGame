import random
class Robot_wepon():
      
    robot_wepon_obj={
                    'lazer eyes':random.randint(40,80),
                    'rubber bullets':random.randint(40,80),
                    'smoke screen':random.randint(40,80),
                    'machine combo attack':random.randint(40,80),
                    'gun shot':random.randint(40,80)         
                        }
    
    def robot_wepon(self,robot_wepon_obj):
        wepon_choise = random.randint(1,4)
        i=1
        for key in robot_wepon_obj:
            if i == wepon_choise:
                val=robot_wepon_obj[key]
                return key ,val
            i=i+1
            

