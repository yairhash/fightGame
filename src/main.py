from functions.register import register
from functions.login import log_in
from functions.the_great_battle import the_great_battle
from functions.your_choise import your_choise
from functions.won_or_lost import won_or_lost



##### main #####

print('Wellcome to my game')
print(" press 1 for register and 2 for login")
user_choise=int(input(''))

if user_choise==1:
    register()  
else:
    user=log_in() 
    
player,opponent=your_choise()
the_great_battle(player,opponent)
won_or_lost(player,user)
   










    


