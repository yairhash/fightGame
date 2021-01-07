import random
class Wepon():
    
    def __init__(self,player):
        self.player=player
 
    archer_wepon_obj={
        'regular bow':random.randint(40,80),
        'multy arrow attack':random.randint(40,80),
        'fire bow':random.randint(40,80),
        'poisen arrow':random.randint(40,80),         
        'ice arrow':random.randint(40,80)
    } 

    wizard_wepon_obj={
        'dragon':random.randint(40,80),
        'special wand':random.randint(40,80),
        'stones from the sky':random.randint(40,80),
        'mega powers':random.randint(40,80),         
        'broom':random.randint(40,80)
    }

    robot_wepon_obj={
        'lazer eyes':random.randint(40,80),
        'rubber bullets':random.randint(40,80),
        'smoke screen':random.randint(40,80),
        'machine combo attack':random.randint(40,80),
        'gun shot':random.randint(40,80)         
    }

    goblin_wepon_obj={
        'dagger':random.randint(40,80),
        'axe':random.randint(40,80),
        'electro bomb':random.randint(40,80),
        'toxic breath':random.randint(40,80),
        'goblin bite' :random.randint(40,80)        
    }
    
    archer_shield_obj={
        'wood shield':random.randint(40,80),
        'metal-wood shield':random.randint(40,80),
        'spartan shield':random.randint(40,80),
        'raven shield':random.randint(40,80)      
    } 

    wizard_shield_obj={
        'magic shield':random.randint(40,80),
        'invisable glass shield':random.randint(40,80),
        'wind shield':random.randint(40,80),
        'bubble shield':random.randint(40,80)      
    }

    robot_shield_obj={
        'wood shield':random.randint(40,80),
        'metal shield':random.randint(40,80),
        'stone shield':random.randint(40,80),
        'super shield':random.randint(40,80)      
    } 
        
    goblin_shield_obj={ 
        'wood sheild':random.randint(40,80),
        'metal sheild':random.randint(40,80),
        'stone sheild':random.randint(40,80),
        'super sheild':random.randint(40,80)       
    }
    
        
    def get_wepon(self,second_return=False,opp=False): 
            if self.player=='wizard':
                wepon_name,wepon_power=self.returned_wepon(self.wizard_wepon_obj,opp)
                shield_name,shield_power=self.returned_wepon(self.wizard_shield_obj,opp)
            
            elif self.player =='archer':
                wepon_name,wepon_power=self.returned_wepon(self.archer_wepon_obj,opp)
                shield_name,shield_power=self.returned_wepon(self.archer_shield_obj,opp)
                
            elif self.player=='robot':    
                wepon_name,wepon_power=self.returned_wepon(self.robot_wepon_obj,opp)
                shield_name,shield_power=self.returned_wepon(self.robot_shield_obj,opp)
                
            elif self.player=='goblin':
                wepon_name,wepon_power=self.returned_wepon(self.goblin_wepon_obj,opp)
                shield_name,shield_power=self.returned_wepon(self.goblin_shield_obj,opp)
        
              
            if second_return:
                print("second_return")
                return wepon_name,wepon_power
            else:
                print("first_return")
                return wepon_name,wepon_power,shield_name,shield_power
                        
       
       
         
    def print_choise(self,obj):
        
            print ('choose your wepon')
            i=1
            for key in obj:  
                print (f'for {key} press {i}')
                i+=1
            player_choise=int((input('')))
            return player_choise
       
    def returned_wepon(self,obj,opp):
        if opp == False:
            p_choise=self.print_choise(obj)
        else: 
            p_choise=random.randint(1,len(obj))
        i=1    
        for key in obj:
            if i == p_choise:
                val=obj[key]
                return key ,val
            i+=1        
    
    
    
    
             
  
        

         
  

    
 
    
          


       
 
           

            
      
      
      
  