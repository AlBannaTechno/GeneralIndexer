from colorama import Fore, Back
class Cooloring():
    def __init__(self):
        self.bcolors = [
            Back.LIGHTCYAN_EX, Back.CYAN,
            Back.LIGHTYELLOW_EX, Back.YELLOW,
            Back.BLACK, Back.LIGHTBLACK_EX,
            Back.LIGHTBLUE_EX, Back.BLUE,
            Back.LIGHTGREEN_EX, Back.GREEN,
            Back.LIGHTWHITE_EX, Back.WHITE,
            Back.LIGHTRED_EX, Back.RED,
            Back.LIGHTMAGENTA_EX, Back.MAGENTA,
            Back.LIGHTYELLOW_EX, Back.YELLOW,
            Back.RESET
        ]
        self.fcolors = [
            Fore.LIGHTCYAN_EX, Fore.CYAN,
            Fore.LIGHTYELLOW_EX, Fore.YELLOW,
            Fore.BLACK, Fore.LIGHTBLACK_EX,
            Fore.LIGHTBLUE_EX, Fore.BLUE,
            Fore.LIGHTGREEN_EX, Fore.GREEN,
            Fore.LIGHTWHITE_EX, Fore.WHITE,
            Fore.LIGHTRED_EX, Fore.RED,
            Fore.LIGHTMAGENTA_EX, Fore.MAGENTA,
            Fore.LIGHTYELLOW_EX, Fore.YELLOW,
            Fore.RESET
        ]
        self.last = len(self.fcolors) - 1
