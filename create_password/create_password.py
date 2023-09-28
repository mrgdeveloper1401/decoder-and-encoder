import string
import random


# password = input('enetr password: ')
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
numbers = string.digits
symbol = string.punctuation


all = lower_case + upper_case + numbers + symbol
while True:
    
    print('1)create password\n2)exit')
    choose = int(input('choose option: '))
    print('*' * 40)
    if choose == 1:
        while True:
            print('len password must bigger then 6 characters and max length is 94')
            lenght = int(input('enter len password: '))
            if lenght < 6:
                print('you must enter bigger in 6 charachter')
                print('*' * 40)
                break
            else:
                password = "".join(random.sample(all, lenght))
            print(password)
        
    elif choose == 2:
        print('successfly exist program')
        break
    else:
        print('you must enter 1 or 2')
    