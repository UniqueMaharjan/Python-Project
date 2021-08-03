'''
Created by Unique Maharjan
Date: 2021-07-20
'''

def Start():
    user = input('Do you want to create your to-do list?? (Y/N): ')
    if user.lower() == 'n':
        print('Thank you for using this!!')
    while user.lower() == 'y':
            print('Please add your things to be done list below: ')
            user_input = ''
            user_data = []
            while user_input != None:
                take_input = input()
                user_data.append(take_input)
                if take_input.lower() == 'done':
                    endt = input('Are you done with giving list? (Y/N): ')
                    if endt.lower() == 'y':
                        exit()




Start()