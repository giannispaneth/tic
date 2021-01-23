import time
import os
import sys
import f3pieces
import random


def evaluatefigures(grid, color):
    points = 0

    kp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    rp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if color == 'W':
        color2 = 'B'
    else:
        color2 = 'W'

    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if grid[i][j] == ('R', color):
                points = points + rp[i][j]
            if grid[i][j] == ('K', color):
                points = points + kp[i][j]
            if grid[i][j] == ('B', color):
                points = points + bp[i][j]
            if grid[i][j] == ('R', color2):
                points = points - rp[i][j]
            if grid[i][j] == ('K', color2):
                points = points - kp[i][j]
            if grid[i][j] == ('B', color2):
                points = points - bp[i][j]
    return points


def iswinning(grid, color):

    i = 0
    j = 0
    k = 0
    l = 0
    for x in [0, 1, 2]:

        if grid[x][x][1] == color:
            k = k+1
            if k == 3:
                return True
        else:
            k = 0

        if grid[2-x][x][1] == color:
            l = l+1
            if l == 3:
                return True
        else:
            l = 0
        for y in [0, 1, 2]:

            if grid[x][y][1] == color:
                i = i+1
                if i == 3:
                    return True
            else:
                i = 0
            if grid[y][x][1] == color:
                j = j+1
                if j == 3:
                    return True
            else:
                j = 0
        i = 0
        j = 0
    return False


def rowevalcoleval(grid, color, z):
    points = 0
    for x in range(0, 3, 1):
        k = 0
        l = 0
        for y in range(0, 3, 1):
            if z == True:
                i = x
                j = y
            else:
                i = y
                j = x
            if grid[i][j][1] == color:
                l = l+1
            elif grid[i][j][1] != color and grid[i][j][1] != "_":
                k = k+1
        if l == 2:
            points = points+3
        if l == 3:
            points = points+100

        if k == 2:
            points = points-3
        if k == 3:
            points = points-100

    return points


def diageval(grid, color, z):
    points = 0
    k = 0
    l = 0
    if z == 0:
        r = 1
    else:
        r = -1
    for i, j in zip([0, 1, 2], [z+0*r, z+1*r, z+2*r]):
        if grid[i][j][1] == color:
            l = l+1
        elif grid[i][j][1] != color and grid[i][j][1] != "_":
            k = k+1
    if l == 2:
        points = points+3
    if l == 3:
        points = points+100

    if k == 2:
        points = points-3
    if k == 3:
        points = points-100

    return points


def evaluateboard(grid, color):
    points = 0
    a = rowevalcoleval(grid, color, z=True)
    points = points+a
    a = rowevalcoleval(grid, color, z=False)
    points = points+a
    a = diageval(grid, color, 2)
    points = points+a
    a = diageval(grid, color, 0)
    points = points+a
    a = evaluatefigures(grid, color)
    points = points+a
    return points


def notinboardmoves(kind, color, grid):
    k = 0

    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if grid[i][j] == (kind, color):
                k = 1
    if k == 0:
        moves = []

        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if grid[i][j] == ('_', '_'):
                    moves.append([i, j])
        return moves
    else:
        moves = []
        return moves


P = [[("K", "B"), ("B", "B"), ("R", "B")], [
    ("K", "W"), ("B", "W"), ("R", "W")]]
grid = [[("_", "_")]*3 for n in range(3)]


grid1 = [[(350, 250), (450, 250), (550, 250), (650, 250)], [(350, 350), (450, 350), (550, 350), (650, 350)], [
    (350, 450), (450, 450), (550, 450), (650, 450)], [(350, 550), (450, 550), (550, 550), (650, 550)]]


def printg(grid):
    print('                 ')
    for i in range(0, 3, 1):
        print(grid[i])


def getpawnpos(grid, kind, color):
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if grid[i][j] == (kind, color):
                return i, j


def allpossiblemoves(color, grid):
    a = [0, 0, 0]
    a[0] = notinboardmoves('R', color, grid)

    a[1] = notinboardmoves('K', color, grid)
    a[2] = notinboardmoves('B', color, grid)
    if a[0] == []:
        c, b = getpawnpos(grid, 'R', color)
        a[0] = f3pieces.rook(c, b, color).validmoves(grid)

    if a[1] == []:
        c, b = getpawnpos(grid, 'K', color)
        a[1] = f3pieces.knight(c, b, color).validmoves(grid)
    if a[2] == []:
        c, b = getpawnpos(grid, 'B', color)
        a[2] = f3pieces.bishop(c, b, color).validmoves(grid)
    return a


winning = 'yes'

while winning == 'no':
    if l == 'B':
        l = 'W'
    else:
        l = 'B'
    x, y, z = input("x,y,kind ").split()
    grid[x, y] = (kind, l)
    winning = input('say if over')


def updategrid(grid, x, y, kind, color):

    q = [[1] * 3 for n in range(3)]
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            q[i][j] = grid[i][j]
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if q[i][j] == (kind, color):
                q[i][j] = ('_', '_')
    q[x][y] = (kind, color)

    return q


def bestmove2(grid, depth, color, color2, alpha, beta, col):
    if color2 == 'W':
        Col = 'B'
    else:
        Col = 'W'
    maxing = -100000

    ar = allpossiblemoves(color2, grid)
    s = [0, 1, 2]
    random.shuffle(s)
    o = 0
    for i in s:

        for posmoves in ar[i]:
            if posmoves != []:
                o = o+1
            if i == 0:
                y = 'R'

            if i == 1:
                y = 'K'

            if i == 2:
                y = 'B'

            q = updategrid(grid, posmoves[0], posmoves[1], y, color2)
            if iswinning(q, color2):
                return posmoves[0], posmoves[1], y, color2

            if o == 1:

                eval = -negamax(q, depth-1, -color, Col, -beta, -alpha, col)
            else:
                eval = -negamax(q, depth-1, -color, Col, -alpha-1, -alpha, col)
                if alpha < eval and eval < beta:
                    eval = -negamax(q, depth-1, -color, Col, -beta, -eval, col)
            if eval > maxing:
                maxing = eval
                bestmoves1 = posmoves[0]
                bestmoves2 = posmoves[1]
                bestmoves3 = y

            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        if beta <= alpha:
            break
    return bestmoves1, bestmoves2, bestmoves3, color2


def negamax(grid, depth, color, color2, alpha, beta, col):
    if color2 == 'W':
        Col = 'B'
    else:
        Col = 'W'
    if depth == 0:

        req = evaluateboard(grid, col)
        return req * color
    if iswinning(grid, Col):
        req = evaluateboard(grid, col)
        return req * color
    if iswinning(grid, color2):
        req = evaluateboard(grid, col)
        return req * color
    ar = allpossiblemoves(color2, grid)
    s = [0, 1, 2]
    random.shuffle(s)
    o = 0
    for i in s:

        for posmoves in ar[i]:
            if posmoves != []:
                o = o+1
            if i == 0:
                y = 'R'

            if i == 1:
                y = 'K'

            if i == 2:
                y = 'B'

            q = updategrid(grid, posmoves[0], posmoves[1], y, color2)

            if o == 1:

                eval = -negamax(q, depth-1, -color, Col, -beta, -alpha, col)
            else:
                eval = -negamax(q, depth-1, -color, Col, -alpha-1, -alpha, col)
                if alpha < eval and eval < beta:
                    eval = -negamax(q, depth-1, -color, Col, -beta, -eval, col)
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        if alpha >= beta:
            break
    return alpha


def negamax2(grid, depth, color, color2):

    alpha = -100000
    if color == 1 and color2 == 'W':
        Col = 'B'
    elif color == -1 and color2 == 'B':
        Col = 'B'

    else:
        Col = 'W'
    if Col == 'W':
        Col2 = 'B'
    else:
        Col2 = 'W'

    if depth == 0:

        req = evaluateboard(grid, color2)
        return req * -color
    if iswinning(grid, Col):
        req = evaluateboard(grid, color2)
        return req * -color
    if iswinning(grid, Col2):
        req = evaluateboard(grid, color2)
        return req * color
    ar = allpossiblemoves(color2, grid)
    s = [0, 1, 2]
    random.shuffle(s)
    o = 0
    for i in s:

        for posmoves in ar[i]:
            if posmoves != []:
                o = o+1
            if i == 0:
                y = 'R'

            if i == 1:
                y = 'K'

            if i == 2:
                y = 'B'

            q = updategrid(grid, posmoves[0], posmoves[1], y, Col2)

            eval = -negamax2(q, depth-1, -color, Col)
            alpha = max(alpha, eval)
    return alpha


def bestmove3(grid, depth, color, color2):

    alpha = -1000000

    ar = allpossiblemoves(color2, grid)
    s = [0, 1, 2]
    random.shuffle(s)
    o = 0
    for i in s:

        for posmoves in ar[i]:
            if posmoves != []:
                o = o+1
            if i == 0:
                y = 'R'

            if i == 1:
                y = 'K'

            if i == 2:
                y = 'B'

            q = updategrid(grid, posmoves[0], posmoves[1], y, color2)
            if iswinning(grid, color2):
                bestmoves1 = posmoves[0]
                bestmoves2 = posmoves[1]
                bestmoves3 = y

                return bestmoves1, bestmoves2, bestmoves3, color
            eval = -negamax2(q, depth-1, -color, color2)
            if eval > alpha:
                bestmoves1 = posmoves[0]
                bestmoves2 = posmoves[1]
                bestmoves3 = y

            alpha = max(alpha, eval)

    return bestmoves1, bestmoves2, bestmoves3, color2


def minimax(grid, depth, color, alpha, beta, maximazingplayer):

    if depth == 0:

        req = evaluateboard(grid, color)

        return req

    if color == 'W':
        color2 = 'B'
    else:
        color2 = 'W'

    if iswinning(grid, color):
        req = evaluateboard(grid, color)

        return req
    if iswinning(grid, color2):
        req = evaluateboard(grid, color)

        return req

    if maximazingplayer:
        maxing = -10000
        ar = allpossiblemoves(color, grid)
        s = [0, 1, 2]
        random.shuffle(s)
        for i in s:
            for posmoves in ar[i]:

                if i == 0:
                    y = 'R'

                if i == 1:
                    y = 'K'

                if i == 2:
                    y = 'B'
                q = updategrid(grid, posmoves[0], posmoves[1], y, color)

                eval = minimax(q, depth-1, color, alpha, beta, False)

                maxing = max(maxing, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:

                    break

            if beta <= alpha:
                break
        return maxing
    else:
        mining = 10000
        ar = allpossiblemoves(color2, grid)
        s = [0, 1, 2]
        random.shuffle(s)
        for i in s:
            for posmoves in ar[i]:
                if i == 0:

                    y = 'R'

                if i == 1:
                    y = 'K'

                if i == 2:
                    y = 'B'

                q = updategrid(grid, posmoves[0], posmoves[1], y, color2)

                eval = minimax(q, depth - 1, color, alpha, beta, True)
                mining = min(mining, eval)
                beta = min(beta, eval)
                if beta <= alpha:

                    break

            if beta <= alpha:
                break
        return mining


def bestmove(grid, depth, color, alpha, beta):

    maxing = -10000
    ar = allpossiblemoves(color, grid)
    s = [0, 1, 2]
    random.shuffle(s)
    for i in s:
        for posmoves in ar[i]:

            if i == 0:
                y = 'R'

            if i == 1:
                y = 'K'

            if i == 2:
                y = 'B'

            q = updategrid(grid, posmoves[0], posmoves[1], y, color)
            if iswinning(q, color):
                return posmoves[0], posmoves[1], y, color
            eval = minimax(q, depth-1, color, alpha, beta, False)

            if eval > maxing:
                maxing = eval
                bestmoves1 = posmoves[0]
                bestmoves2 = posmoves[1]
                bestmoves3 = y

            alpha = max(alpha, eval)
            if beta <= alpha:

                break
        if beta <= alpha:
            break
    return bestmoves1, bestmoves2, bestmoves3, color


# spot = time.time()
# print((time.time()-spot))
grid[0][0] = ('_', '_')
grid[2][0] = ('_', '_')
grid[1][2] = ('_', '_')
grid[2][1] = ('_', '_')

sp2 = bestmove(grid, 3, 'B', -10000, 10000)
print(sp2)
sp3 = minimax(grid, 3, 'B', -100000, 100000, True)
sp = negamax(grid, 3, 1, 'B', - 100000, 100000, 'B')
print(sp, sp3)
ase = evaluateboard(grid, 'W')
are = allpossiblemoves('B', grid)
ame = bestmove2(grid, 3, 1, 'W', -100000, 100000, 'W')
print(ame)

notend = False
notend2 = False
notend3 = True
i = 1
while(notend):
    if (i % 2) != 0:

        a = bestmove(grid, 2, 'W', -10000, 10000)
        grid = updategrid(grid, a[0], a[1], a[2], a[3])
        printg(grid)
        i = i+1
        if iswinning(grid, 'W'):
            notend = False
    else:
        a = bestmove(grid, 5, 'B', -10000, 10000)
        k1 = (a[2], a[3])
        grid = updategrid(grid, a[0], a[1], a[2], a[3])
        printg(grid)
        i = i+1
        if iswinning(grid, 'B'):
            notend = False
while(notend2):
    if (i % 2) != 0:

        a = bestmove2(grid, 2, 1, 'W', -100000, 100000, 'W')
        grid = updategrid(grid, a[0], a[1], a[2], a[3])
        printg(grid)
        i = i+1
        if iswinning(grid, 'W'):
            notend2 = False
    else:
        a = bestmove2(grid, 4, 1, 'B', -100000, 100000, 'B')
        k1 = (a[2], a[3])
        grid = updategrid(grid, a[0], a[1], a[2], a[3])
        printg(grid)
        i = i+1
        if iswinning(grid, 'B'):
            notend2 = False
while(notend3):
    if (i % 2) != 0:

        a = bestmove3(grid, 2, 1, 'W')
        grid = updategrid(grid, a[0], a[1], a[2], a[3])
        printg(grid)
        i = i+1
        if iswinning(grid, 'W'):
            notend3 = False
    else:
        a = bestmove3(grid, 4, 1, 'B')
        k1 = (a[2], a[3])
        grid = updategrid(grid, a[0], a[1], a[2], a[3])
        printg(grid)
        i = i+1
        if iswinning(grid, 'B'):
            notend3 = False
