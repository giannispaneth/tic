import pygame
import sys
from pygame.locals import *
pygame.init()
grid=[[0]*4 for n in range(4)]
grid1=[[(350,250),(450,250),(550,250),(650,250)],[(350,350),(450,350),(550,350),(650,350)],[(350,450),(450,450),(550,450),(650,450)],[(350,550),(450,550),(550,550),(650,550)]]
gameDisplay= pygame.display.set_mode((1000,1000))
pygame.display.set_caption('tic tac chec')
running = True
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (255,0,0)
wow=[0,0,0,0]
image=[0,0,0,0]
imagequeen = pygame.image.load('C:/Users/user/Desktop/queen.png')
image[0] = pygame.image.load('C:/Users/user/Desktop/pawn (2).png')
image[1] = pygame.image.load('C:/Users/user/Desktop/queen.png')
image[2] = pygame.image.load('C:/Users/user/Desktop/queen.png')
image[3] = pygame.image.load('C:/Users/user/Desktop/queen.png')
wow[0]=image[0].get_rect()
wow[1]=image[1].get_rect()
wow[2]=image[2].get_rect()
wow[3]=image[3].get_rect()
max1=[10000,10000,10000,10000]
max=10000
x=[318,418,518,618]
y=[218,218,218,218]
w=[350,450,550,650]
z=[250,250,250,250]
t=[318,418,518,618]
t1=[318,418,518,618]
o1=[118,118,118,118]
o=[118,118,118,118]
a=[0,0,0,0]
wow[0].x=318
wow[0].y=118
wow[1].x=418
wow[1].y=118
wow[2].x=518
wow[2].y=118
wow[3].x=618
wow[3].y=118
u=0
r=5
u=0
l=1
choose=0


def board():
    for i in range(1, 5):
        for j in range(1, 5):
            pygame.draw.rect(gameDisplay, [((i + j) % 2) * 255, ((i + j) % 2) * 255, ((i + j) % 2) * 255],
                             (100 * i + 200, 100 * j + 100, 100, 100))
gameDisplay.fill(BLUE)
board()

def player(mouse1,mouse2):
    global k,r,image
    gameDisplay.blit(image[k],(mouse1,mouse2))


while running:


    pygame.display.update()
    gameDisplay.fill(BLUE)
    board()
    for k in range(0,4):
        if max1[k]<=10000:
            player(t[k],o[k])
    mous= pygame.mouse.get_pressed()
    if mous[0]==1:
        POS = pygame.mouse.get_pos()
        for k in range(0,4):

            if wow[k].collidepoint(POS) and u==0:
                u=u+1

                a[k] = 1
                x[k] = POS[0]
                y[k] = POS[1]
                wow[k].centerx = x[k]
                wow[k].centery = y[k]
                w[k] = x[k]
                z[k] = y[k]
                x[k] = x[k] - 32
                y[k] = y[k] - 32
                t1[k] = t[k]
                o1[k] = o[k]
                r=k
                u=r
                player(x[k], y[k])
                max1[k] = 10000
            elif wow[k].collidepoint(POS) and u == 1 and k==r:
                    u = 0

                    a[k] = 1
                    x[k] = POS[0]
                    y[k] = POS[1]
                    wow[k].centerx = x[k]
                    wow[k].centery = y[k]
                    w[k] = x[k]
                    z[k] = y[k]
                    x[k] = x[k] - 32
                    y[k] = y[k] - 32
                    t1[k] = t[k]
                    o1[k] = o[k]
                    r = k
                    u = r
                    player(x[k], y[k])
                    max1[k] = 10000

    l=0
    if mous[0]==0 and r != 5:

        for i in [350, 450, 550, 650]:
            for j in [250, 350, 450, 550]:
                if (i - w[r]) ** 2 + (j - z[r]) ** 2 <= max1[r]:
                    max1[r] = (i - w[r]) ** 2 + (j - z[r]) ** 2
                    if a[r] == 1:
                        t[r] = i - 32
                        o[r] = j - 32

        if max1[r] <= 10000:
            k=r
            player(t[r], o[r])
            wow[r].centerx = t[r] + 32
            wow[r].centery = o[r] + 32
        else:
            k=r
            player(t1[r], o1[r])
            wow[r].centerx = t1[r] + 32
            wow[r].centery = o1[r] + 32

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            POS=pygame.mouse.get_pos()

            print(POS)









