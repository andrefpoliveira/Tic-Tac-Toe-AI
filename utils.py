def checkWin(board):
    # Check Lines
    for i in board:
        for j in ['X', 'O']:
            if i.count(j) == 3:
                return j

    # Check Cols
    for i in range(3):
        col = []
        for j in board:
            col.append(j[i])

        for j in ['X', 'O']:
            if col.count(j) == 3:
                return j

    dia = []
    neg_dia = []
    # Check Diagonals
    for i in range(3):
        dia.append(board[i][i])
        neg_dia.append(board[i][2-i])

    for j in ['X', 'O']:
            if dia.count(j) == 3 or neg_dia.count(j) == 3:
                return j

    return None

def availableMoves(board):
        return [i for sublist in board for i in sublist if i not in ['X', 'O']]