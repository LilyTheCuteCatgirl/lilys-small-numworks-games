from kandinsky import fill_rect as F0,draw_string as S
from ion import*;k=keydown
from time import sleep as t
L='6Y~8X~=O~<|4<HL~0T~6P~5|04>EFGLMN~5TV~8@P~9|17>@LXY~49=~GNP~?|-./ADGLQ~089T~5=FO~4|79E[~-.8~J]_~h|17H^e~;<T`~RT[_~Q|8IJSVW~03<i~@B[^~A|6ADJL\\_~28<g~V[^g~h|BJL~789:;~[\\]^_~f'.split('|')
W=(245,245,245)
B=(15,19,30)
F=(49,55,70)
H=(65,105,170)
O=(226,157,65)
G=(240,200,75)
P=(55,235,207)
K=(KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT)
def u(v):
 n=8+(v>4);a,b,c,p=L[v].split('~')
 a=[i for i in range(n*n)if i//n in(0,n-1)or i%n in(0,n-1)or chr(i+35)in a]
 return a,[ord(q)-35 for q in b],[ord(q)-35 for q in c],ord(p)-35,n
def d(v,a,b,c,p,s,n):
 F0(0,0,320,222,B)
 S('SOKOBAN '+str(v+1)+'/'+str(len(L)),70,2,W,B)
 z=38-2*n
 for i in range(n*n):
  x,y=71+z*(i%n),23+z*(i//n)
  F0(x,y,z-1,z-1,H if i in a else F)
  if i in b:
   F0(x+7,y+7,7,7,G)
  if i in c:
   F0(x+3,y+3,15,15,O)
  if i==p:
   F0(x+4,y+4,13,13,P)
 m='SOLVED! OK NEXT'if s else'BACK=UNDO SHIFT=RESET'
 S(m,12,203,W,B)
def q(v):
 a,b,c,p,N=u(v);D=(-N,N,-1,1)
 h=[]
 s=False
 d(v,a,b,c,p,s,N)
 while True:
  key=-1
  for i in range(4):
   if k(K[i]):
    key=i
    break
  if key>=0 and not s:
   n=p+D[key]
   if n not in a:
    if n in c:
     j=n+D[key]
     if j in a or j in c:n=p
    if n!=p:
     h.append((p,c[:]))
     if n in c:c[c.index(n)]=j
    p=n
    s=all(pos in b for pos in c)
    d(v,a,b,c,p,s,N)
  elif k(KEY_BACKSPACE)and h:
   p,c=h.pop()
   s=False
   d(v,a,b,c,p,s,N)
   key=4
  elif k(KEY_SHIFT):
   return v
  elif s and k(KEY_OK):
   return(v+1)%10
  if key<0:
   t(.04)
  else:
   while k(K[key]if key<4 else KEY_BACKSPACE):
    t(.04)
v=0
while 1:v=q(v);t(.1)