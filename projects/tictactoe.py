import numpy as np
import pickle
import math

board = [' ' for x in range(10)]

def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def insert_letter(letter, pos):
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))

def player_move():
    run = True
    while run:
        move = input("Please enter a postion:")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print ("Invalid")
            else:
                print("Number in range")
        except Exception as e:
            print(e)

def comp_move(board, depth, max_player):
    if max_player == True:
        bestVal = -math.inf
        for value in board[1:]:
            if value == ' ':
                value = 'O'
                check_move = max(bestVal, comp_move(board, depth+1 , False))
                value = ' '
        return bestVal
    else:
        bestVal = math.inf
        for value in board[1:]:
            if value == ' ':
                player = 'X'
                print(depth)
                check_move = min(bestVal, comp_move(board, depth+1 , True))
                value = ' '
        return bestVal



def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
def main():
    print_board(board)
    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('Sorry, O\'s won this time!')
            break
        if not(is_winner(board, 'X')):
            move = comp_move(board, 0, True)
            if move == 0:
                print('Tie Game!')
            else:
                insert_letter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                print_board(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if is_board_full(board):
        print('Tie Game!')
main()

