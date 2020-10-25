import random
class Wizard_shield():
    
    def shield_choise(self):
        print ('please choose your shield:')
        print ('for magic shield press 1')
        print ('for invisable glass shield press 2')
        print ('for wind shield bow press 3')
        print ('for bubble shield press 4')
        your_shield_coise=int(input(''))
        return your_shield_coise          


      
    wizard_shield_obj={
                        'magic shield':random.randint(40,80),
                        'invisable glass shield':random.randint(40,80),
                        'wind shield':random.randint(40,80),
                        'bubble shield':random.randint(40,80)      
                            }

    def wizard_shield(self,wizard_shield_obj,your_shield_coise):
        i=1
        for key in   wizard_shield_obj:
            if i == your_shield_coise:
                val= wizard_shield_obj[key]
                return key ,val
            i=i+1