from clicker import Clicker
from check_nmbr import check_number, clear
from art import *
from colorama import init, Fore

init()


if __name__ == '__main__':
    clicker = Clicker()

    tprint('macros rwpe', font='bloody')
    print('by tetp1sz')

    while True:
        try:
            number = clicker.menu()
            clear()
        except ValueError:
            print(Fore.RED + '[!] Введите целое число!')
        else:
            number == 1 or 2 or 3 if check_number(number) else print(Fore.RED + '[!] Функция не найдена!')
