import random
import os
import copy

playing_board = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]


positions = {1: [(0, 0), 'free'],
             2: [(0, 1), 'free'],
             3: [(0, 2), 'free'],
             4: [(0, 3), 'free'],
             5: [(1, 0), 'free'],
             6: [(1, 1), 'free'],
             7: [(1, 2), 'free'],
             8: [(1, 3), 'free'],
             9: [(2, 0), 'free'],
             10: [(2, 1), 'free'],
             11: [(2, 2), 'free'],
             12: [(2, 3), 'free'],
             13: [(3, 0), 'free'],
             14: [(3, 1), 'free'],
             15: [(3, 2), 'free'],
             16: [(3, 3), 'free']}

buttons = {'w': 'up',
          'a': 'left',
          's': 'down',
          'd': 'right'}

victory = None
movement = True # Check if a move was made
move = 0
score = 0

def clear_terminal(): # Clear the terminal
    os_name = 'cls' if os.name == 'nt' else 'clear'
    os.system(os_name)

def print_board(playing_board, score): # Display the game board
    cell_width = 6
    horizontal_line = '+' + ('-' * cell_width + '+') * 4
    clear_terminal() # Clear the terminal before  displaying the updated game board

    print(horizontal_line)
    for row in playing_board:
        print('|', end = '')
        for cell in row:
            if cell == 0:
                print(' '.center(cell_width) + '|', end = '')
            else:
                print(str(cell).center(cell_width) + '|', end = '')
        print()
        print(horizontal_line)
    print(f'\nСчет: {score}\n')

def checking_positions(positions, playing_board): # Check if cells are occupied
    free_positions = []
    key = 0
    for y in range(4):
        for x in range(4):
            key += 1
            if playing_board[y][x] == 0:
                positions[key][1] = 'free'
                free_positions.append(key)
            else:
                positions[key][1] = 'busy'
    return free_positions

def filling_in_empty_cells(free_positions, positions, move): # Add new numbers to empty cells
    if move == 1:
        cells = random.sample(free_positions, 2)
    else:
        cells = [random.choice(free_positions)]
    
    for i in cells:
        number = random.random()
        if number <= 0.9:
            playing_board[positions[i][0][0]][positions[i][0][1]] = 2
        else:
            playing_board[positions[i][0][0]][positions[i][0][1]] = 4
        positions[i][1] = 'busy'

def change_on_the_board(victory):
    free_positions = checking_positions(positions, playing_board)
    if free_positions: 
        filling_in_empty_cells(free_positions, positions, move)


# Control functions

# Move up
def up(playing_board, movement):
    global score
    while True:
        changes_board = copy.deepcopy(playing_board)
        for y in range(0, 4):
            for x in range(0, 4):
                if x != 3:
                    if playing_board[x][y] == 0 and playing_board[x + 1][y] != 0 and x != 3:
                        playing_board[x][y], playing_board[x + 1][y] = playing_board[x + 1][y], playing_board[x][y]
                        movement = True
                 
        if changes_board == playing_board:
            rotated_columns = [[], [], [], []]
            columns = [[], [], [], []]
            for y in range(0, 4):
                for x in reversed(range(4)):
                    rotated_columns[y].append(playing_board[x][y])

            for x in range(0, 4):
                for y in reversed(range(4)):
                    if y > 0 and rotated_columns[x][y] == rotated_columns[x][y - 1] and rotated_columns[x][y] != 0:
                        rotated_columns[x][y] += rotated_columns[x][y - 1]
                        rotated_columns[x].pop(y - 1)
                        row = rotated_columns[x]
                        row.insert(0, 0)
                        rotated_columns[x] = row
                        score += rotated_columns[x][y]
                        movement = True

            i = 0
            for x in reversed(range(4)):
                for y in range(0, 4):
                    columns[i].append(rotated_columns[y][x])
                i += 1
            
            return columns, movement

# Move left
def left(playing_board, movement):
    global score
    while True:
        changes_board = copy.deepcopy(playing_board)
        for x in range(0, 4):
            for y in range(0,4):
                if y != 3:
                    if playing_board[x][y] == 0 and playing_board[x][y + 1] != 0:
                        playing_board[x][y], playing_board[x][y + 1] = playing_board[x][y + 1], playing_board[x][y]
                        movement = True
                 
        if changes_board == playing_board:
            for x in range(0, 4):
                for y in range(0, 4):
                    if y < 3 and playing_board[x][y] == playing_board[x][y + 1] and playing_board[x][y] != 0:
                        playing_board[x][y] += playing_board[x][y + 1]
                        playing_board[x].pop(y + 1)
                        row = playing_board[x]
                        row.append(0)
                        playing_board[x] = row
                        score += playing_board[x][y]
                        movement = True
            return movement

# Move down
def down(playing_board, movement):
    global score
    while True:
        changes_board = copy.deepcopy(playing_board)
        for y in range(0, 4):
            for x in reversed(range(4)):
                if x != 0:
                    if playing_board[x][y] == 0 and playing_board[x - 1][y] != 0 and x != 0:
                        playing_board[x][y], playing_board[x - 1][y] = playing_board[x - 1][y], playing_board[x][y]
                        movement = True
                 
        if changes_board == playing_board:
            rotated_columns = [[], [], [], []]
            columns = [[], [], [], []]
            for y in range(0, 4):
                for x in reversed(range(4)):
                    rotated_columns[y].append(playing_board[x][y])

            for x in range(0, 4):
                for y in range(0, 4):
                    if y < 3 and rotated_columns[x][y] == rotated_columns[x][y + 1] and rotated_columns[x][y] != 0:
                        rotated_columns[x][y] += rotated_columns[x][y + 1]
                        rotated_columns[x].pop(y + 1)
                        row = rotated_columns[x]
                        row.append(0)
                        rotated_columns[x] = row
                        score += rotated_columns[x][y]
                        movement = True

            i = 0
            for x in reversed(range(4)):
                for y in range(0, 4):
                    columns[i].append(rotated_columns[y][x])
                i += 1

            return columns, movement

# Move right
def right(playing_board, movement):
    global score
    while True:
        changes_board = copy.deepcopy(playing_board)
        for x in range(0, 4):
            for y in reversed(range(4)):
                if y != 0:
                    if playing_board[x][y] == 0 and playing_board[x][y - 1] != 0:
                        playing_board[x][y], playing_board[x][y - 1] = playing_board[x][y - 1], playing_board[x][y]
                        movement = True
                 
        if changes_board == playing_board:
            for x in range(0, 4):
                for y in reversed(range(4)):
                    if y > 0 and playing_board[x][y] == playing_board[x][y - 1] and playing_board[x][y] != 0:
                        playing_board[x][y] += playing_board[x][y - 1]
                        playing_board[x].pop(y - 1)
                        row = playing_board[x]
                        row.insert(0, 0)
                        playing_board[x] = row
                        score += playing_board[x][y]
                        movement = True
            return movement

def move_on_the_board(buttons): # Movement function
    global playing_board, movement 
    while True:
        try:
            button = input('w - up | a - left | s - down | d - right\n>>> ').lower()
            if not button in list(buttons.keys()):
                raise KeyError
            button = buttons.get(button)

        except:
            print_board(playing_board, score)
            print('\nТакой кнопки не существует\n')
            continue

        else:
            if button == 'up':
                playing_board, movement = up(playing_board, movement)

            elif button == 'left':
                movement = left(playing_board, movement)

            elif button == 'down':
                playing_board, movement = down(playing_board, movement)

            elif button == 'right':
                movement = right(playing_board, movement)

            break

def victory_check(playing_board): # Check if 2048 is on the board
    positions_key = list(positions.keys())
    for row in playing_board:
        if 2048 in row:
            return True

def defeat_check(playing_board): # Check for possible moves when the board is full
    for x in range(0, 4):
        for y in range(0, 4):  # First version of the check
            # if x == 0:
            #     if y == 0:
            #         if playing_board[x][y] == playing_board[x][y + 1] or playing_board[x][y] == playing_board[x + 1][y]:
            #             return
            #     elif y == 3:
            #         if playing_board[x][y] == playing_board[x][y - 1] or playing_board[x][y] == playing_board[x + 1][y]:
            #             return
            #     else:
            #         if playing_board[x][y] == playing_board[x][y - 1] or playing_board[x][y] == playing_board[x + 1][y] or playing_board[x][y] == playing_board[x][y + 1]:
            #             return
                    
            # elif x == 3:
            #     if y == 0:
            #         if playing_board[x][y] == playing_board[x - 1][y] or playing_board[x][y] == playing_board[x][y + 1]:
            #             return
            #     elif y == 3:
            #         if playing_board[x][y] == playing_board[x - 1][y] or playing_board[x][y] == playing_board[x][y - 1]:
            #             return
            #     else:
            #         if playing_board[x][y] == playing_board[x][y - 1] or playing_board[x][y] == playing_board[x - 1][y] or playing_board[x][y] == playing_board[x][y + 1]:
            #             return
            
            # else:
            #     if y == 0:
            #         if playing_board[x][y] == playing_board[x - 1][y] or playing_board[x][y] == playing_board[x][y + 1] or playing_board[x][y] == playing_board[x + 1][y]:
            #             return
            #     elif y == 3:
            #         if playing_board[x][y] == playing_board[x - 1][y] or playing_board[x][y] == playing_board[x][y - 1] or playing_board[x][y] == playing_board[x + 1][y]:
            #             return
            #     else:
            #         if playing_board[x][y] == playing_board[x][y - 1] or playing_board[x][y] == playing_board[x - 1][y] or playing_board[x][y] == playing_board[x][y + 1] or playing_board[x][y] == playing_board[x + 1][y]:
            #             return
            
            # Second version of the check
            if x < 3:
                if playing_board[x][y] == playing_board[x + 1][y]:
                    return
            if y < 3:
                if playing_board[x][y] == playing_board[x][y + 1]:
                    return                                   
    return False


while victory == None:
    move += 1
    victory = victory_check(playing_board)
    if victory == None:
        if movement == True:
            change_on_the_board(victory)
            movement = None
        print_board(playing_board, score)
        free_positions = checking_positions(positions, playing_board)
        if not free_positions:
            victory = defeat_check(playing_board)
            if victory != None:
                break
            
        move_on_the_board(buttons)

print_board(playing_board, score)
if victory == True:
    print('Вы победили! 2048 собрано!')

elif victory == False:
    print('Возможных ходов не осталось. Вы проиграли!')
