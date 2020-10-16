def the_big_win(
                character_wepon_power, 
                opponent_wepon_power, 
                choose_character, 
                character_full_life, 
                opponent_full_life):

    if character_wepon_power > opponent_wepon_power:
        print(f'your wepon\'s attack was stronger then your opponent. your new life satus is { character_full_life-opponent_wepon_power}')
        print(f'{choose_character} wins,you are on to the next fight')  
    else:
        print(f'your opponent\'s wepon attack was stronger then yours. your new life satus is {character_full_life-opponent_wepon_power}')
        print(f'{choose_character} you lost the battle')