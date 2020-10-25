import random
class Archer_shield():

    def shield_choise(self):
        print ('please choose your shield:')
        print ('for wood sheild press 1')
        print ('for metal-wood shield press 2')
        print ('for partan shield bow press 3')
        print ('for raven shield press 4')
        your_shield_coise=int(input(''))
        return your_shield_coise          

    
    archer_shield_obj={
                        'wood shield':random.randint(40,80),
                        'metal-wood shield':random.randint(40,80),
                        'spartan shield':random.randint(40,80),
                        'raven shield':random.randint(40,80)      
                            }

    def archer_shield(self,archer_shield_obj,your_shield_coise):
        i=1
        for key in archer_shield_obj:
            if i == your_shield_coise: 
                val= archer_shield_obj[key]
                return key ,val
            i=i+1