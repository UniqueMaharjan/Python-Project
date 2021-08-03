'''
Created by Unique Maharjan
Date: 2021-06-15
'''

#Countdown in second only
import time

sec = int(input('Enter second for countdown:'))
remark = input('Enter remark for this countdown: ')

for i in range(sec,0,-1):
    print(i)
    time.sleep(1)
print(f'{remark}!!!!')