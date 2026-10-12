from kandinsky import fill_rect as R,draw_string as T
from ion import*;K=keydown;U=KEY_UP;N=KEY_DOWN;O=KEY_OK
from time import sleep as S
B=(0,0,0)
W=(255,255,255)
def M():
 a=104
 b=104
 x=160
 y=110
 u=-3
 v=2
 p=0
 q=0
 while p<5 and q<5:
  if K(U):
   a=max(23,a-4)
  if K(N):
   a=min(191,a+4)
  if b+12<y-3:
   b=min(191,b+2)
  if b+12>y+3:
   b=max(23,b-2)
  x+=u
  y+=v
  if y<=25 or y>=216:
   v=-v
   y=max(25,min(216,y))
  if x<=15 and u<0 and a-3<=y<=a+27:
   u=3
   v=max(-4,min(4,(y-a-12)//4))
   if v==0:v=1
  if x>=301 and u>0 and b-3<=y<=b+27:
   u=-3
   v=max(-4,min(4,(y-b-12)//4))
   if v==0:v=-1
  if x<0 or x>319:
   if x<0:q+=1
   else:p+=1
   x=160
   y=110
   u=3 if(p+q)%2 else-3
   v=2 if(p+q)%3 else-2
   S(.22)
  R(0,0,320,222,B)
  T(str(p)+' : '+str(q),137,0,W,B)
  for h in range(25,222,18):
   R(159,h,2,9,W)
  R(8,a,6,25,W)
  R(306,b,6,25,W)
  R(x-3,y-3,7,7,W)
  S(.04)
 R(0,0,320,222,B)
 T('YOU WIN!'if p>q else'GAME OVER',105,85,W,B)
 T('OK TO RESTART',90,120,W,B)
 while not K(O):S(.05)
 while K(O):S(.05)
while 1:M()