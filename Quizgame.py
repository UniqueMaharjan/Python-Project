'''
Created by Unique Maharjan
Date: 2021-06-28
'''



#---------------------------------------------
def players():
    print('Do you want to play 1 player or 2 player: \nPress "1"for 1 palyer\nPress "2" for 2 player')
    user = None
    user_no = ['1','2']
    while not user in user_no:
        user = input('Enter your Choice: ')
        if user == '1':
            player1()
        elif user == '2':
            player2()

#---------------------------------------------
def player1():
    guesses = []
    question_no = 1
    correct_guess = 0
    for key in question:
        print(f'================[{question_no}]================')
        print(key)

        for i in options[question_no - 1]:
            print(i)
        guess = None
        option = ['A', 'B', 'C', 'D']
        while not guess in option:
            guess = input('Choose your answer wisely: ').upper()
            guess = guess.upper()
            guesses.append(guess)
            question_no += 1
            correct_guess += check_answer_player1(question.get(key),guess)

    score1(correct_guess,guesses)


#----------------------------------------------------
def check_answer_player1(answer,guess):
        if answer == guess:
            return 1
        else:
            return 0

#------------------------------------------------------
def score1(correct_guess,guesses):
    print('+++++++++++++++++')
    print('+++++Results+++++')
    print('+++++++++++++++++')
    print('\n')
    print('Answer: ',end='')
    for i in question:
        print(question.get(i),end=' ')
    print('\n')
    print('Guesses: ',end='')
    for i in guesses:
        print(i,end=' ')
    print()
    print('Your score is '+str(correct_guess))




#===================================================
def player2():
    guesses1 = []
    guesses2 = []
    question_no = 1
    correct_answer1 = 0
    correct_answer2 = 0
    for key in question:
        print(f'================[{question_no}]================')
        print(key)

        for i in options[question_no - 1]:
            print(i)
        guess = None
        guess1 = None
        option = ['A', 'B', 'C', 'D']
        while not (guess and guess1) in option:
            guess = input('Player 1 Choose your answer wisely: ').upper()
            guess1 = input('Player 2 Choose your answer wisely: ').upper()
            print('\n')
            guesses1.append(guess)
            guesses2.append(guess1)
            question_no += 1
            correct_answer1 += check_answer_player1(question.get(key),guess)
            correct_answer2 += check_answer_player1(question.get(key),guess1)

    score(correct_answer1,correct_answer2,guesses1,guesses2)
#-----------------------------------------------------
def score(player1ans,player2ans,player1guess,player2guess):
    print('+++++++++++++++++')
    print('+++++Results+++++')
    print('+++++++++++++++++')
    print('\n')
    print('Answer: ', end='')
    for i in question:
        print(question.get(i), end=' ')
    print('\n')
    print('Guess of Player 1: ', end=' ')
    for i in player1guess:
        print(i, end=' ')
    print()
    print('Guess of Player 2: ',end=' ')
    for i in player2guess:
        print(i,end=' ')
    print()
    print('Score of Player 1: ' +str(player1ans))
    print('Score of Player 2: ' +str(player2ans))

#-----------------------------------------------------
def play_again():
    remainder = None
    while not remainder == 'Y':
        remainder = input('Do you want to play again? (Y/N): ').upper()
        if remainder == 'Y':
            return True
        elif remainder == 'N':
            return False
        else:
            print('Please type correctly!!')

#-------------------------------------------------------
question = {
    'How many time zones are there in Russia?':'B',
    "What's the national flower of Japan?":'C',
    'How many stripes are there on the US flag?' : 'D',
    "What's the national animal of Australia?" : "A",
    "How many days does it take for the Earth to orbit the Sun?": "B",
    "Which of the following empires had no written language?":"A",
    "Until 1923, what was the Turkish city of Istanbul called?":"B"
}

options = [['A: 12','B: 11','C: 13','D: 15'],
    ['A: Sun flower','B: Rose','C: Cherry blossom','D:Daisy'],
    ['A: 25','B: 35','C: 10','D: 13'],
    ['A: Red Kangaroo','B: Tiger','C: Lion','D: Kiwi'],
    ['A: 200','B: 365','C: 300','D: 265'],
    ['A: Incan','B: Aztec','C: Egyptian','D: Roman'],
    ['A: Ankara','B: Constantinople','C: Antalya','D: Izmir']]

print('________________________________________________')
print('===================Quiz Game====================')
print('________________________________________________\n\n\n')

print('Press "0" to start Game and Press "1" to exit Game!!\n')
a = None
while not a == '0':
    a = input('Enter your choice: ')
    print('\n\n')
    if a == '1':
        exit()
    elif a == '0':
        players()
        #new_game()
    else:
        print('---------Please check what you are selecting!!!!---------')

while play_again():
    print('\n')
    players()

print('---------Thank you for playing!!!---------')



