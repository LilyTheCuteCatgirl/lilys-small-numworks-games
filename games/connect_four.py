from kandinsky import fill_rect as F,draw_string as S
from ion import*;k=keydown
from time import sleep as t
B=(16,22,39)
Q=(25,80,200)
R=(242,72,80)
Y=(255,217,68)
E=(6,13,29)
W=(240,242,245)
G=(E,R,Y)
L,T,C=62,31,28
def O(x,y,color):
 F(x+8,y+3,12,22,color)
 F(x+4,y+5,20,18,color)
 F(x+2,y+9,24,10,color)
def w(b,c,r,s):
 for u,v0 in((1,0),(0,1),(1,1),(1,-1)):
  n0=1
  for g in(-1,1):
   x,y=c+u*g,r+v0*g
   while 0<=x<7 and 0<=y<6 and b[y*7+x]==s:
    n0+=1
    x+=u*g
    y+=v0*g
  if n0>=4:return 1
 return 0
def p(b,c,s):
 for r in range(5,-1,-1):
  if not b[r*7+c]:b[r*7+c]=s;return r
 return-1
def a0(b):
 o=[3,2,4,1,5,0,6]
 for s in(2,1):
  for c in o:
   r=p(b,c,s)
   if r>=0:
    win=w(b,c,r,s)
    b[r*7+c]=0
    if win:
     return c
 for c in o:
  if b[c]==0:
   return c
 return-1
def d(b,c,s,m):
 F(0,0,320,222,B)
 S('YOU'if s==1 and m==1 else'CPU'if m==1 else'RED'if s==1 else'YELLOW',3,3,W,B)
 F(L,T,196,168,Q)
 for r in range(6):
  for j in range(7):
   x,y=L+C*j,T+C*r
   O(x,y,G[b[r*7+j]])
 S('v',L+c*C+8,13,Y,B)
 S('LEFT/RIGHT  OK=DROP',20,201,W,B)
def h():
 F(0,0,320,222,B)
 S('CONNECT FOUR',66,52,W,B)
 S('OK: VS COMPUTER',52,98,R,B)
 S('EXE: 2 PLAYERS',52,128,Y,B)
 while not(k(KEY_OK)or k(KEY_EXE)):t(.04)
 a=1 if k(KEY_OK)else 2
 while k(KEY_OK)or k(KEY_EXE):
  t(.04)
 return a
def f(m):
 b=[0]*42
 c,s,n=3,1,0
 d(b,c,s,m)
 while True:
  if s==2 and m==1:
   a=a0(b)
   t(.23)
  else:
   a=-1
   if k(KEY_LEFT):
    c=(c-1)%7
    a=-2
   elif k(KEY_RIGHT):
    c=(c+1)%7
    a=-2
   elif k(KEY_OK)or k(KEY_EXE):
    a=c
   if a==-1:t(.04);continue
   while k(KEY_LEFT)or k(KEY_RIGHT)or k(KEY_OK)or k(KEY_EXE):
    t(.03)
   if a==-2:d(b,c,s,m);continue
  r=p(b,a,s)
  if r<0:continue
  n+=1
  v=w(b,a,r,s)
  d(b,c,s,m)
  if v or n==42:
   z=('RED WINS!'if s==1 else'YELLOW WINS!')if v else'DRAW!'
   F(72,88,180,52,B)
   S(z,81,89,W,B)
   S('OK TO RESTART',81,113,W,B)
   while k(KEY_OK):
    t(.04)
   while not k(KEY_OK):
    t(.04)
   while k(KEY_OK):
    t(.04)
   return
  s=3-s
  d(b,c,s,m)
while 1:f(h())