'''
Created by Unique Maharjan
Date: 2021-06-16
'''

import random

print('______________________________________________\n')
print('        Scissor, Paper , Rock Game            \n')
print('______________________________________________\n\n')
print('Press "0" to start Game')
print('Press "1" to close Game\n\n')


game_choice = {
    0 : 'Scissor',
    1 : 'Paper',
    2 : 'Rock'
}
win = "WoW!! You Just won against Computer!!!"
loss = "Sorry Computer Just Won!!!"
draw = "It's Draw. Same choice from both!!!"
def output():
    print(f'Computer choice: {game_choice[pick]}\n')
    print(f'Player choice : {_choice_}\n')

def Scissor():
    if game_choice[pick] == 'Scissor' and _choice_ == 'Scissor':
        output()
        print(f'{draw}\n')
    elif game_choice[pick] == 'Rock' and _choice_ == 'Scissor':
        output()
        print(f'{loss}\n')
    elif game_choice[pick] == 'Paper' and _choice_ == 'Scissor':
        output()
        print(f'{win}\n')

def Paper():
    if game_choice[pick] == 'Scissor' and _choice_ == 'Paper':
        output()
        print(f'{loss}\n')
    elif game_choice[pick] == 'Rock' and _choice_ == 'Paper':
        output()
        print(f'{win}\n')
    elif game_choice[pick] == 'Paper' and _choice_ == 'Paper':
        output()
        print(f'{draw}\n')

def Rock():
    if game_choice[pick] == 'Scissor' and _choice_ == 'Rock':
        output()
        print(f'{win}\n')
    elif game_choice[pick] == 'Rock' and _choice_ == 'Rock':
        output()
        print(f'{draw}\n')
    elif game_choice[pick] == 'Paper' and _choice_ == 'Rock':
        output()
        print(f'{loss}\n')



_user_ = ''
while len(_user_) == 0:
    _user_ = input('Enter your choice: ')
    if _user_ == '0':
        a = 'Y'
        while a == 'Y':
            _choice_ = input('Choose between Scissor, Paper and Rock: ')
            pick = random.randrange(0,3)
            Scissor()
            Rock()
            Paper()
            a = input('Do you want to play again?? (Y/N): ').upper()
    elif _user_ == 1:
        exit()
    else:
        print('Please press "0" or "1" only!!!')










