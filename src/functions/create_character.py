from wepon.wepon import Wepon
from characters.character import Character
from .random_opponent import your_random_opponent


def create_character(wepon_name,shield_name,char_type):
    wepon_class=Wepon()
    wepon_power,shield_power=wepon_class.get_wepon_and_shield_power(wepon_name,shield_name,char_type)
    print(wepon_power,shield_power)
    player=Character(char_type,250,wepon_name,wepon_power,shield_name,shield_power,0,0)
    random_opp=your_random_opponent(char_type)
    opponent=Character(random_opp.char_type,random_opp.full_life,random_opp.wepon_name,random_opp.wepon_power,random_opp.shield_name,random_opp.shield_power,0,0)
    return player,opponent