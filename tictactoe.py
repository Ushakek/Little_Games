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

    for i in win:
        if i == 'X':
            some_x.append(i)
        elif i == 'O':
            some_o.append(i)

    for i in win_pos:
        if win[i[0]] == win[i[1]] == win[i[2]] != ' ':
            print('{} wins'.format(win[i[0]]))
            return False

    if len(win) != (len(some_o) + len(some_x)):
        print('Game not finished')
        return True

    if len(some_x) + len(some_o) == 9:
        print('Draw')
        return False


def step(pos):
    board = [[pos[0], pos[1], pos[2]],
             [pos[3], pos[4], pos[5]],
             [pos[6], pos[7], pos[8]]]
    count = 0
    game = True

    while game:

        try:  # ловим ошибки неправильного ввода(буквы, более, чем 1 аргумент и тд)
            user_step_y, user_step_x = input('Enter the coordinates: ').split()
            user_step_x = int(user_step_x) - 1  # эта строка и следующая для верного определения в списке
            user_step_y = int(user_step_y) - 1
        except ValueError:
            print('You should enter numbers!')
        else:

            if user_step_x > 2 or user_step_y > 2:
                print('Coordinates should be from 1 to 3!')
            elif board[user_step_y][user_step_x] == 'X' or board[user_step_y][user_step_x] == 'O':
                print('This cell is occupied! Choose another one!')
            elif board[user_step_y][user_step_x] == ' ' and count == 0:
                board[user_step_y][user_step_x] = 'X'
                count += 1
                new_board = ''
                for i in board:
                    for j in i:
                        new_board += j
                print_board(new_board)
                game = check_win(new_board)
            elif board[user_step_y][user_step_x] == ' ' and count == 1:
                board[user_step_y][user_step_x] = 'O'
                count -= 1
                new_board = ''
                for i in board:
                    for j in i:
                        new_board += j
                print_board(new_board)
                game = check_win(new_board)


game_board = '         '
print_board(game_board)
step(game_board)
