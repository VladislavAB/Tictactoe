win_combinations = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
    [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def pole():
    print('-----------------')
    print(f'| {numbers[0]} |', f'| {numbers[1]} |', f'| {numbers[2]} |')
    print(f'| {numbers[3]} |', f'| {numbers[4]} |', f'| {numbers[5]} |')
    print(f'| {numbers[6]} |', f'| {numbers[7]} |', f'| {numbers[8]} |')
    print('-----------------')


x_combinations = []
o_combinations = []
step = 0


def check_win_x():
    for i in win_combinations:
        if i == x_combinations:
            print('Победил игрок X!')
            return True


def check_win_o():
    for i in win_combinations:
        if i == o_combinations:
            print('Победил игрок O!')
            return True


def check_er(player):
    if player.isalpha():
        if len(player) > 1:
            print('Вы ввели буквенные значения! Введите цифру!')
            return False
        else:
            print('Вы ввели букву! Введите цифру!')
            return False
    elif player == '' or player == ' ':
        print('Повторите ввод!')
        return False
    elif 1 > int(player) or int(player) > 9 or numbers[int(player) - 1] in ('X', 'O'):
        print('Диапазон 1-9! Вы ввели цифру вне диапазона или занятую клетку! Повторите ввод!')
        return False
    global step
    step = step + 1
    return True


player_x_move = True
print('Добро пожаловать!')
pole()

while True:
    if player_x_move:
        x_player = input('Игрок X, введите цифру(Q - выйти): ')
        if x_player == 'Q':
            break
        if check_er(x_player):
            x_combinations.append(int(x_player))
            numbers[int(x_player) - 1] = 'X'
            player_x_move = False
        pole()
        if check_win_x():
            break
        if step == 9:
            print('Ничья!')
            break
    else:
        o_player = input('Игрок O, введите цифру(Q - выйти): ')
        if o_player == 'Q':
            break
        if check_er(o_player):
            o_combinations.append(int(o_player))
            numbers[int(o_player) - 1] = 'O'
            player_x_move = True
        pole()
        if check_win_o():
            break
        if step == 9:
            print('Ничья!')
            break
