lst = []
while True:
    print('choose option\n1) Encrypt: \n2) Decrypt: \n3) Exist: ')
    choose = int(input('your choose: '))
    
    if choose == 1:
        plain_text = input('enter your text: ')
        encrypt_text = ''
        for item in plain_text:
            en = ord(item)
            en +=2
            ent = chr(en)
            encrypt_text += ent
        print(encrypt_text)
        print('\n','*' * 20)
        
    elif choose == 2:
        encrypt_text = input('encrypt_text: ')
        plain_text = ''
        for item in encrypt_text:
            en = ord(item)
            en -=2
            ent = chr(en)
            plain_text += ent
        print(plain_text)
        print('\n','*' * 20)
        
    elif choose == 3:
        print('exit program')
        break
    else:
        print('out of range number please enter 1 or 2 or 3')
