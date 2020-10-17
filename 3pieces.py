def notinboardmoves(kind,color,grid):
    
    for i in range(0,3,1):
        for j in range(0,3,1):
            if grid[i][j]==(kind,color):
                k=1
    if k==1:
        moves=[]

        for i in range(0,3,1):
            for j in range(0,3,1):
                if grid[i][j]=='_':
                    moves.append([i,j])
        return moves
    else:
        moves=[]
        return moves

class pawn:
    def __init__(self, row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.kind = 'P'

    def validmoves(self,grid):
        i = self.row
        j = self.col
        k=1
        moves = []
        a,b=i,j
        a=a-k
        if inreach(a,b,grid,i,j) and grid[a][b]=='_':
            moves.append([a,b])
        b=b+1
        if  inreach(a,b,grid,i,j) and grid[a][b]!='_':
            moves.append([a,b])
        b=b-2
        if  inreach(a,b,grid,i,j) and grid[a][b]!='_':
            moves.append([a,b])

        return moves
class rook:
    def __init__(self, row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.kind = 'R'

    def validmoves(self,grid):
        i = self.row
        j = self.col

        moves = []
        for a in range(i,3,1):
            if grid[a][j][1] == self.color and a!=i:
                break
            elif grid[a][j][1] != '_' and a!=i:
                moves.append([a,j])
                break
            if inreach(a,j,grid,i,j) and a!=i :

                moves.append([a,j])
        for a in range(i,-1,-1):

            if grid[a][j][1]==self.color and a!=i:
                break
            elif grid[a][j][1] != '_' and a!=i:
                moves.append([a,j])
                break
            if inreach(a,j,grid,i,j) and a!=i :
                moves.append([a,j])
        for b in range(j,3,1):
            if grid[i][b][1] == self.color and b!=j:
                break
            elif grid[i][b][1] != '_' and b!=j:
                moves.append([i,b])
                break
            if inreach(i,b,grid,i,j) and b!=j :

                moves.append([i,b])
        for b in range(j,-1,-1):

            if grid[i][b][1]==self.color and b!=j:
                break
            elif grid[i][b][1] != '_' and b!=j:
                moves.append([i,b])
                break
            if inreach(i,b,grid,i,j) and b!=j :
                moves.append([i,b])
        return moves
class bishop:
    def __init__(self, row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.kind = 'B'

    def validmoves(self,grid):
        i=self.row
        j=self.col
        moves=[]
        for k, l in zip([1, -1, -1, 1], [1, -1, 1, -1]):
            a = i
            b = j
            while a>=0 and b>=0 and a<=3 and b<=3:

                if grid[a][b][1] == self.color and a!=i:
                    break
                elif grid[a][b][1] != '_' and inreach(a,b,grid,i,j):

                    moves.append([a,b])
                    break
                else:
                    if inreach(a, b, grid, i, j):
                        moves.append([a,b])
                a = a + k
                b = b + l
        return moves
class knight:
    def __init__(self, row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.kind = 'K'

    def validmoves(self,grid):
        i=self.row
        j=self.col
        moves=[]
        a,b=i,j
        moves=[]
        for k,l in zip([1,2,-1,-2,1,2,-1,-2],[2,1,-2,-1,-2,-1,2,1]):
            a=a+k
            b=b+l
            if inreach(a,b,grid,i,j):
                moves.append([a,b])
            a=i
            b=j
        return moves


def printgrid():
    for i in range(0,4):
        print(grid[i])

def figonboard(P,a,b):
    ar= False
    for i in range(0,4):
        for j in range(0,4):
            if grid[i][j]==P[a][b]:
                ar= True
    if ar==True :
        return True
    else:
        return False



class validmoves1:
    def __init__(self,col,row):
        self.col=col
        self.row=row
        self.add=col + row



def inreach(a,b,grid,i,j):

    if a >= 0 and a <= 3 and b>=0 and b<=3 and grid[i][j][1]!=grid[a][b][1]:
        return True
    else:
        return False