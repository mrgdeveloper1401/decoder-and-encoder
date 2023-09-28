import time
from os import system, name

while True:
    choose = input('do you want start? (y/n) ')
    if choose == 'yes' or choose == 'YES' or choose == 'Y' or choose == 'y':
        houre = int(input('enter your hour: '))
        minute = int(input('enter your minute: '))
        second = int(input('enter your second: '))
        total = houre * 60 + minute * 60 + second
        
        print('timer start now ....')
        time.sleep(1)
        while total >= 1:
            print(total)
            total -= 1
            time.sleep(1)
            if name == 'nt':
                system('cls')
            system('clear')
        print('time end ....')
    elif choose == 'no' or choose ==  'NO' or choose == 'n' or choose == 'N':
        print('successlfy exist progrmm')
        break