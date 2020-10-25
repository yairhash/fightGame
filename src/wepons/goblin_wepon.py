import random   

class Goblin_wepon(): 
  
    goblin_wepon_obj={
                    'dagger':random.randint(40,80),
                    'axe':random.randint(40,80),
                    'electro bomb':random.randint(40,80),
                    'toxic breath':random.randint(40,80),
                    'goblin bite' :random.randint(40,80)        
                        }
                        
    def goblin_wepon(self,goblin_wepon_obj):
        wepon_choise = random.randint(1,4)        
        i=1
        for key in goblin_wepon_obj:
            if i == wepon_choise:
                val=goblin_wepon_obj[key]
                return key ,val
            i=i+1
            


       
