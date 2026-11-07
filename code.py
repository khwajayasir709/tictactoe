print("Welcome to Tic Tac Toe Game!")

import random

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

while True:
    board = [' ' for _ in range(9)]
    player = 'X'
    computer = 'O'
    game_over = False

    while not game_over:
        print_board(board)
        if player == 'X':
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                if (board[0] == board[1] == board[2] != ' ') or \
                   (board[3] == board[4] == board[5] != ' ') or \
                   (board[6] == board[7] == board[8] != ' ') or \
                   (board[0] == board[3] == board[6] != ' ') or \
                   (board[1] == board[4] == board[7] != ' ') or \
                   (board[2] == board[5] == board[8] != ' ') or \
                   (board[0] == board[4] == board[8] != ' ') or \
                   (board[2] == board[4] == board[6] != ' '):
                    print_board(board)
                    print("Congratulations! You win!")
                    game_over = True 
                    break

                elif computer == 'O':
                            move = random.randint(0, 8)
                            while board[move] != ' ':
                                move = random.randint(0, 8)
                            board[move] = computer
                            if (board[0] == board[1] == board[2] != ' ') or \
                               (board[3] == board[4] == board[5] != ' ') or \
                               (board[6] == board[7] == board[8] != ' ')    or \
                               (board[0] == board[3] == board[6] != ' ') or \
                               (board[1] == board[4] == board[7] != ' ') or \
                               (board[2] == board[5] == board[8] != ' ') or \
                               (board[0] == board[4] == board[8] != ' ') or \
                               (board[2] == board[4] == board[6] != ' ' ):
                                print_board(board)
                                print("Computer wins! Better luck next time.")
                                game_over = True
                                break
    else:
        print_board(board)
        print("It's a tie!")
        game_over = True

                                
                                    