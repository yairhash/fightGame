import random
class Wepon():         
    wizard_wepon_obj={
                    'dragon':60,
                    'special wand':35,
                    'stones from the sky':50,
                    'mega powers':70,         
                    'broom':10
                        }
                        
    def wizard_wepon(self,wizard_wepon_obj):
        i=0
        while i<=5:  
            random_num=random.randint(10,80)          
            for key in wizard_wepon_obj:

                wepon_power=wizard_wepon_obj[key]
                if wepon_power>=random_num:
                    return (key,wepon_power)  
            i=i+1            
   
             
    archer_wepon_obj={
                    'regular bow':10,
                    'multy arrow attack':72,
                    'fire bow':40,
                    'tiny bombs':30,         
                    'ice arrow':25
                        }
            
    def archer_wepon(self,archer_wepon_obj):
        i=0
        while i<=5:  
            random_num=random.randint(10,80)          
            for key in archer_wepon_obj:
                wepon_power=archer_wepon_obj[key]
                if wepon_power>=random_num:
                    return (key,wepon_power)  
            i=i+1 
            
                    
    goblin_wepon_obj={
                    'dagger':30,
                    'axe':38,
                    'electro bomb':45,
                    'toxic breath':69,
                    'goblin bite' :25        
                        }
                
    def goblin_wepon(self,goblin_wepon_obj):
        i=0
        while i<=5:  
            random_num=random.randint(10,80)          
            for key in goblin_wepon_obj:
                wepon_power=goblin_wepon_obj[key]
                if wepon_power>=random_num:
                    return (key,wepon_power)  
            i=i+1 
            
    robot_wepon_obj={
                    'lazer eyes':44,
                    'rubber bullets':33,
                    'smoke screen':20,
                    'machine combo attack':71,
                    'gun shot':50         
                        }
            
    def robot_wepon(self,robot_wepon_obj):
        i=0
        while i<=5:  
            random_num=random.randint(10,80)          
            for key in robot_wepon_obj:
                wepon_power=robot_wepon_obj[key]
                if wepon_power>=random_num:
                    return (key,wepon_power)  
            i=i+1   
            