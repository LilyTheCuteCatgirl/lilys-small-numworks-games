from kandinsky import*;from ion import*;from time import sleep;from random import randint;x=20;y=190;F=190;O=0;bc=0;be=0;am=0;H=0;ad=2;ar=-13;J=0;B=0;a=0;d=[];E=0;aL=randint(30,50);t=[];q=0;aN=randint(30,50);j=[];v=0;K=randint(30,70);m=[];l=0;D=randint(1,2);p=[];A=0;L=randint(30,50);Q=min(14,10+a//3);Y=min(14,10+a//3);U=min(14,10+a//3);ag=min(14,10+a//3);T=min(14,5+a//3);aY=[(11,-12,8,1),(10,-11,10,1),(13,-10,7,1),(10,-10,2,1),(10,-9,10,3),(10,-6,5,1),(10,-5,8,1),(9,-4,5,1),(0,-4,1,1),(7,-3,7,1),(0,-3,1,1),(6,-2,10,1),(0,-2,2,1),(15,-1,1,1),(5,-1,9,1),(0,-1,3,1),(0,0,14,1),(1,1,12,1),(2,2,11,1),(3,3,9,1),(4,4,7,1),(5,5,3,1),(9,5,2,1),(6,6,2,1),(9,6,1,1),(6,7,1,1),(9,7,1,1),(6,8,2,1),(9,8,2,1)]
aF=aY[:21]+[(5,5,4,1),(10,5,1,1),(6,6,2,1),(10,6,3,1),(6,7,1,1),(6,8,2,1)];aE=aY[:21]+[(5,5,2,1),(9,5,2,1),(6,6,2,1),(9,6,1,1),(9,7,1,1),(9,8,2,1)];aU=aY[:21]+[(3,5,11,6)]
aj=[(0,-3,1,1),(18,-3,8,1),(0,-2,3,1),(7,-2,8,1),(17,-2,10,1),(0,-1,19,1),(20,-1,7,1),(1,0,26,1),(2,1,25,1),(3,2,24,1),(4,3,18,1),(5,4,11,1),(18,4,7,1),(6,5,5,1),(14,5,1,1),(5,6,3,1),(10,6,2,1),(14,6,2,1),(5,7,2,1),(5,8,1,1),(5,9,2,1)];ai=aj[:15]+[(5,6,1,1),(8,6,3,1),(14,6,2,1),(5,7,2,1),(8,7,2,1),(8,8,1,1),(8,9,2,1)];V=aj+[(5,6,1,1),(8,6,3,1),(14,6,2,1),(5,7,2,1),(8,7,2,1),(8,8,1,1),(8,9,2,1)]
au=[(33,-36,24,3),(30,-33,30,3),(39,-30,21,3),(30,-30,6,3),(30,-27,30,9),(30,-18,15,3),(30,-15,24,3),(27,-12,15,3),(0,-12,3,3),(21,-9,21,3),(0,-9,3,3),(18,-6,30,3),(0,-6,6,3),(45,-3,3,3),(15,-3,27,3),(0,-3,9,3),(0,0,42,3),(3,3,36,3),(6,6,33,3),(9,9,27,3),(12,12,21,3),(15,15,9,3),(27,15,6,3),(15,18,6,3),(30,18,3,3),(15,21,3,3),(30,21,3,3),(15,24,6,3),(30,24,6,3)];S=[(-15,2,4,7),(-19,0,11,1),(-20,-1,13,1),(-20,-8,3,7),(-15,-13,4,15),(-9,-10,3,9),(-19,-9,1,1),(-14,-14,2,1),(-8,-11,1,1)];at=[(0,13,2,1),(10,13,35,1),(1,12,2,1),(4,12,2,1),(9,12,1,1),(44,12,1,1),(5,11,1,1),(43,11,1,1),(5,10,1,1),(41,10,3,1),(5,9,2,1),(41,9,1,1),(6,8,8,1),(38,8,4,1),(13,7,5,1),(30,7,1,1),(38,7,1,1),(17,6,1,1),(31,6,8,1),(17,5,1,1),(31,5,1,1),(17,4,3,1),(30,4,2,1),(19,3,2,1),(30,3,2,1),(20,2,6,1),(28,2,3,1),(25,1,4,1)]
av=[(0,5,1,1),(1,5,5,1),(1,4,2,1),(3,3,3,1),(6,4,1,1),(7,5,5,1),(12,6,2,1),(12,5,5,1),(14,6,3,1),(17,5,2,1),(20,5,2,1)];W=[(1,5,7,1),(0,5,1,1),(1,5,5,1),(1,4,2,1),(3,3,3,1),(6,4,1,1),(7,5,5,1),(12,6,2,1),(12,5,5,1),(14,6,3,1),(17,5,2,1),(20,5,2,1)];aB=[(4,0,2,1),(3,1,3,1),(2,2,5,1),(1,3,6,1),(0,4,14,1),(6,5,9,1),(7,6,14,1),(8,7,10,1),(8,8,12,1),(8,9,9,1),(8,10,4,1),(8,11,3,1),(8,12,2,1),(8,13,2,1),(8,14,1,1)];an=[(7,-3,1,1),(7,-2,2,1),(7,-1,3,1),(8,0,3,1),(8,1,4,1),(8,2,5,1),(8,3,6,1),(4,0,2,1),(3,1,3,1),(2,2,5,1),(1,3,6,1),(0,4,14,1),(6,5,9,1),(7,6,14,1),(8,7,10,1),(9,8,11,1),(10,9,7,1)];X=aB+[(7,-3,1,1),(7,-2,2,1),(7,-1,3,1),(8,0,3,1),(8,1,4,1),(8,2,5,1),(8,3,6,1),(10,9,7,1)]
aC=[(0,0,6,2),(4,2,8,2),(6,4,8,2),(8,6,8,2),(10,8,8,4),(12,12,8,4),(12,12,8,14),(10,24,8,4),(8,28,8,2),(6,30,8,2),(4,32,8,2),(0,34,6,2)];aG=[(3,0,1,1),(0,1,1,1),(3,1,1,1),(6,1,1,1),(3,2,1,1),(2,3,3,1),(0,4,8,1),(2,5,3,1),(3,6,1,1),(0,7,1,1),(3,7,1,1),(6,7,1,1),(3,8,1,1)];aw=[(3,0,1,1),(3,1,1,1),(3,2,1,1),(2,3,3,1),(0,4,8,1),(2,5,3,1),(3,6,1,1),(3,7,1,1),(3,8,1,1)];C=(83,83,83);ab=(218,218,218);b=(255,255,255)
def k(bi,bj,bf,bk=C):
 for (bg,bh,w,h) in bf:fill_rect(bi+bg,bj+bh,w,h,C)
def M(bi,bj,bf):
 for (bg,bh,w,h) in bf:fill_rect(bi+bg,bj+bh,w,h,ab)
def R(bi,bj,bf):
 for (bg,bh,w,h) in bf:fill_rect(bi+bg,bj+bh,w,h,b)
def a3(bf,bg):k(bf,bg,aY)
def aP(bf,bg):k(bf,bg,aF)
def aO(bf,bg):k(bf,bg,aE)
def aX(bf,bg):R(bf,bg,aU)
def aJ(bf,bg):k(bf,bg,aj)
def aI(bf,bg):k(bf,bg,ai)
def ao(bf,bg):R(bf,bg,V)
def aV(bf,bg):k(bf,bg,au,(83,83,83))
def a2(bf,bg):k(bf,bg,S)
def aW(bf,bg):R(bf,bg,S)
def a5(bf,bg):M(bf,bg,at)
def aZ(bf,bg):fill_rect(bf,bg,48,14,b)
def bd(bf,bg):fill_rect(bf,bg,2,1,C)
def a8(bf,bg):fill_rect(bf,197,2,7,b)
def a6(bf,bg):k(bf,bg,av)
def a0(bf,bg):R(bf,bg,W)
def a9(bf,bg):k(bf,bg,aB)
def a1(bf,bg):k(bf,bg,an)
def a4(bh,bi):
 for (bf,bg,w,h) in X:fill_rect(bh+bf,bi+bg,w,h,b)
def ba(bf,bg):M(bf,bg,aC)
def I(bf,bg):M(bf,bg,aG)
def G(bf,bg):M(bf,bg,aw)
def aM(bf,bg,bh,bi):return bh-20<bf+14 and bh-8>bf and(bi-20<bg)and(bi>bg-20)
def ay(bf,bg,bh,bi):return bh-20<bf+26 and bh-8>bf and(bi-20<bg)and(bi>bg-12)
def ap(bh,bi,bf,bg):return bh<bf+14 and bh+30>bf and(bi<bg+14)and(bi+20>bg)
def aS():
 global bc,O,ae;global x,y,H,F;global d,t,j,m,p;global E,q,v,l,A;global aL,aN,K,D,L;global B,a;bg=(83,83,83);bh=(218,218,218);bf=(255,255,255)
 if bc<=O:bc=O
 draw_string(str(bc),x+20,10,bg,bf);ae=True;draw_string('PERDU',135,100,bg,bf);draw_string('Appuie sur OK pour recommencer',10,120,bg,bf);print('Ton score est de :',O);print('et ton meilleur score de :',bc,'!');print('Encore :',bc-O+1,'pt(s) de plus pour depasser ton recort !');x=20;y=F;H=0;d=[];j=[];m=[];p=[];t=[];E=0;q=0;v=0;l=0;A=0;B=0;a=0;O=0
while True:
 sleep(0.1);fill_rect(0,0,320,222,(255,255,255));draw_string('CHROME DINO',100,50,(83,83,83),(255,255,255));draw_string('Appuie sur OK pour jouer',40,70,(83,83,83),(255,255,255));draw_string('commandes:(shift)',10,200,(83,83,83),(255,255,255));draw_string('V 1.00',250,200,(83,83,83),(255,255,255));aV(x+100,y-40);fill_rect(0,195,320,1,(83,83,83))
 while not keydown(KEY_OK)and(not keydown(KEY_SHIFT)):sleep(0.05)
 if keydown(KEY_SHIFT):fill_rect(0,0,320,222,(255,255,255));draw_string('COMMANDES :',110,30,(83,83,83),(255,255,255));draw_string('Sauter :    (OK)',80,80,(83,83,83),(255,255,255));draw_string("S'acroupir : (V)",80,110,(83,83,83),(255,255,255));draw_string('Pause :  (sprm.)',80,140,(83,83,83),(255,255,255));draw_string('Appuie sur OK pour jouer',40,165,(83,83,83),(255,255,255));draw_string('propriété intellectuelle:(exe)',10,200,(83,83,83),(255,255,255));fill_rect(0,195,320,1,(83,83,83))
 while not keydown(KEY_OK)and(not keydown(KEY_EXE)):
  sleep(0.05)
  if keydown(KEY_EXE):fill_rect(0,0,320,222,(255,255,255));draw_string('Propriété intelectuelle :',45,30,(83,83,83),(255,255,255));draw_string('Copyright(c) 2026 LilyTheCatgirl.',0,90,(83,83,83),(255,255,255));draw_string('Tous droits réservés. ',62,120,(83,83,83),(255,255,255))
 while not keydown(KEY_OK):sleep(0.05)
 if keydown(KEY_OK):fill_rect(0,0,320,222,b);ae=False
 Z=-1
 while not ae:
  draw_string('HI',x-10,10,C,b);draw_string(str(bc),x+20,10,C,b);draw_string(str(O),x+250,10,C,b);fill_rect(0,195,320,1,C);O+=1;az=O//300%2
  if az==0:C=(83,83,83);ab=(218,218,218);b=(255,255,255);aR=False
  else:C=(172,172,172);ab=(37,37,37);b=(0,0,0);aR=True
  if az!=Z:fill_rect(0,0,320,222,b);Z=az
  if aR:ba(50,90);I(100,100);G(20,110);I(60,40);G(140,20);I(130,75);G(60,140);I(260,120);G(180,90);I(220,70);G(280,60);I(250,20);G(160,110)
  ah=130+a*4+randint(0,60);af=max(20,E//2-a);aD=af+40+randint(0,20);N=randint(1,4)
  if len(d)<3 and E>=randint(af,aD)and(N==1):
   if len(d)==0 or d[-1]<350-ah:
    aH=randint(2,3);ax=randint(1,6)
    if ax==6:
     aQ=0
     for g in range(aH):aQ+=20;d.append(350+int(aQ))
    else:d.append(350);E=0
  if l>=D:aA=randint(197,203);m.append([320,aA]);l=0;D=randint(1,3)
  aK=260+a*6;P=max(40,q//2);aa=P+40;N=randint(1,7)
  if len(t)<1 and len(d)<100 and(q>=randint(P,aa))and(O>300)and(N==2):d.append(650);aq=randint(150,180);t.append([400,aq]);q=0
  if len(j)<3 and v>=K:aT=randint(50,120);j.append([320,aT]);v=0;K=randint(20-a,60-a)
  if len(m)<5 and l>=D:aA=randint(197,203);m.append([320,aA]);l=0;D=randint(1,3)
  if len(p)<2 and A>=L:p.append(500);A=0;L=randint(20-a,60-a)
  aX(x,y);ao(x,y);y+=H
  if y<F:H+=ad
  else:y=F;H=0
  if keydown(KEY_DOWN):
   ad+=7;ac=J%15
   if ac%5<2:aJ(x,y)
   else:aI(x,y)
  else:ad=2
  if y<F and(not keydown(KEY_DOWN)):a3(x,y)
  elif not keydown(KEY_DOWN):
   ac=J%15
   if ac%5<2:aP(x,y)
   else:aO(x,y)
  for o in range(len(j)):aZ(j[o][0],j[o][1]);j[o][0]-=T;a5(j[o][0],j[o][1])
  for u in range(len(m)):a8(m[u][0],m[u][1]);m[u][0]-=ag;bd(m[u][0],m[u][1])
  for r in range(len(p)):a0(p[r],F);p[r]-=U;a6(p[r],F)
  for i in range(len(d)):
   aW(d[i],F);d[i]-=Q;a2(d[i],F);ak=d[i];al=F
   if not keydown(KEY_DOWN):
    if aM(x,y,ak,al):
     aS()
     while not keydown(KEY_OK):sleep(0.1)
     break
   elif ay(x,y,ak,al):
    aS()
    while not keydown(KEY_OK):sleep(0.1)
    break
  for f in range(len(t)):
   a7,bb=t[f];a4(a7,bb);t[f][0]-=Y;a7=t[f][0];ac=J%10
   if ac%5<2:a9(a7,bb)
   else:a1(a7,bb)
   if ap(x,y,a7,bb):
    aS()
    while not keydown(KEY_OK):sleep(0.1)
    break
  d=[c for c in d if c>-10];j=[n for n in j if n[0]>-50];m=[s for s in m if s[0]>-10];p=[r for r in p if r>-20];t=[z for z in t if z[0]>-30];E+=randint(1,4+a//3);v+=1;l+=1;A+=1;q+=1;B+=1;J+=1
  if B%60==0:a+=1;Q=min(14,10+a//3);Y=min(14,10+a//3);U=min(14,10+a//3);ag=min(14,10+a//3);T=min(14,5+a//3)
  sleep(0.03)
  if keydown(KEY_OK)and y==F and(not keydown(KEY_DOWN)):H=ar
  if keydown(KEY_BACKSPACE)and am==0:
   be=B;am=1;draw_string('pause',133,110,C,b);sleep(0.5)
   while not keydown(KEY_BACKSPACE)and am==1:sleep(0.1)
   fill_rect(0,0,320,222,b)
  if be+20<B:am=0