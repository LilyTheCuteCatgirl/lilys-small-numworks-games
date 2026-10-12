from random import*;from kandinsky import*;from ion import*;from time import*
W=(255,255,255);K=(0,0,0);S=(0,204,0);R=(255,0,0)
def b():
 try:get_keys()
 except:return'orange'
 else:return'red'
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
  if keydown(k)==True and u+k!=3:return k
 return u
def f():fill_rect(0,0,320,222,W)
def d():print('\n \n \n \n \n \n \n \n \n \n \n \n \n ')
def h():draw_string('(DELETE to exit)',0,0);a(31183,70,80,10,S);fill_rect(95,80,2,4,K);fill_rect(95,86,2,4,K);fill_rect(100,84,4,2,R);fill_rect(104,82,2,2,R);fill_rect(104,86,2,2,R);U()
def a(p,x,y,o,q):
 for s in range(5):
  for r in range(3):
   if p>>(14-s*3-r)&1:fill_rect(x+r*o,y+s*o,o,o,q)
def U():
 for i,v in enumerate((31597,31725,23469,31207)):a(v,110+40*i,80,10,K)
def X(i,r,s,o):
 for j,(t,x,y)in enumerate((('Speed:'+str(r),50,140),('Power:+'+str(s),200,140),('Score:+'+str(o),50,170),('Play',220,170))):draw_string(t,x,y,b()if i==j+1 else'black','white')
def l():
 f();h();draw_string('> Play <',125,140,b());draw_string('  Options  ',110,165);q=0;r=0.05;s=5;o=1;z=0;p=1
 while keydown(KEY_OK)!=True and z==0:
  if keydown(KEY_DOWN)and p==1:draw_string('  Play  ',125,140);draw_string('> Options <',110,165,b());p=2
  elif keydown(KEY_UP)and p==2:draw_string('> Play <',125,140,b());draw_string('  Options  ',110,165);p=1
  if keydown(KEY_LEFTPARENTHESIS)and keydown(KEY_RIGHTPARENTHESIS):draw_string('Dark mode enabled !',80,195);q=1
  if keydown(KEY_BACKSPACE):z=1
  sleep(0.1)
 if p==2 and z!=1:
  fill_rect(0,130,300,60,W);r=0.05;s=5;o=1;X(1,r,s,o);p=1;sleep(0.2)
  while keydown(KEY_OK)!=True or p!=4:
   if keydown(KEY_RIGHT):p=p+1
   elif keydown(KEY_DOWN):p=p+2
   elif keydown(KEY_LEFT):p=p-1
   elif keydown(KEY_UP):p=p-2
   if p<0:p=0
   if p>4:p=4
   if p==1:
    X(p,r,s,o)
    if keydown(KEY_OK):d();r=input('Speed:');h()
   elif p==2:
    X(p,r,s,o)
    if keydown(KEY_OK):d();s=int(input('Power:+'));h()
   elif p==3:
    X(p,r,s,o)
    if keydown(KEY_OK):d();o=int(input('Score:'));h()
   elif p==4:X(p,r,s,o)
   if keydown(KEY_LEFTPARENTHESIS)and keydown(KEY_RIGHTPARENTHESIS)or q==1:draw_string('Dark mode enabled !',80,195);q=1
   if keydown(KEY_BACKSPACE):z=1;break
   sleep(0.1)
 if z!=1:
  if q==1:g(1,r,s,o)
  elif q==0:g(0,r,s,o)
 elif z==1:f();return
def g(B=0,J=0.05,G=5,H=1):
 D=(248,252,248);t=K;s=S;w=(248,0,0)
 if B==1:D=K;t=(0,0,204)
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
   while keydown(KEY_BACKSPACE)!=True:sleep(0.1)
   while keydown(KEY_BACKSPACE):sleep(0.1)
  A.append(u)
  if x==q and y==r:z=z+float(G);q,r=j(w,D);o=o+int(H)
  x=x+((u==3)-(u==0))*10;y=y+((u==2)-(u==1))*10;x,y=c(x,y)
  if z:z=z-1
  else:A.remove(A[0]);E=E+((v==3)-(v==0))*10;F=F+((v==2)-(v==1))*10;E,F=c(E,F);v=A[0];fill_rect(E-4,F-4,10,10,D)
  p=get_pixel(x,y)
  if x<0 or x>320 or y<0 or(y>220):p=t
  if p!=w and p!=D:p=t
  fill_rect(x-4,y-4,10,10,s);s=get_pixel(x,y);I=n(A,x,y)
  if u==3 or u==0:fill_rect(x,y-4,2,4,K);fill_rect(x,y+2,2,4,K);fill_rect(I[0]-4,I[1]-4,10,10,s)
  elif u==2 or u==1:fill_rect(x-4,y,4,2,K);fill_rect(x+2,y,4,2,K);fill_rect(I[0]-4,I[1]-4,10,10,s)
  sleep(float(J))
  while s==w or s==D:s=(randint(0,255),randint(0,255),randint(0,255))
  if len(A)==640:
   if B==1:draw_string('You win !',120,100,'white','black');draw_string('(You reached the max length)',20,120,'white','black')
   else:draw_string('You win !',120,100);draw_string('(You reached the max length)',20,120)
   p=t
 if B==1:draw_string('Score:'+str(o),10,10,'white','black');draw_string('(OK=play again, DELETE=Menu)',10,30,'white','black')
 else:draw_string('Score:'+str(o),10,10);draw_string('(OK=play again, DELETE=Menu)',10,30)
 C=0
 while C==0:
  if keydown(KEY_OK):C=1;g(B,J,G,H)
  elif keydown(KEY_BACKSPACE):C=2;l()
 print('Score:',o)
l()