from kandinsky import fill_rect as F,draw_string as S
from ion import keydown as Q,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_OK
from time import sleep as E,monotonic as M
from random import randint as I
R='################# #o.....#.......o# #.###..#..###.#.# #......#........# #.###.....###.#.# #...#..#..#.....# ###.#.....#.###.# #......#........# #.###.....###.#.# #...#..#..#...#.# #.#....#....#...# #o.............o# #################'.split()
D=((0,-1),(0,1),(-1,0),(1,0))
K=(KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT)
B=(0,0,0)
U=(20,50,190)
W=(255,255,255)
Y=(255,220,0)
G=((255,60,80),(0,220,230),(250,100,230))
def C(x,y):
 c=m[y][x];a=41+14*x;b=22+14*y
 F(a,b,14,14,U if c=='#'else B)
 if c=='.':F(a+6,b+6,2,2,W)
 if c=='o':F(a+4,b+4,6,6,Y)
def A(x,y,c):
 a=41+14*x;b=22+14*y
 F(a+2,b+2,10,10,c)
 if c!=Y:
  F(a+4,b+4,2,2,W)
  F(a+8,b+4,2,2,W)
def H():
 F(0,0,320,20,B)
 S('PAC-MAN '+str(s)+'  LIVES '+str(l),1,0,Y,B)
def V(text):
 F(32,91,256,38,B)
 S(text,36,100,Y,B)
 while Q(KEY_OK):E(.06)
 while not Q(KEY_OK):E(.06)
 while Q(KEY_OK):E(.06)
def Z():
 global a,b,O,t
 a,b=8,11
 O=[[8,6],[8,3],[3,5]]
 t=0
def T(x,y):
 return 0<=y<len(m)and 0<=x<17 and m[y][x]!='#'
def J():
 for y in range(len(m)):
  for x in range(17):C(x,y)
def X():
 global l,s,p
 for i,g in enumerate(O):
  if g[0]==a and g[1]==b:
   if p:
    s+=200
    O[i]=[8,6]
   else:
    l-=1
    H()
    E(.35)
    Z()
    J()
    H()
    return True
 return False
def P():
 global m,a,b,O,t,s,l,p,n
 m=[list(row)for row in R]
 n=sum(row.count('.')+row.count('o')for row in R)
 s=0;l=3;p=0
 Z()
 F(0,0,320,222,B)
 J()
 H()
 A(a,b,Y)
 for i,g in enumerate(O):A(g[0],g[1],G[i])
 w=2;d=2;z=M()
 while l and n:
  for i in range(4):
   if Q(K[i]):w=i
  v=M()
  if v-z<.15:
   E(.02)
   continue
  z=v
  o=(a,b)
  i,j=D[w]
  if T(a+i,b+j):d=w
  i,j=D[d]
  if T(a+i,b+j):a+=i;b+=j
  c=m[b][a]
  if c in'.o':
   if c=='o':s+=50;p=35
   else:s+=10
   n-=1;m[b][a]=' '
  C(o[0],o[1])
  C(a,b)
  if X():continue
  t+=1
  if t%2==0:
   for i,g in enumerate(O):
    ox,oy=g
    q=[(ox+i,oy+j)for i,j in D if T(ox+i,oy+j)]
    if q:
     if I(0,4)==0:
      nx,ny=q[I(0,len(q)-1)]
     else:
      def e(p):return abs(p[0]-a)+abs(p[1]-b)
      h=q[0]
      for q in q[1:]:
       if(p and e(q)>e(h))or(not p and e(q)<e(h)):h=q
      nx,ny=h
     O[i]=[nx,ny]
     C(ox,oy)
     if X():break
  A(a,b,Y)
  for i,g in enumerate(O):A(g[0],g[1],(G[i]if not p else(35,35,230)))
  if p:p-=1
  H()
 V('YOU WIN!'if n==0 else'GAME OVER')
while True:P()