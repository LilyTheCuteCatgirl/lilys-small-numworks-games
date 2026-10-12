from random import*;from kandinsky import*;from ion import*;from time import*
W=(255,255,255);K=(0,0,0);S=(0,204,0);R=(255,0,0)
def n(i,x,y):
 d=i[-1];x,y=c(x+10*((d==0)-(d==3)),y+10*((d==1)-(d==2)));return[x,y]
def j(q,r):
 o=randint(0,31)*10+4;p=randint(0,21)*10+5
 while get_pixel(o,p)!=r:o=randint(0,31)*10+4;p=randint(0,21)*10+5
 fill_rect(o-4,p-4,10,10,q);return(o,p)
def c(x,y):
 if x<4:x=314
 if x>314:x=4
 if y<5:y=215
 if y>215:y=5
 return(x,y)
def m(u):
 for k in range(4):
  if keydown(k)and u+k!=3:return k
 return u
def f():fill_rect(0,0,320,222,W)
def h():draw_string('(DELETE to exit)',0,0);a(31183,70,80,10,S);fill_rect(95,80,2,4,K);fill_rect(95,86,2,4,K);fill_rect(100,84,4,2,R);fill_rect(104,82,2,2,R);fill_rect(104,86,2,2,R);U()
def a(p,x,y,o,q):
 for s in range(5):
  for r in range(3):
   if p>>(14-s*3-r)&1:fill_rect(x+r*o,y+s*o,o,o,q)
def U():
 for i,v in enumerate((31597,31725,23469,31207)):a(v,110+40*i,80,10,K)
def l():
 f();h();draw_string('> Play <',125,140,'red')
 while not keydown(KEY_OK):
  if keydown(KEY_BACKSPACE):f();return
  sleep(0.1)
 g()
def g():
 D=(248,252,248);t=K;s=S;w=(248,0,0)
 fill_rect(0,0,320,222,D);fill_rect(0,221,320,1,K)
 try:get_keys()
 except:fill_rect(0,0,320,1,(255,181,49))
 else:fill_rect(0,0,320,1,(197,52,49))
 D=get_pixel(2,40)
 A=[3,3,3,3,3];x=154;y=115;E=104;F=115;u,v=(3,3);z=5;q,r=j(w,D);w=get_pixel(q,r);o,p=(0,0)
 while p!=t and p!=s:
  if keydown(0)or keydown(1)or keydown(2)or keydown(3):u=m(u)
  if keydown(KEY_BACKSPACE):
   while keydown(KEY_BACKSPACE):sleep(0.1)
   while not keydown(KEY_BACKSPACE):sleep(0.1)
   while keydown(KEY_BACKSPACE):sleep(0.1)
  A.append(u)
  if x==q and y==r:z=z+1;q,r=j(w,D);o=o+1
  x=x+((u==3)-(u==0))*10;y=y+((u==2)-(u==1))*10;x,y=c(x,y)
  if z:z=z-1
  else:A.remove(A[0]);E=E+((v==3)-(v==0))*10;F=F+((v==2)-(v==1))*10;E,F=c(E,F);v=A[0];fill_rect(E-4,F-4,10,10,D)
  p=get_pixel(x,y)
  if x<0 or x>320 or y<0 or(y>220):p=t
  if p!=w and p!=D:p=t
  fill_rect(x-4,y-4,10,10,s);s=get_pixel(x,y);I=n(A,x,y)
  if u==3 or u==0:fill_rect(x,y-4,2,4,K);fill_rect(x,y+2,2,4,K);fill_rect(I[0]-4,I[1]-4,10,10,s)
  elif u==2 or u==1:fill_rect(x-4,y,4,2,K);fill_rect(x+2,y,4,2,K);fill_rect(I[0]-4,I[1]-4,10,10,s)
  sleep(0.05)
  while s==w or s==D:s=(randint(0,255),randint(0,255),randint(0,255))
  if len(A)==640:
   draw_string('You win !',120,100);draw_string('(You reached the max length)',20,120)
   p=t
 draw_string('Score:'+str(o),10,10);draw_string('(OK=play again, DELETE=Menu)',10,30)
 C=0
 while not C:
  if keydown(KEY_OK):C=1;g()
  elif keydown(KEY_BACKSPACE):C=2;l()
 print('Score:',o)
l()