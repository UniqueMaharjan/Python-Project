'''
Created by Unique Maharjan
Date: 2021-06-15
'''

#Rectangle and square shape generator


rows = int(input('Enter rows :'))
columns = int(input('Enter columns : '))
symbol = input('Enter symbol use for creating object: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()