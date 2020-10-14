from utils import *

class AI:
    def findBestMove(self, board):
        bestX = None
        bestY = None
        bestVal = -float("Inf")
        for move in availableMoves(board):
            x = int(move) // 3
            y = int(move) - (int(move) // 3)*3

            board[x][y] = 'O'

            moveVal = self.minimax(board, 0, False)

            board[x][y] = move

            if moveVal > bestVal:
                bestX = x
                bestY = y
                bestVal = moveVal

        return bestX, bestY

    def isMovesLeft(self, board):
        return len(availableMoves(board)) > 0

    def minimax(self, board, depth, isMaximizingPlayer):
        if checkWin(board) == 'X':
            #print("Perdi")
            return -10
        elif checkWin(board) == 'O':
            #print("Ganhei")
            return 10

        if len(availableMoves(board)) == 0:
            return 0

        if isMaximizingPlayer:
            bestVal = -float("Inf")
            for move in availableMoves(board):
                x = int(move) // 3
                y = int(move) - (int(move) // 3)*3
                board[x][y] = 'O'
                value = self.minimax(board, depth+1, not isMaximizingPlayer)
                board[x][y] = move
                bestVal = max(bestVal, value)
            return bestVal
        else:
            bestVal = float("Inf")
            for move in availableMoves(board):
                x = int(move) // 3
                y = int(move) - (int(move) // 3)*3
                board[x][y] = 'X'
                value = self.minimax(board, depth+1, not isMaximizingPlayer)
                board[x][y] = move
                bestVal = min(bestVal, value)
            return bestVal