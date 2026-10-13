from kandinsky import fill_rect as F0,draw_string as S
from ion import*;k=keydown
from time import sleep as t
L=('########/#......#/#......#/#..$...#/#..o@..#/#......#/#......#/########','########/#......#/#..o.o.#/#..$.$.#/#...@..#/#......#/#......#/########','########/#......#/#..o.o.#/#..$.$.#/#..#@..#/#......#/#......#/########','########/#......#/#.o..o.#/#.$##$.#/#..@...#/#......#/#......#/########','########/#......#/#.oo...#/#.$$##.#/#...@..#/#......#/#......#/########',)
W=(245,245,245)
B=(15,19,30)
F=(49,55,70)
H=(65,105,170)
O=(226,157,65)
G=(240,200,75)
P=(55,235,207)
K=(KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT)
D=(-8,8,-1,1)
def u(v):
 a,b,c=[],[],[]
 p=0
 for i,ch in enumerate(L[v].replace('/','')):
  if ch=='#':
   a.append(i)
  if ch=='o':
   b.append(i)
  if ch=='$':
   c.append(i)
  if ch=='@':
   p=i
 return a,b,c,p
def d(v,a,b,c,p,s):
 F0(0,0,320,222,B)
 S('SOKOBAN '+str(v+1)+'/'+str(len(L)),70,2,W,B)
 for i in range(64):
  x,y=71+22*(i%8),23+22*(i//8)
  F0(x,y,21,21,H if i in a else F)
  if i in b:
   F0(x+7,y+7,7,7,G)
  if i in c:
   F0(x+3,y+3,15,15,O)
  if i==p:
   F0(x+4,y+4,13,13,P)
 m='SOLVED! OK NEXT'if s else'BACK=UNDO SHIFT=RESET'
 S(m,12,203,W,B)
def q(v):
 a,b,c,p=u(v)
 h=[]
 s=False
 d(v,a,b,c,p,s)
 while True:
  key=-1
  for i in range(4):
   if k(K[i]):
    key=i
    break
  if key>=0 and not s:
   n=p+D[key]
   if 0<=n<64 and n not in a:
    if n in c:
     j=n+D[key]
     if j<0 or j>=64 or j in a or j in c:
      n=p
     else:
      h.append((p,c[:]))
      c[c.index(n)]=j
    else:
     h.append((p,c[:]))
    p=n
    s=all(pos in b for pos in c)
    d(v,a,b,c,p,s)
  elif k(KEY_BACKSPACE)and h:
   p,c=h.pop()
   s=False
   d(v,a,b,c,p,s)
   key=4
  elif k(KEY_SHIFT):
   return v
  elif s and k(KEY_OK):
   return(v+1)%len(L)
  if key<0:
   t(.04)
  else:
   while k(K[key]if key<4 else KEY_BACKSPACE):
    t(.04)
def z():
 v=0
 while True:
  v=q(v)
  t(.1)
z()