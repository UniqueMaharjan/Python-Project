#Calculator
print('-----------------------------------------\n')
print('               CALCULATOR                \n')
print('_________________________________________\n')
print('''Press no. to access following features:\n
      0: Addition
      1: Substraction
      2: Divide
      3: Multiply \n'''
      )
user_data = int(input('Enter your choice :'))
if user_data == 0:
    print('--------ADDITION----------')
    a = int(input('Enter your 1st number : \t'))
    b = int(input('Enter your 2nd number : \t'))
    print(f'Your result is : \n'
          f'{a} + {b} = {a+b}')
elif user_data == 1:
    print('--------SUBTRACTION----------')
    a = int(input('Enter your 1st number : \t'))
    b = int(input('Enter your 2nd number : \t'))
    print(f'Your result is :'
          f'{a} - {b} = {a - b}')
elif user_data == 2:
    print('--------DIVIDE----------')
    a = int(input('Enter your 1st number : \t'))
    b = int(input('Enter your 2nd number : \t'))
    print(f'Your result is :'
          f'{a} / {b} = {a/b}')
elif user_data == 3:
    print('--------Multiplication----------')
    a = int(input('Enter your 1st number : \t'))
    b = int(input('Enter your 2nd number : \t'))
    print(f'Your result is :'
          f'{a} * {b} = {a*b}')
else:
    print('Error!! Please Check choice of number and type wisely...')