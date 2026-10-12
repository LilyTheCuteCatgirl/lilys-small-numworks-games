def z(s,h=1):
 r=[];i=0
 while i<len(s):
  x=ord(s[i])-68;y=ord(s[i+1])-68;w=ord(s[i+2])-32;i+=3;t=h
  if w>=48:w-=48;t=ord(s[i])-32;i+=1
  r.append((x,y,w,t))
 return r
from kandinsky import*;c=(83,83,83);f=(255,255,255);e=(218,218,218);from ion import*;from time import sleep;from random import randint;x=20;y=190;F=190;O=0;bc=0;be=0;am=0;H=0;ad=2;ar=-13;J=0;B=0;a=0;d=[];E=0;aL=randint(30,50);t=[];q=0;aN=randint(30,50);j=[];v=0;K=randint(30,70);m=[];l=0;D=randint(1,2);p=[];A=0;L=randint(30,50);Q=min(14,10+a//3);Y=min(14,10+a//3);U=min(14,10+a//3);ag=min(14,10+a//3);T=min(14,5+a//3);aY=z('O8(N9*Q:\'N:"N;Z#N>%N?(M@%D@!KA\'DA!JB*DB"SC!IC)DC#DD.EE,FF+GG)HH\'II#MI"JJ"MJ!JK!MK!JL"ML"')
aF=aY[:21]+[(5,5,4,1),(10,5,1,1),(6,6,2,1),(10,6,3,1),(6,7,1,1),(6,8,2,1)];aE=aY[:21]+[(5,5,2,1),(9,5,2,1),(6,6,2,1),(9,6,1,1),(9,7,1,1),(9,8,2,1)];aU=aY[:21]+[(3,5,11,6)]
aj=z('DA!VA(DB#KB(UB*DC3XC\'ED:FE9GF8HG2IH+VH\'JI%RI!IJ#NJ"RJ"IK"IL!IM"');V=aj+[(5,6,1,1),(8,6,3,1),(14,6,2,1),(5,7,2,1),(8,7,2,1),(8,8,1,1),(8,9,2,1)];ai=V[:15]+V[21:]
au=[(i*3,j*3,k*3,l*3)for i,j,k,l in aY[:23]]+z('SV&bV#SY#bY#S\\&b\\&',3);S=z("5FT'1D+0C-0<S'57T/;:S)1;!66\"<9!");at=z('DQ"NQCEP"HP"MP!pP!IO!oO!IN!mN#IM"mM!JL(jL$QK%bK!jK!UJ!cJ(UI!cI!UH#bH"WG"bG"XF&`F#]E$')
av=z('DI!EI%EH"GG#JH!KI%PJ"PI%RJ#UI"XI"');W=[(1,5,7,1)]+av;aB=z('HD"GE#FF%EG&DH.JI)KJ.LK*LL,LM)LN$LO#LP"LQ"LR!');an=z('KA!KB"KC#LD#LE$LF%LG&HD"GE#FF%EG&DH.JI)KJ.LK*ML+NM\'');X=aB+[(7,-3,1,1),(7,-2,2,1),(7,-1,3,1),(8,0,3,1),(8,1,4,1),(8,2,5,1),(8,3,6,1),(10,9,7,1)]
aC=z('DD&HF(JH(LJ(NLX$PPX$PPX.N\\X$L`(Jb(Hd(Df&',2);aG=z('GD!DE!GE!JE!GF!FG#DH(FI#GJ!DK!GK!JK!GL!');aw=z('GD!GE!GF!FG#DH(FI#GJ!GK!GL!');C=c;ab=e;b=f
def k(bi,bj,bf,bk):
 for (bg,bh,w,h) in bf:fill_rect(bi+bg,bj+bh,w,h,bk)
def aM(bf,bg,bh,bi):return bh-20<bf+14 and bh-8>bf and(bi-20<bg)and(bi>bg-20)
def ay(bf,bg,bh,bi):return bh-20<bf+26 and bh-8>bf and(bi-20<bg)and(bi>bg-12)
def ap(bh,bi,bf,bg):return bh<bf+14 and bh+30>bf and(bi<bg+14)and(bi+20>bg)
def aS():
 global bc,O,ae;global x,y,H,F;global d,t,j,m,p;global E,q,v,l,A;global aL,aN,K,D,L;global B,a;bg=c;bh=e;bf=f
 if bc<=O:bc=O
 draw_string(str(bc),x+20,10,bg,bf);ae=True;draw_string('PERDU',135,100,bg,bf);draw_string('Appuie sur OK pour recommencer',10,120,bg,bf);print('Ton score est de :',O);print('et ton meilleur score de :',bc,'!');print('Encore :',bc-O+1,'pt(s) de plus pour depasser ton recort !');x=20;y=F;H=0;d=[];j=[];m=[];p=[];t=[];E=0;q=0;v=0;l=0;A=0;B=0;a=0;O=0
while True:
 sleep(0.1);fill_rect(0,0,320,222,f);draw_string('CHROME DINO',100,50,c,f);draw_string('Appuie sur OK pour jouer',40,70,c,f);draw_string('commandes:(shift)',10,200,c,f);draw_string('V 1.00',250,200,c,f);k(x+100,y-40,au,C);fill_rect(0,195,320,1,c)
 while not keydown(KEY_OK)and(not keydown(KEY_SHIFT)):sleep(0.05)
 if keydown(KEY_SHIFT):fill_rect(0,0,320,222,f);draw_string('COMMANDES :',110,30,c,f);draw_string('Sauter :    (OK)',80,80,c,f);draw_string("S'acroupir : (V)",80,110,c,f);draw_string('Pause :  (sprm.)',80,140,c,f);draw_string('Appuie sur OK pour jouer',40,165,c,f);draw_string('propriété intellectuelle:(exe)',10,200,c,f);fill_rect(0,195,320,1,c)
 while not keydown(KEY_OK)and(not keydown(KEY_EXE)):
  sleep(0.05)
  if keydown(KEY_EXE):fill_rect(0,0,320,222,f);draw_string('Propriété intelectuelle :',45,30,c,f);draw_string('Copyright(c) 2026 Diégo KHELLADI.',0,90,c,f);draw_string('Tous droits réservés. ',62,120,c,f)
 while not keydown(KEY_OK):sleep(0.05)
 if keydown(KEY_OK):fill_rect(0,0,320,222,b);ae=False
 Z=-1
 while not ae:
  draw_string('HI',x-10,10,C,b);draw_string(str(bc),x+20,10,C,b);draw_string(str(O),x+250,10,C,b);fill_rect(0,195,320,1,C);O+=1;az=O//300%2
  if az==0:C=c;ab=e;b=f;aR=False
  else:C=(172,172,172);ab=(37,37,37);b=(0,0,0);aR=True
  if az!=Z:fill_rect(0,0,320,222,b);Z=az
  if aR:k(50,90,aC,ab);k(100,100,aG,ab);k(20,110,aw,ab);k(60,40,aG,ab);k(140,20,aw,ab);k(130,75,aG,ab);k(60,140,aw,ab);k(260,120,aG,ab);k(180,90,aw,ab);k(220,70,aG,ab);k(280,60,aw,ab);k(250,20,aG,ab);k(160,110,aw,ab)
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
  k(x,y,aU,b);k(x,y,V,b);y+=H
  if y<F:H+=ad
  else:y=F;H=0
  if keydown(KEY_DOWN):
   ad+=7;ac=J%15
   if ac%5<2:k(x,y,aj,C)
   else:k(x,y,ai,C)
  else:ad=2
  if y<F and(not keydown(KEY_DOWN)):k(x,y,aY,C)
  elif not keydown(KEY_DOWN):
   ac=J%15
   if ac%5<2:k(x,y,aF,C)
   else:k(x,y,aE,C)
  for o in range(len(j)):fill_rect(j[o][0],j[o][1],48,14,b);j[o][0]-=T;k(j[o][0],j[o][1],at,ab)
  for u in range(len(m)):fill_rect(m[u][0],197,2,7,b);m[u][0]-=ag;fill_rect(m[u][0],m[u][1],2,1,C)
  for r in range(len(p)):k(p[r],F,W,b);p[r]-=U;k(p[r],F,av,C)
  for i in range(len(d)):
   k(d[i],F,S,b);d[i]-=Q;k(d[i],F,S,C);ak=d[i];al=F
   if not keydown(KEY_DOWN):
    if aM(x,y,ak,al):
     aS()
     while not keydown(KEY_OK):sleep(0.1)
     break
   elif ay(x,y,ak,al):
    aS()
    while not keydown(KEY_OK):sleep(0.1)
    break
  for h in range(len(t)):
   a7,bb=t[h];k(a7,bb,X,b);t[h][0]-=Y;a7=t[h][0];ac=J%10
   if ac%5<2:k(a7,bb,aB,C)
   else:k(a7,bb,an,C)
   if ap(x,y,a7,bb):
    aS()
    while not keydown(KEY_OK):sleep(0.1)
    break
  d=[g for g in d if g>-10];j=[n for n in j if n[0]>-50];m=[s for s in m if s[0]>-10];p=[r for r in p if r>-20];t=[g for g in t if g[0]>-30];E+=randint(1,4+a//3);v+=1;l+=1;A+=1;q+=1;B+=1;J+=1
  if B%60==0:a+=1;Q=min(14,10+a//3);Y=min(14,10+a//3);U=min(14,10+a//3);ag=min(14,10+a//3);T=min(14,5+a//3)
  sleep(0.03)
  if keydown(KEY_OK)and y==F and(not keydown(KEY_DOWN)):H=ar
  if keydown(KEY_BACKSPACE)and am==0:
   be=B;am=1;draw_string('pause',133,110,C,b);sleep(0.5)
   while not keydown(KEY_BACKSPACE)and am==1:sleep(0.1)
   fill_rect(0,0,320,222,b)
  if be+20<B:am=0
