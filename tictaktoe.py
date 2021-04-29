def print_board(pos):
    print('---------')
    print('|', pos[0], pos[1], pos[2], '|')
    print('|', pos[3], pos[4], pos[5], '|')
    print('|', pos[6], pos[7], pos[8], '|')
    print('---------')


def check_win(win):
    win_pos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    some_x = []
    some_o = []
    count = 0

    for i in win:
        if i == 'X':
            some_x.append(i)
        elif i == 'O':
            some_o.append(i)

    if (len(some_x) > (len(some_o) + 1) or len(some_o) > (len(some_x) + 1)) and len(some_x) != len(some_o):
        return print('Impossible')

    for i in win_pos:
        if win[i[0]] == win[i[1]] == win[i[2]]:
            count += 1
    if count > 1:
        return print('Impossible')

    for i in win_pos:
        if win[i[0]] == win[i[1]] == win[i[2]]:
            return print('{} wins'.format(win[i[0]]))

    if len(win) != (len(some_o) + len(some_x)):
        return print('Game not finished')

    if len(some_x) + len(some_o) == 9:
        return print('Draw')


user_input = input()
print_board(user_input)
check_win(user_input)
