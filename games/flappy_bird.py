from math import*;from time import*;from ion import keydown as kd,KEY_OK as ko,KEY_UP as ku;from kandinsky import fill_rect as fr;from kandinsky import*;from random import*;from ion import*;d='black';m='white';z='red';w='yellow';D=color(173,216,230);p=color(144,238,144);u=color(0,100,0)
def n(K,L):
 fr(K,L+150,38,2,d);fr(K,L+150,2,8,d);fr(K+2,L+158,2,6,d);fr(K+4,L+164,2,150,d);fr(K+36,L+150,2,8,d);fr(K+34,L+158,2,4,d);fr(K+32,L+162,2,150,d);fr(K+6,L+164,26,2,d);fr(K+2,L+152,2,6,p);fr(K+4,L+158,2,6,p);fr(K+6,L+166,2,150,p);fr(K+34,L+152,2,6,p);fr(K+32,L+158,2,4,p);fr(K+30,L+162,2,1,p);fr(K+30,L+166,2,150,p);fr(K+4,L+152,30,6,u);fr(K+6,L+158,26,6,u);fr(K+8,L+166,22,150,u);fr(K+38,L+150,2,150,a);fr(K+36,L+158,2,150,a);fr(K+34,L+162,2,150,a);fr(K,L+68,38,2,d);fr(K,L+62,2,8,d);fr(K+2,L+56,2,6,d);fr(K+4,L-80,2,136,d);fr(K+36,L+62,2,6,d);fr(K+34,L+56,2,6,d);fr(K+32,L-80,2,136,d);fr(K+4,L+54,30,2,d);fr(K+2,L+62,2,6,p);fr(K+4,L+56,2,6,p);fr(K+6,L-80,2,134,p);fr(K+34,L+62,2,6,p);fr(K+32,L+56,2,6,p);fr(K+30,L-80,2,134,p);fr(K+2,L+62,2,6,p);fr(K+4,L+56,2,6,p);fr(K+6,L+56,26,6,u);fr(K+4,L+62,30,6,u);fr(K+8,L-80,22,134,u);fr(K+38,L-80,2,150,a);fr(K+36,L-80,2,142,a);fr(K+34,L-80,2,136,a)
g=[color(0,100,100),D,'grey','pink','brown',d,color(0,0,100),color(0,100,200),'green'];F=1;l=2;f=1;a=D;fr(0,0,350,300,D);a=(173,216,230);j=20;k=50;n(j,k);j=260;k=50;n(j,k);draw_string('by LilyTheCatgirl',80,55,d,D);draw_string('[shift]',110,150,d,D);fr(102,86,92,47,d);fr(103,87,90,45,m);draw_string('<-   ->',110,90,d,m);fr(135,91,15,15,g[f]);draw_string('jouer',118,110,z,m)
while F==1:
 a=g[f]
 if kd(KEY_LEFT)and f>0 and(l==1):f=f-1;fr(135,91,15,15,g[f]);a=g[f];sleep(0.3);print(a)
 if kd(KEY_RIGHT)and f<len(g)-1 and(l==1):f=f+1;fr(135,91,15,15,g[f]);sleep(0.3);a=g[f];print(a)
 if kd(ku)and l==2:l=1;draw_string('<-   ->',110,90,z,m);fr(135,91,15,15,g[f]);draw_string('jouer',118,110,d,m)
 if kd(KEY_DOWN)and l==1:l=2;draw_string('<-   ->',110,90,d,m);fr(135,91,15,15,g[f]);draw_string('jouer',118,110,z,m)
 if kd(ko)and l==2:F=0
if a==d or a==color(0,0,100)or a==color(0,100,200):h=m
else:h=d
x=50;y=100;I=1;J=0;j=0;k=0;q=250;A=0;r=375;B=0;s=500;C=0;b=0;t=0;c=10;o=0;E=1;H=1;v=0;fr(0,0,350,350,a)
def G(K,L):
 if J-I>0:fr(K,L-10,32,10,a);fr(K,L,8,4,a);fr(K,L+4,6,2,a);fr(K,L+6,2,2,a);fr(K+8,L,4,2,a);fr(K+30,L,2,14,a);fr(K+26,L,4,4,a);fr(K+24,L,2,2,a);fr(K+28,L+4,2,2,a)
 else:fr(K,L+24,32,4,a);fr(K,L+14,2,4,a);fr(K+2,L+16,2,4,a);fr(K+4,L+20,2,4,a);fr(K+6,L+22,4,2,a);fr(K+20,L+22,12,2,a);fr(K+30,L+16,2,4,a);fr(K+28,L+20,2,2,a)
 fr(K+12,L,12,2,d);fr(K+8,L+2,4,2,d);fr(K+4,L+4,2,2,d);fr(K+2,L+6,8,2,d);fr(K,L+8,2,6,d);fr(K+2,L+14,2,2,d);fr(K+4,L+16,6,2,d);fr(K+4,L+18,2,2,d);fr(K+6,L+20,4,2,d);fr(K+10,L+22,10,2,d);fr(K+20,L+20,8,2,d);fr(K+28,L+16,2,4,d);fr(K+20,L+16,8,2,d);fr(K+18,L+18,2,2,d);fr(K+16,L+16,2,2,d);fr(K+18,L+14,2,2,d);fr(K+20,L+12,10,2,d);fr(K+30,L+14,2,2,d);fr(K+28,L+6,2,6,d);fr(K+24,L+6,2,4,d);fr(K+26,L+4,2,2,d);fr(K+24,L+2,2,2,d);fr(K+18,L+2,2,2,d);fr(K+16,L+4,2,6,d);fr(K+18,L+10,2,2,d);fr(K+10,L+8,2,2,d);fr(K+12,L+10,2,4,d);fr(K+10,L+14,2,2,d);fr(K+2,L+12,2,2,w);fr(K+4,L+14,6,2,w);fr(K+10,L+12,2,2,w);fr(K+12,L+4,4,6,w);fr(K+14,L+10,4,6,w);fr(K+12,L+14,2,2,w);fr(K+18,L+12,2,2,w);fr(K+10,L+16,6,6,'orange');fr(K+6,L+18,12,2,'orange');fr(K+16,L+20,4,2,'orange');fr(K+20,L+18,8,2,z);fr(K+18,L+16,2,2,z);fr(K+20,L+14,10,2,z);fr(K+2,L+8,8,4,m);fr(K+4,L+12,6,2,m);fr(K+10,L+10,2,2,m);fr(K+12,L+2,6,2,m)
 fr(K+8,L+4,4,2,m);fr(K+20,L+2,4,10,m);fr(K+18,L+4,2,6,m);fr(K+24,L+4,2,2,m);fr(K+26,L+6,2,6,m);fr(K+24,L+10,4,2,m)
while H==1:
 while E==1:
  sleep(0.01);j=q;k=A;n(j,k);q=q-2
  if q<=-40:q=320;A=randint(-50,80)
  j=r;k=B;n(j,k);r=r-2
  if r<=-40:r=320;B=randint(-50,80)
  j=s;k=C;n(j,k);s=s-2
  if s<=-40:s=320;C=randint(-50,80)
  G(x,y);I=y;y=y+b;c=c-1
  if y>200:t=0;b=-3
  if y<0:t=0;b=3
  if kd(ko)or kd(ku):
   if not y>200 and(not y<0):t=10;b=-3
  if c==0 and t==0:b=b+1;c=3
  if c==0 and t>0:b=b+1;c=3
  if x+26>q and x<q+38 and(y>A+138):E=0
  if x+26>q and x<q+38 and(y<A+68):E=0
  if x+26>r and x<r+38 and(y>B+138):E=0
  if x+26>r and x<r+38 and(y<B+68):E=0
  if x+26>s and x<s+38 and(y>C+138):E=0
  if x+26>s and x<s+38 and(y<C+68):E=0
  J=y
  if x>q-1 and x<q+1:o=o+1
  if x>r-1 and x<r+1:o=o+1
  if x>s-1 and x<s+1:o=o+1
  draw_string(str(o),150,5,h,a)
  if kd(KEY_SHIFT):fr(150,90,15,40,m);fr(170,90,15,40,m);draw_string('[shift]',130,140,m,a);v=1
  if v==1:
   fr(150,90,15,40,m);fr(170,90,15,40,m);draw_string('[shift]',130,140,m,a);sleep(0.3)
   while v==1:
    sleep(0.001)
    if kd(KEY_SHIFT):v=0;sleep(0.2);fr(0,0,350,300,a)
  sleep(0.003)
 c=5;t=0;b=3
 while not y>280:
  n(q,A);n(r,B);n(s,C);G(x,y);draw_string(str(o),150,5,h,a);I=y;c=c-1;y=y+b
  if c==0 and t==0:b=b+1;c=5
  J=y;sleep(0.003)
 x=320;y=0
 for i in range(330):fr(x,y,5,250,h);fr(x+5,y,5,250,a);x=x-1;sleep(0.001)
 draw_string('BRAVO',130,95,h,a);draw_string('by LilyTheCatgirl',92,110,h,a);draw_string('Ton score: '+str(o),100,128,h,a);draw_string('[OK/UP]:rejouer',80,145,h,a);j=10;k=50;n(j,k);j=250;k=50;n(j,k);j=135;k=20;n(j,k)
 while E==0:
  if kd(ko)or kd(ku):fr(0,0,350,250,a);x=50;y=100;I=1;J=0;j=0;k=0;q=200;A=0;r=325;B=0;s=450;C=0;b=0;t=0;c=10;o=0;E=1