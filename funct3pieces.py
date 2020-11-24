import os
import sys
import game
import random

def evaluatefigures(grid,color):
    points=0
    
    kp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    rp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    bp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if color == 'W':
        color2='B'
    else:
        color2='W'

    for i in [0,1,2]:
        for j in [0,1,2]:
            if grid[i][j]==('R',color):
                points = points + rp[i][j]
            if grid[i][j]==('K',color):
                points = points + kp[i][j]
            if grid[i][j]==('B',color):
                points = points + bp[i][j]
            if grid[i][j]==('R',color2) :
                points = points - rp[i][j]
            if grid[i][j]==('K',color2) :
                points = points - kp[i][j]
            if grid[i][j]==('B',color2) :
                points = points - bp[i][j]
    return points

def iswinning(grid,color):
    a=False
    i=0
    j=0
    k=0
    l=0
    for x in [0,1,2]:
        5
        
        if grid[x][x][1]==color:
                k=k+1
                if k==3 :
                    return True
        else
                k = 0
                
        if grid[2-x][x][1]==color:
                l=l+1
                if l==3 :
                    return True
        else
                l = 0
        for y in [0,1,2]:
            
            if grid[x][y][1]==color:
                i=i+1
                if i==3 :
                    return True
            else
                i = 0
            if grid[y][x][1]==color:
                j=j+1
                if j==3: 
                    return True
            else 
                j=0
        i=0
        j=0
    returnt False

def rowevalcoleval(grid,color,z):
    points=0
    for x in range(0,3,1):
        k=0
        l=0
        for y in range(0,3,1):
            if z==True:
                i=x
                j=y
            else:
                i=y
                j=x
            if grid[i][j][1]==color:
                l=l+1
            elif grid[i][j][1]!=color and grid[i][j][1]!="_":
                k=k+1
        if l==2 :
            points=points+2
        if l==3 :
            points=points+ 100
       
        if k == 2:
            points = points - 3
        if k == 3:
            points = points -100
        
    return points
def diageval(grid,color,z):
    points=0
    k = 0
    l = 0
    for i,j in zip([0,1,2],[z-0,z-1,z-2]):
            if grid[i][j][1]==color:
                l=l+1
            elif grid[i][j][1]!=color and grid[i][j][1]!="_":
                k=k+1
    if l==2 :
            points=points+2
    if l==3 :
            points=points+100

    if k == 2:
            points = points - 3
    if k == 3:
            points = points -100
    
    return points
def evaluateboard(grid,color):
    points=0
    a=rowevalcoleval(grid,color,z=True)
    points=points+a
    a=rowevalcoleval(grid,color,z=False)
    points=points+a
    a=diageval(grid,color,2)
    points=points+a
    a=diageval(grid,color,0)
    points=points+a
    a=evaluatefigures(grid,color)
    points=points+a
    return points

def notinboardmoves(kind,color,grid):
    k=0

    for i in range(0,3,1):
        for j in range(0,3,1):
            if grid[i][j]==(kind,color):
                k=1
    if k==0:
        moves=[]

        for i in range(0,3,1):
            for j in range(0,3,1):
                if grid[i][j]==('_','_'):
                    moves.append([i,j])
        return moves
    else:
        moves=[]
        return moves


P=[[("K","B"),("B","B"),("R","B")],[("K","W"),("B","W"),("R","W")]]
grid=[[("_","_")]*3 for n in range(3)]



grid1=[[(350,250),(450,250),(550,250),(650,250)],[(350,350),(450,350),(550,350),(650,350)],[(350,450),(450,450),(550,450),(650,450)],[(350,550),(450,550),(550,550),(650,550)]]



def printg(grid):
    print('                 ')
    for i in range(0, 3, 1):
        print(grid[i])


def getpawnpos(grid,kind,color):
    for i in [0,1,2]:
        for j in [0,1,2]:
            if grid[i][j]==(kind,color):
                return i,j

def allpossiblemoves(color,grid):
    a=[0,0,0]
    a[0]=notinboardmoves('R',color,grid)
    
    a[1]=notinboardmoves('K',color,grid)
    a[2]=notinboardmoves('B',color,grid)
    if a[0]==[]:
        c,b=getpawnpos(grid,'R',color)
        a[0]=game.rook(c,b,color).validmoves(grid)
    
    if a[1] == []:
        c, b = getpawnpos(grid,'K', color)
        a[1] = game.knight(c,b,color).validmoves(grid)
    if a[2] == []:
        c, b = getpawnpos(grid,'B', color)
        a[2] = game.bishop(c,b,color).validmoves(grid)
    return a





winning='yes'

while winning=='no':
    if l=='B':
        l='W'
    else:
        l='B'
    x, y, z = input("x,y,kind ").split()
    grid[x,y]=(kind,l)
    winning = input('say if over')





def updategrid(grid,x,y,kind,color):

    q = [[1] * 3 for n in range(3)]
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            q[i][j] = grid[i][j]
    for i in [0,1,2]:
        for j in [0,1,2]:
            if q[i][j]==(kind,color):
                q[i][j]=('_','_')
    q[x][y]=(kind,color)


    return q


def minimax(grid,depth,color,alpha,beta,maximazingplayer):
    if depth == 0 :
        req=evaluateboard(grid,color)

        return req

        print()
    if color == 'W':
        color2='B'
    else:
        color2='W'
    if iswinning(grid,color2)
    if maximazingplayer:
        maxing=-10000
        ar=allpossiblemoves(color,grid)

        for i in [0,1,2]:
            for posmoves in ar[i]:

                if i==0:
                    y='R'
                    q=updategrid(grid,posmoves[0],posmoves[1],y,color)

                    eval=minimax(q,depth-1,color,alpha,beta,False)

                    maxing = max(maxing, eval)
                    alpha = max(alpha, eval)


            
                if i==1:
                    y='K'
                    q=updategrid(grid,posmoves[0],posmoves[1],y,color)
                    eval=minimax(q,depth-1,color,alpha,beta,False)
                    maxing = max(maxing, eval)
                    alpha = max(alpha, eval)

                if i==2:
                    y='B'
                    q=updategrid(grid,posmoves[0],posmoves[1],y,color)
                    eval=minimax(q,depth-1,color,alpha,beta,False)
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
        for i in [0, 1, 2]:
            for posmoves in ar[i]:
                if i == 0:
                    y = 'R'
                    q = updategrid(grid, posmoves[0], posmoves[1], y, color2)
                    eval = minimax(q, depth - 1, color,alpha,beta, True)
                    mining = min(mining, eval)
                    beta = min(beta, eval)

               

                if i == 1:
                    y = 'K'
                    q = updategrid(grid, posmoves[0], posmoves[1], y, color2)
                    eval = minimax(q, depth - 1, color,alpha,beta, True)
                    mining = min(mining, eval)
                    beta = min(beta, eval)

                if i == 2:
                    y = 'B'
                    q = updategrid(grid, posmoves[0], posmoves[1], y, color2)
                    eval = minimax(q, depth - 1, color,alpha,beta, True)
                    mining = min(mining, eval)
                    beta = min(beta, eval)
                if beta <= alpha:
                    break
            if beta <= alpha:
                break
        return mining
def bestmove(grid,depth,color,alpha,beta):


        maxing=-10000
        ar=allpossiblemoves(color,grid)

        for i in [0,1,2]:
            for posmoves in ar[i]:

                if i==0:
                    y='R'
                    q=updategrid(grid,posmoves[0],posmoves[1],y,color)

                    eval=minimax(q,depth-1,color,alpha,beta,False)

                    if eval >= maxing:
                        maxing = eval
                        bestmoves1 = posmoves[0]
                        bestmoves2 = posmoves[1]
                        bestmoves3 = y
                    alpha = max(alpha, eval)

                    
                if i==1:
                    y='K'
                    q=updategrid(grid,posmoves[0],posmoves[1],y,color)
                    eval=minimax(q,depth-1,color,alpha,beta,False)
                    if eval >= maxing:
                        maxing = eval
                        bestmoves1 = posmoves[0]
                        bestmoves2 = posmoves[1]
                        bestmoves3 = y
                    alpha = max(alpha, eval)

                if i==2:
                    y='B'
                    q=updategrid(grid,posmoves[0],posmoves[1],y,color)
                    eval=minimax(q,depth-1,color,alpha,beta,False)
                    if eval>=maxing:
                        maxing=eval
                        bestmoves1=posmoves[0]
                        bestmoves2=posmoves[1]
                        bestmoves3=y
                    alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            if beta <= alpha:
                break
        return bestmoves1,bestmoves2,bestmoves3,color



import time
#spot = time.time()
#print((time.time()-spot))
grid[1][2]=('R','W')
grid[0][1]=('K','B')
grid[1][1]=('B','B')
sp=bestmove(grid, 3, 'B', -10000, 10000)
print(sp)
al=minimax(grid,3,'B',-10000,10000,True)

ase=evaluateboard(grid,'B')


notend=False
i=1
while(notend):
    if (i % 2)!=0:
        a=[0,0,0,0]
        a=input("enter valid move").split()
        print(a)
        a[0]=int(a[0])
        a[1]=int(a[1])
        print(a)
        k2=(a[2],a[3])
        grid[a[0]][a[1]]=k2
        printg(grid)
        i=i+1
    else:
        a = bestmove(grid, 4, 'B', -10000, 10000)
        k1=(a[2],a[3])
        grid[a[0]][a[1]]=k1
        printg(grid)
        i=i+1
