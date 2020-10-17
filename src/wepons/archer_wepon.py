
class Archer_wepon(): 
    
    def wepon_choise(self):
        print ('please choose your wepon:')
        print ('for regular bow press 1')
        print ('for multy arrow attack press 2')
        print ('for fire bow 3')
        print ('for tiny bombs press 4')
        print ('for ice arrow press 5')
        your_wepon_coise=int(input(''))
        return your_wepon_coise             
    
    archer_wepon_obj={
                    'regular bow':10,
                    'multy arrow attack':72,
                    'fire bow':40,
                    'tiny bombs':30,         
                    'ice arrow':25
                        }
            
    def archer_wepon(self,archer_wepon_obj,your_wepon_coise):
        i=1
        for key in archer_wepon_obj:
            if i == your_wepon_coise:
                val=archer_wepon_obj[key]
                return key ,val
            i=i+1
            



           
           
           
           
           