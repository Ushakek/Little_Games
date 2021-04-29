def print_board(pos):
    print('---------')
    print('|', pos[0], pos[1], pos[2], '|')
    print('|', pos[3], pos[4], pos[5], '|')
    print('|', pos[6], pos[7], pos[8], '|')
    print('---------')


def check_win(win):
    win_pos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for i in win_pos:
        if win[i[0]] == win[i[1]] == win[i[2]]:
            return win[i[0]]
    return False


def check_game(pos):
    some_x = []
    some_o = []

    for i in pos:
        if i == 'X':
            some_x.append(i)
        elif i == 'O':
            some_o.append(i)
    if len(pos) != (len(some_o) + len(some_x)):
        return 'Game not finished'


user_input = input()
print_board(user_input)
who_win = check_win(user_input)

if not who_win:
    print(check_game(user_input))
else:
    print('{} wins'.format(who_win))
