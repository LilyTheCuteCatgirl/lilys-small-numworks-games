from kandinsky import fill_rect as F,draw_string as S
from ion import*;k=keydown
from time import sleep as t
from random import randint as r
W,H,T,O=53,32,6,30
B=(7,12,25)
C=(20,235,255)
R=(255,75,95)
A=(245,245,245)
D=((0,-1),(1,0),(0,1),(-1,0))
Z=(KEY_UP,KEY_RIGHT,KEY_DOWN,KEY_LEFT)
def Q():
 g=[0]*(W*H)
 a,b,p=12,10,1
 u,v,e=40,22,3
 F(0,0,320,222,B)
 S('TRON  ARROWS=TURN',53,4,A,B)
 F(0,O-2,320,2,(55,65,95))
 def f(x,y):
  return 0<=x<W and 0<=y<H and not g[y*W+x]
 def P(x,y,color):
  F(x*T+1,O+y*T+1,T-2,T-2,color)
 g[b*W+a]=1
 g[v*W+u]=2
 P(a,b,C)
 P(u,v,R)
 while True:
  for i in range(4):
   if k(Z[i])and(i+2)%4!=p:
    p=i
    break
  c=(-1,-1)
  for i in(e,(e+1)%4,(e+3)%4):
   dx,dy=D[i];j=1
   while j<8 and f(u+dx*j,v+dy*j):j+=1
   c=max(c,((j-1)*4+r(0,2),i))
  e=c[1]
  dx,dy=D[p]
  nx,ny=a+dx,b+dy
  dx,dy=D[e]
  mx,my=u+dx,v+dy
  o=f(nx,ny)
  q=f(mx,my)
  if(nx,ny)==(mx,my):o=q=0
  if not(o and q):
   m='YOU WIN!'if o else'YOU LOSE!'if q else'DRAW!'
   F(66,93,198,54,B)
   S(m,108,95,A,B)
   S('OK TO RESTART',78,117,A,B)
   while k(KEY_OK):
    t(.05)
   while not k(KEY_OK):
    t(.05)
   while k(KEY_OK):
    t(.05)
   return
  a,b,u,v=nx,ny,mx,my
  g[ny*W+nx]=1
  g[my*W+mx]=2
  P(nx,ny,C)
  P(mx,my,R)
  t(.14)
while 1:Q()