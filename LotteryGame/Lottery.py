import random


def create_board():
    board = [[], [], [], []]
    added_nums = []

    for row in board:
        for i in range(4):
            num = random.randint(1, 54)
            while num in added_nums:
                num = random.randint(1, 54)
            row.append(num)
            added_nums.append(num)

    return board


def print_board(board):
    s = ' '
    print('    1    2    3    4')
    print('    -----------------')
    print(
        f'1 | {board[0][0]}{(5 - len(str(board[0][0]))) * s}{board[0][1]}{(5 - len(str(board[0][1]))) * s}{board[0][2]}{(5 - len(str(board[0][2]))) * s}{board[0][3]}')
    print('  |')
    print(
        f'2 | {board[1][0]}{(5 - len(str(board[1][0]))) * s}{board[1][1]}{(5 - len(str(board[1][1]))) * s}{board[1][2]}{(5 - len(str(board[1][2]))) * s}{board[1][3]}')
    print('  |')
    print(
        f'3 | {board[2][0]}{(5 - len(str(board[2][0]))) * s}{board[2][1]}{(5 - len(str(board[2][1]))) * s}{board[2][2]}{(5 - len(str(board[2][2]))) * s}{board[2][3]}')
    print('  |')
    print(
        f'4 | {board[3][0]}{(5 - len(str(board[3][0]))) * s}{board[3][1]}{(5 - len(str(board[3][1]))) * s}{board[3][2]}{(5 - len(str(board[3][2]))) * s}{board[3][3]}')


def horizontal(player_board, computer_board):
    pulled_cards = []
    player_winner = False
    computer_winner = False

    for i in range(54):
        card = random.randint(1, 54)
        while card in pulled_cards:
            card = random.randint(1, 54)
        pulled_cards.append(card)
        print(card)

        for row in player_board:
            count = 0
            for element in row:
                if element in pulled_cards:
                    count += 1
            if count == 4:
                player_winner = True

        for row in computer_board:
            count = 0
            for element in row:
                if element in pulled_cards:
                    count += 1
            if count == 4:
                computer_winner = True

        if player_winner and computer_winner:
            print("It's a tie!")
            print('Your board:')
            print_board(player_board)
            print('My board:')
            print_board(computer_board)
        else:
            if player_winner:
                print('You won!!!')
                print('Your board:')
                print_board(player_board)
                print('My board:')
                print_board(computer_board)
                break
            elif computer_winner:
                print('I won!!! Good luck next time')
                print('Your board:')
                print_board(player_board)
                print('My board:')
                print_board(computer_board)
                break


def vertical(player_board, computer_board):
    pulled_cards = []
    player_winner = False
    computer_winner = False

    for i in range(54):
        card = random.randint(1, 54)
        while card in pulled_cards:
            card = random.randint(1, 54)
        pulled_cards.append(card)
        print(card)

        for i in range(4):
            player_count = 0
            for x in range(4):
                if player_board[x][i] in pulled_cards:
                    player_count += 1
                if player_count == 4:
                    player_winner = True

        for i in range(4):
            computer_count = 0
            for x in range(4):
                if computer_board[x][i] in pulled_cards:
                    computer_count += 1
                if computer_count == 4:
                    computer_winner = True

        if player_winner and computer_winner:
            print("It's a tie!")
            print('Your board:')
            print_board(player_board)
            print('My board:')
            print_board(computer_board)
        else:
            if player_winner:
                print('You won!!!')
                print('Your board:')
                print_board(player_board)
                print('My board:')
                print_board(computer_board)
                break
            elif computer_winner:
                print('I won!!! Good luck next time')
                print('Your board:')
                print_board(player_board)
                print('My board:')
                print_board(computer_board)
                break


def full_board(player_board, computer_board):
    pulled_cards = []
    player_winner = False
    computer_winner = False

    for i in range(54):
        card = random.randint(1, 54)
        while card in pulled_cards:
            card = random.randint(1, 54)
        pulled_cards.append(card)
        print(card)

        player_count = 0
        for row in player_board:
            for element in row:
                if element in pulled_cards:
                    player_count += 1
        if player_count == 16:
            player_winner = True

        computer_count = 0
        for row in computer_board:
            for element in row:
                if element in pulled_cards:
                    computer_count += 1
        if computer_count == 16:
            computer_winner = True

        if player_winner and computer_winner:
            print("It's a tie!")
            print_board(player_board)
            print_board(computer_board)
        else:
            if player_winner:
                print('You won!!!')
                print('Your board:')
                print_board(player_board)
                print('My board:')
                print_board(computer_board)
                break
            elif computer_winner:
                print('I won!!! Good luck next time')
                print('Your board:')
                print_board(player_board)
                print('My board:')
                print_board(computer_board)
                break


def main():
    player_board = create_board()
    computer_board = create_board()
    change_board = 'Y'
    while change_board == 'Y':
        player_board = create_board()
        print('Player board:')
        print('')
        print_board(player_board)
        change_board = input('Do you want to change your board? Y/N: ')
        while change_board != 'Y' and change_board != 'N':
            print('Input a valid character')
            change_board = input('Do you want to change your board? Y/N: ')
    print('Computer board:')
    print('')
    print_board(computer_board)

    game_mode = input('''
Select Game Mode
Horizontal: H
Vertical: V
Full board: F

Game mode: ''')

    while game_mode != 'H' and game_mode != 'V' and game_mode != 'F':
        print('Select a valid game mode')
        game_mode = input('''
Select Game Mode
Horizontal: H
Vertical: V
Full board: F

Game mode: ''')

    if game_mode == 'H':
        horizontal(player_board, computer_board)
    elif game_mode == 'V':
        vertical(player_board, computer_board)
    elif game_mode == 'F':
        full_board(player_board, computer_board)


if __name__ == '__main__':
    main()
            
            