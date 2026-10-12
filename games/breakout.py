from kandinsky import fill_rect as F,draw_string as D
from ion import*;K=keydown
from time import sleep as Z
Q=(0,0,0)
W=(255,255,255)
C=((230,70,70),(250,140,45),(230,205,65),(85,195,115),(75,150,225))
def G():
 s=0
 l=3
 v=1
 p=130
 x=160
 y=175
 u=2
 w= -2
 b=[1]*60
 m=60
 e=0
 F(0,0,320,222,Q)
 def H():
  F(0,0,320,222,Q)
  for i in range(60):
   if b[i]:
    F(5+i%12*26,27+i//12*12,24,9,C[i//12])
  D('S:'+str(s)+' L:'+str(l)+' Lv:'+str(v),0,0,W,Q)
 H()
 while 1:
  if e:
   D('YOU WIN!'if e==2 else'GAME OVER',105,115,W,Q)
   D('OK TO RESTART',85,137,W,Q)
   if K(KEY_OK):
    return
   Z(.08)
   continue
  F(p,190,58,7,Q)
  F(x-3,y-3,6,6,Q)
  if K(KEY_LEFT):
   p=max(1,p-6)
  if K(KEY_RIGHT):
   p=min(261,p+6)
  o=y
  x+=u
  y+=w
  if x<4 or x>316:
   u= -u
   x=max(4,min(316,x))
  if y<23:
   w=abs(w)
  if 27<=y<87 and 5<=x<317:
   j=(x-5)//26
   k=(y-27)//12
   if j<12 and b[k*12+j]:
    b[k*12+j]=0
    m-=1
    s+=10
    w= -w
    F(5+j*26,27+k*12,24,9,Q)
    D('S:'+str(s)+' L:'+str(l)+' Lv:'+str(v),0,0,W,Q)
  if w>0 and o<190<=y+3 and p-3<=x<=p+61:
   w= -abs(w)
   t=x-(p+29)
   u= -3 if t< -14 else(-2 if t<0 else(2 if t<14 else 3))
  if y>218:
   l-=1
   if not l:
    e=1
   else:
    x,y,u,w=160,175,2,-2
    p=130
    H()
  if not m:
   v+=1
   if v>3:
    e=2
   else:
    b=[1]*60
    m=60
    x,y,u,w=160,175,2+v//2,-2-v//2
    H()
  F(p,190,58,7,W)
  F(x-3,y-3,6,6,W)
  Z(.045)
while 1:
 G()