from kandinsky import fill_rect as R,draw_string as T
from ion import keydown as K,KEY_LEFT as L,KEY_RIGHT as H,KEY_OK as O,KEY_EXE as E
from time import sleep as S
from random import randint as Q
B=(0,0,0)
W=(255,255,255)
G=(40,255,80)
C=(50,220,255)
D=(255,75,75)
P=((255,75,75),(255,220,50),(80,255,90))
def A():
 return[(m*29,r*23,r)for r in range(3)for m in range(8)]
def J():
 x=150
 u=0
 v=-1
 j=0
 k=-1
 h=3
 s=0
 n=1
 a=A()
 b=42
 c=32
 d=3
 f=0
 z=0
 while h>0:
  f+=1
  if K(L):x=max(1,x-4)
  if K(H):x=min(299,x+4)
  if(K(O)or K(E))and v<0:
   u=x+10
   v=194
  if v>=0:v-=7
  if v<0:v=-1
  if k>=0:k+=4+n//3
  if k>220:k=-1
  if z:z-=1
  if f%max(3,8-n)==0:
   b+=d
   o=min(p[0]for p in a)+b
   t=max(p[0]for p in a)+b+18
   if o<3 or t>316:
    b-=d
    d=-d
    c+=9
  if v>=0:
   for i in a:
    e=b+i[0]
    g=c+i[1]
    if e<=u<=e+19 and g<=v<=g+13:
     a.remove(i)
     s+=10
     v=-1
     break
  if k>=0 and j>=x and j<=x+21 and 194<=k<=211 and not z:
   h-=1
   z=30
   k=-1
  if not a:
   n+=1
   a=A()
   b=42
   c=32
   d=3
   k=-1
   v=-1
  if max(p[1]for p in a)+c>185:
   h=0
  if k<0 and f%32==0:
   i=a[Q(0,len(a)-1)]
   j=b+i[0]+9
   k=c+i[1]+12
  R(0,0,320,222,B)
  T('S:'+str(s)+' L:'+str(h)+' W:'+str(n),3,0,W,B)
  for e,g,r in a:
   X=b+e
   Y=c+g
   R(X,Y,19,12,P[r])
   R(X+4,Y+4,3,3,B)
   R(X+12,Y+4,3,3,B)
  if z%4<2:
   R(x,201,22,9,C)
   R(x+8,197,6,5,C)
  if v>=0:R(u,v,3,8,G)
  if k>=0:R(j,k,3,8,D)
  S(.045)
 R(0,0,320,222,B)
 T('GAME OVER',110,85,W,B)
 T('SCORE: '+str(s),100,110,W,B)
 T('OK TO RESTART',90,140,W,B)
 while not K(O):S(.05)
 while K(O):S(.05)
while True:J()