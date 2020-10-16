from functions.the_great_battle import the_great_battle
from characters.wizard import Wizard
from characters.archer import Archer
from wepons.wepons import Wepon

print("which character you want , wizard or archer?")
choose_character = input('')
def your_choise(choose_character):
    if choose_character == 'archer':
        archer_name = input('enter archer name: ')
        archer_outfit = input('enter archer outfit: ')
        full_life = 100
        archer_wepon_class=Wepon()
        archer_wepon_name,archer_wepon_power=archer_wepon_class.archer_wepon(archer_wepon_class.archer_wepon_obj)
        class_name = Archer(archer_name,archer_outfit,full_life,archer_wepon_name,archer_wepon_power)
        the_great_battle(class_name, choose_character,archer_wepon_name,archer_wepon_power,full_life)
    else:
        wizard_name = input('enter wizard name: ')
        wizard_outfit = input('enter wizard outfit: ')
        full_life = 100
        wizard_wepon_class=Wepon()
        wizard_wepon_name,wizard_wepon_power=wizard_wepon_class.wizard_wepon(wizard_wepon_class.wizard_wepon_obj)
        class_name = Wizard( wizard_name, wizard_outfit,full_life,wizard_wepon_name,wizard_wepon_power)  # name is a class *****
        the_great_battle(class_name, choose_character,wizard_wepon_name,wizard_wepon_power,full_life)

##### main #####
your_choise(choose_character)
