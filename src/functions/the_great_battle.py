from .random_opponent import your_random_opponent
from .the_big_win import the_big_win

def the_great_battle(class_character, choose_character,wepon_name,wepon_power,full_life):

    print("attack")
    if choose_character == 'archer':
        print(f'your are attackig wepon is {class_character.wepon_name} with power of {class_character.wepon_power}.your starting life status is {class_character.full_life}')
        opponent=your_random_opponent()
        print(f'your opponent is:{opponent.char_type},and his attacking wepon is {opponent.wepon_name} with the power of {opponent.wepon_power}.his starting life status is {opponent.full_life}')
        the_big_win(class_character.wepon_power,opponent.wepon_power,choose_character,class_character.full_life,opponent.full_life)
    else:
        print(f'your are attackig wepon is {class_character.wepon_name} with power of {class_character.wepon_power}.your starting life status is {class_character.full_life}')
        opponent=your_random_opponent()
        print(f'your opponent is {opponent.char_type},and his attacking wepon is{opponent.wepon_name} with the power of{opponent.wepon_power}.his starting life status is {opponent.full_life}')
        the_big_win(class_character.wepon_power,opponent.wepon_power,choose_character,class_character.full_life,opponent.full_life)