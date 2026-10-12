from kandinsky import fill_rect as F,draw_string as D
from ion import*;K=keydown
from time import sleep as Z
B=(0,0,0)
W=(255,255,255)
G=(30,115,60)
U=(30,80,155)
R=(55,55,65)
P=(110,240,65)
L=(165,115,55)
C=(240,75,75)
A={2:(-1,2,78,134),3:(1,2,66,116),4:(-1,3,83,143),
6:(1,3,37,102),7:(-1,2,47,125),8:(1,4,34,100),9:(-1,3,42,115)}
H=(40,120,200,280)
def J():
 x=160
 y=10
 l=3
 s=0
 t=0
 q=0
 h=[0,0,0,0]
 e=0
 while True:
  if e:
   F(0,0,320,222,B)
   D('YOU WIN!'if e==2 else'GAME OVER',105,85,W,B)
   D('SCORE: '+str(s),100,110,W,B)
   D('OK TO RESTART',85,140,W,B)
   if K(KEY_OK):
    return
   Z(.08)
   continue
  if q:
   q-=1
  elif K(KEY_UP):
   y-=1
   q=3
  elif K(KEY_DOWN):
   y=min(10,y+1)
   q=3
  elif K(KEY_LEFT):
   x-=18
   q=3
  elif K(KEY_RIGHT):
   x+=18
   q=3
  t+=1
  a=1
  if y in A:
   d,v,w,g=A[y]
   if y<5:
    x+=d*v
    a=0
   for i in range(5):
    p=(i*g+t*v*d)%(5*g)-w
    if y<5:
     if p+8<=x<=p+w-8:
      a=1
    elif x+7>p and x-7<p+w:
     a=0
  if y==0:
   n=min(range(4),key=lambda i:abs(x-H[i]))
   if abs(x-H[n])<25 and not h[n]:
    h[n]=1
    s+=100
    if sum(h)==4:
     e=2
   else:
    a=0
   x,y=160,10
  if x<7 or x>313 or not a:
   l-=1
   x,y=160,10
   q=4
   if not l:
    e=1
  F(0,0,320,222,B)
  D('L:'+str(l)+' S:'+str(s),0,0,W,B)
  for r in range(11):
   Y=20+r*18
   F(0,Y,320,18,U if 2<=r<=4 else R if 6<=r<=9 else G)
  for i in range(4):
   F(H[i]-24,22,48,14,P if h[i]else B)
  for r,c in A.items():
   d,v,w,g=c
   for i in range(5):
    p=(i*g+t*v*d)%(5*g)-w
    if-w<p<320:
     z=max(0,p)
     k=min(320,p+w)
     if k>z:
      F(z,20+r*18+2,k-z,14,L if r<5 else C)
  F(x-7,20+y*18+2,14,14,P)
  F(x-4,20+y*18+4,3,3,B)
  F(x+2,20+y*18+4,3,3,B)
  Z(.06)
while True:
 J()