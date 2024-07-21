import pyautogui as pya
from colorama import Fore


class Clicker:
    def menu(self):
        macros_number = int(input(Fore.WHITE + '\n[?] Введите нужный макрос:\n\t1. Автофарм\n\t2. Бокс\n\t3. Колхоз (пшено)\n\t> '))
        return macros_number

    def key_down_farm(self):
        pya.keyDown('z')
        pya.keyDown('shift')
        pya.mouseDown()
        return Fore.GREEN + '[i] Макрос фарма активен'

    def key_up_farm(self):
        pya.keyUp('z')
        pya.keyUp('shift')
        pya.mouseUp()
        return Fore.RED + '[i] Макрос фарма неактивен'

    def key_down_box(self):
        pya.keyDown('z')
        pya.keyDown('w')
        pya.keyDown('ctrl')
        pya.keyDown('space')
        return Fore.GREEN + '[i] Макрос бокса активен'

    def key_up_box(self):
        pya.keyUp('z')
        pya.keyUp('w')
        pya.keyUp('ctrl')
        pya.keyUp('space')
        return Fore.RED + '[i] Макрос бокса неактивен'

    def key_down_ferma(self):
        pya.keyDown('w')
        pya.keyDown('ctrl')
        pya.mouseDown()
        return Fore.GREEN + '[i] Макрос фермы активен'

    def key_up_ferma(self):
        pya.keyUp('w')
        pya.keyUp('ctrl')
        pya.mouseUp()
        return Fore.RED + '[i] Макрос фермы неактивен'
