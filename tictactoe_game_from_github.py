from copy import deepcopy
from time import sleep

# Resets the board
def reset():
    global hor,ver,dia
    hor = [[None,None,None] for i in range(3)]
    ver = deepcopy(hor)
    dia = [[None,None,None] for i in range(2)]

reset()
rules = '''Rules:
2 people can be O or X. To fill a spot in the 3x3 grid, enter 1,2,3,4,5,6,7,8, or 9.
You can not put your letter into a spot with already a letter.
Whoever who gets three in a row horizontaly, verticaly, or diagonally, wins.'''
print(rules)
sleep(1)
# Puts in the inputs
def putin(num1,type1):
    global hor,ver,dia
    # hor/dia
    if num1 in (1,2,3):
        if hor[0][num1-1] != None:
            print('That spot is already taken.\n')
            return 'bad'
        if num1 == 1:
            dia[0][0] = type1
        elif num1 == 3:
            dia[1][0] = type1
        hor[0][num1-1] = type1
    if num1 in (4,5,6):
        if hor[1][num1-4] != None:
            print('That spot is already taken.\n')
            return 'bad'
        if num1 == 5:
            dia[0][1] = type1
            dia[1][1] = type1
        hor[1][num1-4] = type1
    if num1 in (7,8,9):
        if hor[2][num1-7] != None:
            print('That spot is already taken.\n')
            return 'bad'
        if num1 == 9:
            dia[0][2] = type1
        elif num1 == 7:
            dia[1][2] = type1
        hor[2][num1-7] = type1
    # ver
    if num1 in (1,4,7):
        if num1 == 1:
            num1 = 0
        if num1 == 4:
            num1 = 1
        if num1 == 7:
            num1 = 2
        ver[0][num1] = type1
    if num1 in (2,5,8):
        if num1 == 2:
            num1 = 0
        if num1 == 5:
            num1 = 1
        if num1 == 8:
            num1 = 2
        ver[1][num1] = type1
    if num1 in (3,6,9):
        if num1 == 3:
            num1 = 0
        if num1 == 6:
            num1 = 1
        if num1 == 9:
            num1 = 2
# Shows the board
def show_board():
    global hor
    end = ''
    first = True
    final = False
    for row in hor:
        if not first:
            end += '\n-------'
        else:
            first = False
        end += '\n|'
        for item in row:
            if row[-1] == item:
                final = True
            if not final:
                if item:
                    end += item + '|'
                else:
                    end += ' |'
            else:
                if item:
                    end += item + '|'
                else:
                    end += ' |'
    print(end+'\n')
# Tests for wins
def check():
    stop = False
    done = False
    sleep(0.2)
    show_board()
    for fir,sec,thir in hor:
        if fir == sec and fir == thir and fir != None:
            if fir == 'o':
                print('Player O wins!')
            elif fir == 'x':
                print('Player X wins!')
            done = True
            break
    for fir,sec,thir in ver:
        if fir == sec and fir == thir and fir != None:
            if fir == 'o':
                print('Player O wins!')
            elif fir == 'x':
                print('Player X wins!')
            done = True
            break
    for fir,sec,thir in dia:
        if fir == sec and fir == thir and fir != None:
            if fir == 'o':
                print('Player O wins!')
            elif fir == 'x':
                print('Player X wins!')
            done = True
            break
    if done:
        while True:
            again = input('Play again (y/n)? ')
            if again == 'y':
                break
            elif again == 'n':
                stop = True
                break
            else:
                print('Please enter y or n.')
                continue
        return stop
    else:
        return 'continue on'
def helpme():
    global hor
    old = hor
    hor = [['1','2','3'],['4','5','6'],['7','8','9']]
    show_board()
    hor = deepcopy(old)
helpme()
print('Enter help at anytime to get the grid layout.')

# Main loop
sleep(1)
while True:
    # If player X didn't win already, Player O's turn
    while True:
        try:
            num1 = input('Player O: ')
            num1 = int(num1)
        except:
            if num1 == 'help':
                helpme()
            else:
                print('Please enter a number.\n')
            continue
        else:
            if num1 not in (1,2,3,4,5,6,7,8,9,'help'):
                print('Please enter 1,2,3,4,5,6,7,8,9,or help.')
                continue
            a = putin(num1,'O')
            if a:
                continue
            break
    # Check for win
    good = check()
    if good == True:
        break
    elif good == False:
        print()
        reset()
        continue
    # If not, Player X's turn
    while True:
        try:
            num2 = input('Player X: ')
            num2 = int(num2)
        except:
            if num2 == 'help':
                helpme()
            else:
                print('Please enter a number.\n')
            continue
        else:
            if num2 not in (1,2,3,4,5,6,7,8,9,'help'):
                print('Please enter 1,2,3,4,5,6,7,8,9,or help.')
                continue
            a = putin(num2,'X')
            if a:
                continue
            break
    # Check for win
    good = check()
    if good == True:
        break
    elif good == False:
        print()
        reset()
        continue
