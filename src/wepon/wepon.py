import random
import itertools
class Wepon():
 
  
    wepon_list=[
        {
            'name':'archer',
            'regular bow':random.randint(40,80),
            'multy arrow attack':random.randint(40,80),
            'fire bow':random.randint(40,80),
            'poisen arrow':random.randint(40,80),         
            'ice arrow':random.randint(40,80)
        },
        {
            'name':'wizard',
            'dragon':random.randint(40,80),
            'special wand':random.randint(40,80),
            'stones from the sky':random.randint(40,80),
            'mega powers':random.randint(40,80),         
            'broom':random.randint(40,80)
        },
        {
            'name':'robot',
            'lazer eyes':random.randint(40,80),
            'rubber bullets':random.randint(40,80),
            'smoke screen':random.randint(40,80),
            'machine combo attack':random.randint(40,80),
            'gun shot':random.randint(40,80)         
        },
        {
            'name':'goblin',
            'dagger':random.randint(40,80),
            'axe':random.randint(40,80),
            'electro bomb':random.randint(40,80),
            'toxic breath':random.randint(40,80),
            'goblin bite' :random.randint(40,80)        
        }  
    ]
    
    shield_list=[
        {
            'name':'archer',
            'wood shield':random.randint(40,80),
            'metal-wood shield':random.randint(40,80),
            'spartan shield':random.randint(40,80),
            'raven shield':random.randint(40,80)      
        },
        {
            'name':'wizard',
            'magic shield':random.randint(40,80),
            'invisable glass shield':random.randint(40,80),
            'wind shield':random.randint(40,80),
            'bubble shield':random.randint(40,80),      
            'ofir shield':random.randint(40,80)      
        },
        {
            'name':'robot',
            'wood shield':random.randint(40,80),
            'metal shield':random.randint(40,80),
            'stone shield':random.randint(40,80),
            'super shield':random.randint(40,80)      
        },
        { 
            'name':'goblin', 
            'wood sheild':random.randint(40,80),
            'metal sheild':random.randint(40,80),
            'stone sheild':random.randint(40,80),
            'super sheild':random.randint(40,80)       
        }
    ]
    
    
    def print_wepon_and_shield(self,char_type):
        wepon_list=self.wepon_list
        shield_list=self.shield_list
        for(wepon_obj,shield_obj) in zip(wepon_list,shield_list):
            if char_type==wepon_obj['name'] and char_type==shield_obj['name']:
                   print(wepon_obj.keys(),shield_obj.keys())                     
            return 'somthing went wrong'
            
            
     
     
    def get_wepon_and_shield_power(self,wepon_name,shield_name,char_type):
        shield_list=self.shield_list
        wepon_list=self.wepon_list
        print(wepon_name)
        print(shield_name)
        for( wepon_obj,shield_obj) in zip(wepon_list,shield_list):
            if char_type==wepon_obj['name'] and char_type==shield_obj['name']:
                    wepon_power=wepon_obj.get(wepon_name)
                    shield_power=shield_obj.get(shield_name)
                    print(wepon_power,shield_power)
                    return wepon_power,shield_power                     
            return 'somthing went wrong'
            
            
     
            
           
  
                 
  
          

    
 
    
          


       
 
           

            
      
      
      
  