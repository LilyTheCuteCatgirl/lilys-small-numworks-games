from kandinsky import fill_rect as F,draw_string as S
from ion import*;K=keydown
from time import sleep as Z,monotonic as M
from random import randint as I
H='4567125614561245015604562456'
C=((20,20,20),(0,210,220),(255,225,40),(190,80,225),(70,215,85),(245,70,70),(65,100,255),(255,150,55))
W=(255,255,255)
def B(n,r,x,y):
 for ch in H[n*4:n*4+4]:
  k=int(ch,16);a=k%4;b=k//4
  if n!=1:
   for _ in range(r):a,b=3-b,a
  yield x+a,y+b
def T(n,r,x,y):
 for a,b in B(n,r,x,y):
  if a<0 or a>=10 or b>=20 or b>=0 and g[b][a]:return 0
 return 1
def P(x,y,c):
 if y>=0:F(82+10*x,20+10*y,9,9,C[c])
def D():
 F(78,16,104,204,(90,90,90))
 F(81,19,100,200,C[0])
 for j in range(20):
  for i in range(10):
   if g[j][i]:P(i,j,g[j][i])
 for a,b in B(p,r,u,v):P(a,b,p+1)
 F(194,0,126,122,W)
 S('TETRIS',204,8)
 S('SCORE',204,38)
 S(str(s),204,58)
 S('LINES '+str(l),204,84)
 S('LV '+str(e),204,104)
def N():
 global p,r,u,v,b
 if not b:b=list(range(7))
 p=b.pop(I(0,len(b)-1))
 r=0;u=3;v=-1
 return T(p,r,u,v)
def L():
 global g,s,l,e
 for x,y in B(p,r,u,v):
  if y<0:return 0
  g[y][x]=p+1
 q=[row for row in g if 0 in row]
 c=20-len(q)
 g=[[0]*10 for _ in range(c)]+q
 l+=c
 e=1+l//10
 s+=(0,100,300,500,800)[c]*e
 return N()
def V():
 global g,p,r,u,v,b,s,l,e
 g=[[0]*10 for _ in range(20)]
 b=[];s=0;l=0;e=1
 N()
 F(0,0,320,222,W)
 S('ROTATE',0,20)
 S('MOVE',0,50)
 S('FALL',0,80)
 S('DROP',0,110)
 S('TETRIS',0,185)
 t=M();j=t;h=0;d=0
 D()
 while 1:
  o=M();c=0
  U=K(KEY_UP)
  if U and not h:
   a=(r+1)%4
   for w in(0,-1,1,-2,2):
    if T(p,a,u+w,v):r=a;u+=w;c=1;break
  h=U
  f=K(KEY_LEFT);i=K(KEY_RIGHT)
  if f or i:
   if o>=j:
    m=u+i-f
    if T(p,r,m,v):u=m;c=1
    j=o+.12
  else:j=o
  k=K(KEY_OK)or K(KEY_EXE)
  if k and not d:
   while T(p,r,u,v+1):v+=1;s+=1
   if not L():break
   c=1;t=o
  d=k
  z=max(.10,.68-.045*(e-1))
  if o-t>=(.065 if K(KEY_DOWN)else z):
   if T(p,r,u,v+1):v+=1
   elif not L():break
   c=1;t=o
  if c:D()
  Z(.025)
 F(72,90,156,50,W)
 S('GAME OVER',86,98)
 S('OK RESTART',82,118)
 while K(KEY_OK)or K(KEY_EXE):Z(.05)
 while not(K(KEY_OK)or K(KEY_EXE)):Z(.05)
 while K(KEY_OK)or K(KEY_EXE):Z(.05)
while 1:V()