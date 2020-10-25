import random
class Goblin_shield():
      
    goblin_shield_obj={
                    'wood sheild':random.randint(40,80),
                    'metal sheild':random.randint(40,80),
                    'stone sheild':random.randint(40,80),
                    'super sheild':random.randint(40,80)       
                        }

    def goblin_shield(self,goblin_shield_obj):
        shield_choise = random.randint(1,4)
        i=1
        for key in goblin_shield_obj:
            if i == shield_choise:
                val=goblin_shield_obj[key]
                return key ,val
            i=i+1
                