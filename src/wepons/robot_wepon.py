import random
class Robot_wepon():
      
    robot_wepon_obj={
                    'lazer eyes':44,
                    'rubber bullets':33,
                    'smoke screen':20,
                    'machine combo attack':71,
                    'gun shot':50         
                        }
    
    def robot_wepon(self,robot_wepon_obj):
        wepon_choise = random.randint(1,4)
        i=1
        for key in robot_wepon_obj:
            if i == wepon_choise:
                val=robot_wepon_obj[key]
                return key ,val
            i=i+1
            

