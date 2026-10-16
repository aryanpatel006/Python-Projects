import random
print('----Number Guessing Game----\nSelect Mode:\n- Easy\n- Medium\n- Hard')
mode = input('\nEnter the mode: ')

if mode == 'Easy':
    num = random.randint(1,10)
    count = 0
    while True:
        userNum = int(input('Enter a number: '))
        if userNum == num:
            count+=1
            print(f'Correct\nAttempts: {count}')
            break
        elif userNum > num:
            print('Too high.')
            count+=1
        elif userNum < num:
            print('Too low.')
            count+=1
elif mode == 'Medium':
    num = random.randint(1,50)
    count = 0
    while True:
        userNum = int(input('Enter a number: '))
        if userNum == num:
            count+=1
            print(f'Correct\nAttempts: {count}')
            break
        elif userNum > num:
            print('Too high.')
            count+=1
        elif userNum < num:
            print('Too low.')
            count+=1
elif mode == 'Hard':
    num = random.randint(1,100)
    count = 0
    while True:
        userNum = int(input('Enter a number: '))
        if userNum == num:
            count+=1
            print(f'Correct\nAttempts: {count}')
            break
        elif userNum > num:
            print('Too high.')
            count+=1
        elif userNum < num:
            print('Too low.')
            count+=1