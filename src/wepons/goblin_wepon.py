import random   

class Goblin_wepon(): 
  
    goblin_wepon_obj={
                    'dagger':30,
                    'axe':38,
                    'electro bomb':45,
                    'toxic breath':69,
                    'goblin bite' :25        
                        }
                        
    def goblin_wepon(self,goblin_wepon_obj):
        wepon_choise = random.randint(1,4)        
        i=1
        for key in goblin_wepon_obj:
            if i == wepon_choise:
                val=goblin_wepon_obj[key]
                return key ,val
            i=i+1
            


       
