from wepon.wepon import Wepon


def wepon_second_choise(player):
    print('you can change wepon:')
    wepon_class=Wepon(player)
    wepon_name,wepon_power=wepon_class.get_wepon(True)
    setattr(player,'wepon_name',wepon_name)
    setattr(player,'wepon_power',wepon_power)
    return wepon_name,wepon_power

        