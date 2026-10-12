from kandinsky import fill_rect as F,draw_string as S
from ion import keydown as K,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_OK,KEY_EXE,KEY_SHIFT
from time import sleep as Z
from random import randint as I
W=12;H=9;M=18
T=(255,255,255)
B=(0,0,0)
G=(160,165,175)
U=(25,75,210)
R=(210,35,35)
def N(p):
 x=p%W;y=p//W
 return[(y+j)*W+x+i for j in(-1,0,1)for i in(-1,0,1)if 0<=x+i<W and 0<=y+j<H and(i or j)]
def C(p):return sum(m[q]for q in N(p))
def D(p):
 x=34+21*(p%W);y=22+21*(p//W)
 c=T if o[p]else G
 F(x,y,20,20,c)
 if o[p]:
  if m[p]:S('*',x+5,y+1,R,c)
  else:
   n=C(p)
   if n:S(str(n),x+5,y+1,(0,0,200)if n<3 else R,c)
 elif f[p]:S('F',x+5,y+1,R,c)
 if p==j:
  F(x,y,20,1,U)
  F(x,y+19,20,1,U)
  F(x,y,1,20,U)
  F(x+19,y,1,20,U)
def A(s=''):
 F(0,0,320,20,T)
 S(s or'MINES '+str(M)+' FLAGS '+str(sum(f)),4,0,B,T)
def J():
 global m,o,f,j,a
 m=[0]*(W*H);o=[0]*(W*H);f=[0]*(W*H)
 j=0;a=True
 F(0,0,320,222,T)
 for p in range(W*H):D(p)
 A()
def P(p):
 b=N(p)+[p]
 n=0
 while n<M:
  q=I(0,W*H-1)
  if q not in b and not m[q]:m[q]=1;n+=1
def V(p):
 t=[p]
 while t:
  q=t.pop()
  if o[q]or f[q]:continue
  o[q]=1
  D(q)
  if C(q)==0 and not m[q]:
   for z in N(q):
    if not o[z]and not f[z]:t.append(z)
def L():
 global j,a
 J()
 z=(KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_OK,KEY_EXE,KEY_SHIFT)
 while True:
  k=-1
  for i,v in enumerate(z):
   if K(v):k=i;break
  if k<0:Z(.04);continue
  d=j
  x=j%W;y=j//W
  if k==0 and y>0:j-=W
  if k==1 and y<H-1:j+=W
  if k==2 and x>0:j-=1
  if k==3 and x<W-1:j+=1
  if k==6 and not o[j]:
   f[j]=1-f[j]
   A()
  if k in(4,5)and not f[j]and not o[j]:
   if a:P(j);a=False
   if m[j]:
    for p in range(W*H):
     if m[p]:o[p]=1;D(p)
    A('BOOM! OK TO RESTART')
    break
   V(j)
   if sum(o)==W*H-M:
    A('YOU WIN! OK TO RESTART');break
  D(d);D(j)
  while K(z[k]):Z(.035)
 while K(KEY_OK)or K(KEY_EXE):Z(.05)
 while not(K(KEY_OK)or K(KEY_EXE)):Z(.05)
 while K(KEY_OK)or K(KEY_EXE):Z(.05)
while True:L()