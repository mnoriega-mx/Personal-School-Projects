import random


def create_answer_board():
    added_nums = []
    board = []
    for i in range(6):
        row = []
        for r in range(6):
            num = random.randint(1, 18)
            while added_nums.count(num) == 2:
                num = random.randint(1, 18)
            row.append(num)
            added_nums.append(num)
        board.append(row)
    return board


def create_player_board():
    board = []
    for i in range(6):
        row = []
        for r in range(6):
            row.append('*')
        board.append(row)
    return board


def print_board(board):
    s = ' '
    print('    1    2    3    4    5    6')
    print('    ---------------------------')
    print(
        f'1 | {board[0][0]}{(5 - len(str(board[0][0]))) * s}{board[0][1]}{(5 - len(str(board[0][1]))) * s}{board[0][2]}{(5 - len(str(board[0][2]))) * s}{board[0][3]}{(5 - len(str(board[0][3]))) * s}{board[0][4]}{(5 - len(str(board[0][4]))) * s}{board[0][5]}')
    print('  |')
    print(
        f'2 | {board[1][0]}{(5 - len(str(board[1][0]))) * s}{board[1][1]}{(5 - len(str(board[1][1]))) * s}{board[1][2]}{(5 - len(str(board[1][2]))) * s}{board[1][3]}{(5 - len(str(board[1][3]))) * s}{board[1][4]}{(5 - len(str(board[1][4]))) * s}{board[1][5]}')
    print('  |')
    print(
        f'3 | {board[2][0]}{(5 - len(str(board[2][0]))) * s}{board[2][1]}{(5 - len(str(board[2][1]))) * s}{board[2][2]}{(5 - len(str(board[2][2]))) * s}{board[2][3]}{(5 - len(str(board[2][3]))) * s}{board[2][4]}{(5 - len(str(board[2][4]))) * s}{board[2][5]}')
    print('  |')
    print(
        f'4 | {board[3][0]}{(5 - len(str(board[3][0]))) * s}{board[3][1]}{(5 - len(str(board[3][1]))) * s}{board[3][2]}{(5 - len(str(board[3][2]))) * s}{board[3][3]}{(5 - len(str(board[3][3]))) * s}{board[3][4]}{(5 - len(str(board[3][4]))) * s}{board[3][5]}')
    print('  |')
    print(
        f'5 | {board[4][0]}{(5 - len(str(board[4][0]))) * s}{board[4][1]}{(5 - len(str(board[4][1]))) * s}{board[4][2]}{(5 - len(str(board[4][2]))) * s}{board[4][3]}{(5 - len(str(board[4][3]))) * s}{board[4][4]}{(5 - len(str(board[4][4]))) * s}{board[4][5]}')
    print('  |')
    print(
        f'6 | {board[5][0]}{(5 - len(str(board[5][0]))) * s}{board[5][1]}{(5 - len(str(board[5][1]))) * s}{board[5][2]}{(5 - len(str(board[5][2]))) * s}{board[5][3]}{(5 - len(str(board[5][3]))) * s}{board[5][4]}{(5 - len(str(board[5][4]))) * s}{board[5][5]}')


def uncover_card(col, row, player_board, answer_board):
    player_board[row - 1][col - 1] = answer_board[row - 1][col - 1]


def cover_card(col, row, board):
    board[row - 1][col - 1] = '*'


def correct_pair(col1, row1, col2, row2, board):
    if board[row1 - 1][col1 - 1] == board[row2 - 1][col2 - 1]:
        return True
    else:
        return False


def change_turn(turn):
    if turn == 1:
        turn = 2
    else:
        turn = 1
    return turn


def main():
    answer_board = create_answer_board()
    player_board = create_player_board()

    continue_playing = True

    turn = 1

    points_p1 = 0
    points_p2 = 0

    while continue_playing:

        print_board(answer_board)
        print('''

        ''')
        print_board(player_board)

        print(f''''


Player {turn}'s turn
Choose a card!

        ''')
        column_card_1 = int(input('Column: '))
        row_card_1 = int(input('Row: '))
        while (column_card_1 < 1 or column_card_1 > 6) or (row_card_1 < 1 or row_card_1 > 6):
            print('Input valid numbers')
            column_card_1 = int(input('Column: '))
            row_card_1 = int(input('Row: '))
        while player_board[row_card_1 - 1][column_card_1 - 1] != '*':
            print('That card has already been uncovered, choose a new card')
            column_card_1 = int(input('Column: '))
            row_card_1 = int(input('Row: '))

        uncover_card(column_card_1, row_card_1, player_board, answer_board)

        print_board(player_board)

        print('''

        Choose a new card!

        ''')
        column_card_2 = int(input('Column: '))
        row_card_2 = int(input('Row: '))
        while (column_card_2 < 1 or column_card_2 > 6) or (row_card_2 < 1 or row_card_2 > 6):
            print('Input valid numbers')
            column_card_2 = int(input('Column: '))
            row_card_2 = int(input('Row: '))
        while column_card_1 == column_card_2 and row_card_1 == row_card_2:
            print('You have already chosen that card, choose a new card')
            column_card_2 = int(input('Column: '))
            row_card_2 = int(input('Row: '))
        while player_board[row_card_2 - 1][column_card_2 - 1] != '*':
            print('That card has already been uncovered, choose a new card')
            column_card_2 = int(input('Column: '))
            row_card_2 = int(input('Row: '))

        uncover_card(column_card_2, row_card_2, player_board, answer_board)
        print('''

        ''')
        print_board(player_board)

        if correct_pair(column_card_1, row_card_1, column_card_2, row_card_2, answer_board):
            print('''

            Correct!!
            ''')
            if turn == 1:
                points_p1 += 1
            else:
                points_p2 += 1
        else:
            print('Good luck next time')
            cover_card(column_card_1, row_card_1, player_board)
            cover_card(column_card_2, row_card_2, player_board)
            turn = change_turn(turn)

        if points_p1 > points_p2:
            winner = 'Player 1'
        elif points_p2 > points_p1:
            winner = 'Player 2'
        else:
            winner = 'tie'

        if points_p1 + points_p2 == 18:
            continue_playing = False

            if winner == 'tie':
                print(f''''

Game ended!!!

Total Points
Player 1: {points_p1}
Player 2: {points_p2}
It's a tie!

                ''')
            else:
                print(f''''

Game Ended!!!

Total Points
Player 1: {points_p1}
Player 2: {points_p2}
{winner} is the winner!

                ''')
        if continue_playing:
            continue_ = input('Do you want to continue playing? Y/N: ')
            while continue_ != 'Y' and continue_ != 'N':
                print('Inout a valid character')
                continue_ = input('Do you want to continue playing? Y/N: ')
            if continue_ == 'N':
                print(f'''

Game Ended!!!

Total Points
Player 1: {points_p1}
Player 2: {points_p2}
{winner} is the winner!

                ''')
                continue_playing = False


if __name__ == '__main__':
    main()

