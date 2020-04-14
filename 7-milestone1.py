from IPython.display import clear_output
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board



def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    player1 = marker
    if player1 =='X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

def place_marker(player,board,position):
    if player == 'X':
        board[position] = 'X'
    else:
        board[position] = 'O' 

def win_check(player, board):
    if board[7]==player  and board[8] == player and board[9] == player:
        return True
    elif board[4]==player  and board[5] == player and board[6] == player:
        return True
    elif board[2]==player  and board[3] == player and board[3] == player:
        return True
    elif board[7]==player  and board[4] == player and board[1] == player:
        return True
    elif board[8]==player  and board[5] == player and board[2] == player:
        return True
    elif board[9]==player  and board[6] == player and board[3] == player:
        return True
    elif board[7]==player  and board[5] == player and board[3] == player:
        return True
    elif board[9]==player  and board[5] == player and board[1] == player:
        return True
    else:
        return False

def space_check(board,position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True


def full_board_check(board):
    
    pass


def player_choice(board):
    
    choice = int(input('Choose 1-9:'))
    while(not space_check(board,choice)):
        choice = int(input('Choose 1-9:'))
    return choice

def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')


while True:
    board = [' ']*10
    marker = player_input()
    player1 = marker[0]
    player2 = marker[1]
    turn = 'player1'
    gameOn = True

    print(player1)
    print(player2)
    #Players one's Turn

    while(gameOn):
        if(turn == 'player1'):
            display_board(board)
            position = player_choice(board)
            place_marker(player1, board, position)

            if(win_check(player1, board)):
                display_board(board)
                print('Congratulations! You have won the game!')
                gameOn = False
            else:
                turn = 'player2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(player2, board, position)

            if(win_check(player1, board)):
                display_board(board)
                print('Congratulations! You have won the game!')
                gameOn = False
            else:
                turn = 'player1'

    if not replay():
        break
