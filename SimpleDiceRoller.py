'''
Created by : Unique Maharjan
Date: 2021-06-16
'''


import random

print('________________________________\n')
print('           Dice Roller          \n')
print('________________________________\n')
print('''\nPress 0 to roll the dice
Press 1 to exit game\n\n
''')
_user_input = ''
while len(_user_input) == 0:
    _user_input = input('Enter your choice: ')
    if _user_input == '0':
        a = 'Y'
        while (a == 'Y'):
            rolling = random.randrange(1,7)
            if rolling == 1 or rolling == 6:
                print(f'You got {rolling}. So, either move {rolling} step forward or take out your character!\n\n')
            else:
                print(f'You got {rolling} number. So, move {rolling} step forward!!!\n\n')
            a = input('do you want to roll again?? Y/N : \n\n')

    elif _user_input == '1':
        exit()
    else:
        print('Please Check your number!!!')
