import random 

class Wizard_wepon(): 
    
    def wepon_choise(self):
        print ('please choose your wepon:')
        print ('for dragon press 1')
        print ('for special wand press 2')
        print ('for stones from the sky press 3')
        print ('for mega powers press 4')
        print ('for broom press 5')
        
        your_wepon_coise=int(input(''))
        return your_wepon_coise
    
        
            
    wizard_wepon_obj={
                    'dragon':60,
                    'special wand':35,
                    'stones from the sky':50,
                    'mega powers':70,         
                    'broom':10
                        }
                        
    def wizard_wepon(self,wizard_wepon_obj,your_wepon_coise):
        i=1
        for key in wizard_wepon_obj:
            if i == your_wepon_coise:
                val=wizard_wepon_obj[key]
                return key ,val
            i=i+1
            
         
            

       

           
   
       