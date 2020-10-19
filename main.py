from ai import AI
from utils import *
import sys

#sys.setrecursionlimit(4000)


def print_board(board):
    for i, row in enumerate(board):
        print(' | '.join(row))
        if i != 2:
            print('-'*9)

def ask_input(board):
    value = int(input("Please choose where you want to play: "))
    x = value // 3
    y = value - (value // 3)*3
    while board[x][y] in ['X', 'O']:
        value = int(input("Error! Not an empty space! Please choose where you want to play: "))
        x = value // 3
        y = value - (value // 3)*3

    return x, y

def main():
    board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
    running = True
    turn = 0

    ai = AI()

    while running:
        print_board(board)

        if len(availableMoves(board)) == 0:
            print("IT'S A TIE!")
            return

        if turn % 2 == 1:
            x, y = ask_input(board)
            board[x][y] = 'X'
            print(f"Player 1 chose {x*3 + y}!")

        else:
            x, y = ai.findBestMove(board)
            board[x][y] = 'O'
            print(f"The computer chose {x*3 + y}!")

        winner = checkWin(board)
        if winner:
            print_board(board)
            print(f"The winner is: {winner}")
            return

        turn += 1

if __name__=="__main__":
    main()