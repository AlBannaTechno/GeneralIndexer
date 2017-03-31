from docopt import docopt
from colorama import Fore, Back
from Base import Controller
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

commands="""

Usage:
 GeneralIndexer -h | --help
 GeneralIndexer find (file | mfile) <data>  [--f <fpath> ] [--result <expression>]

Options:
 -h , --help
 -f fbath
 -result expression     we can use this like index,name,path:012 or we can do name,index : 10
"""
# simple command  >python GeneralIndexer.py find file python --f os.txt --result 01
def main():
    arguments = docopt(commands, version='1.0.0rc2')
    print(arguments)
    cont=Controller()
    newLine="\n"
    sepratore=" , "
    exp_list=[]
    # file=[]
    if arguments.get('find'):
        if arguments.get('--result'):
            expressions=arguments.get('<expression>')
            print(expressions)
            for e in expressions:
                if int(e) in range(0,3):
                    exp_list.append(int(e))
                else:
                    print("Warn : InValid Value in expression")
        else:
            exp_list=[1]
        data=arguments.get('<data>')
        if arguments.get('--f'):
            file = open(arguments.get('<fpath>'), 'w', encoding='utf-8')
            file.close()
        if arguments.get('mfile'):
            data=data.split(',')
            for d in data:
                databooks=cont.get_books_name_like(arguments[d])
                if arguments.get('--f'):
                    file = open(arguments.get('<fpath>'), 'a', encoding='utf-8')
                    file.write("#"*20+str(d)+"#"*20+newLine)
                    for db in databooks:
                        for _exp in exp_list:
                            file.write(str(db[_exp])+sepratore)
                        file.write(newLine)
                    file.close()
                else:
                    print("#"*20+str(d)+"#"*20)
                    for db in databooks:
                        for _exp in exp_list:
                            print(db[_exp],end=sepratore)
                        print("")
        elif arguments.get('file'):
            databooks = cont.get_books_name_like(data)
            if arguments.get('--f'):
                file = open(arguments.get('<fpath>'), 'a', encoding='utf-8')
                for db in databooks:
                    for _exp in exp_list:
                        file.write(str(db[_exp])+sepratore)
                    file.write(newLine)
                file.close()
            else:
                for db in databooks:
                    for _exp in exp_list:
                        print(db[_exp],end=sepratore)
                    print("")
if __name__ == '__main__':
    main()