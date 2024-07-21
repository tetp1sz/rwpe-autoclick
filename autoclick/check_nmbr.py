from clicker import Clicker
from colorama import Fore
import keyboard as kb
import os


clear = lambda: os.system('cls')


def check_number(number):
    clicker = Clicker()

    # farm
    if number == 1:
        print(Fore.WHITE + '[i] Для активации макроса нажмите Z, для деактивации X, для выхода из макроса N')
        while True:
            if kb.is_pressed('z'):
                print(clicker.key_down_farm())
            elif kb.is_pressed('x'):
                print(clicker.key_up_farm())
            elif kb.is_pressed('n'):
                clear()
                break
    # box
    elif number == 2:
        print(Fore.WHITE + '[i] Для активации макроса нажмите Z, для деактивации X, для выхода из макроса N')
        while True:
            if kb.is_pressed('z'):
                print(clicker.key_down_box())
            elif kb.is_pressed('x'):
                print(clicker.key_up_box())
            elif kb.is_pressed('n'):
                clear()
                break

    # ferma
    elif number == 3:
        print(Fore.WHITE + '[i] Для активации макроса нажмите Z, для деактивации X, для выхода из макроса N')
        while True:
            if kb.is_pressed('z'):
                print(clicker.key_down_ferma())
            elif kb.is_pressed('x'):
                print(clicker.key_up_ferma())
            elif kb.is_pressed('n'):
                clear()
                break
