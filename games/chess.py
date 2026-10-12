from kandinsky import*;from ion import keydown;from time import sleep;from random import randint;from math import*
def Y(s):return[[ord(c)-65 for c in ae]for ae in s.split('_')]
aa=Y('JE_IG_HI_HI_HI_HI_IG_JE_A_A_JE_IG_IG_HI_GK_EO_CS');ab=Y('CDCDCDCD_CDCDCDCD_CS_CS_DQ_DQ_EO_EO_FM_FM_FM_FM_FM_FFCF_EFBCBF_DFBEBF_CGBCBBBG_CGBEBG');P=Y('KC_JE_IE_IDCB_HEBD_HI_IG_IG_JE_KC_A_IG_JE_IG_IG_HI_FFCF_DGEG_CFIF');Q=Y('KC_IF_HI_GK_GL_FDBJ_EP_DQ_CS_CHCJ_CFDK_DDDL_IM_HN_GN_EP_DR_DR');Z=Y('KC_JE_EDDCDD_DGBCBG_CS_CS_CECGCE_CDEEED_DCEEEC_DDECED_DEDCDE_EECCCE_FM_GK_GK_FM_EO_CS');U=Y('JE_DDCGCD_CFBGBF_CFBGBF_CFCECF_DDECED_EBEEEB_ECDEDC_EO_FM_FM_GK_GK_GK_FM_DQ_CS_CS');g=[None,aa,Q,P,ab,U,Z]
def b():ae=[[4,1],[2,1],[3,1],[5,1],[6,1],[3,1],[2,1],[4,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[4,2],[2,2],[3,2],[6,2],[5,2],[3,2],[2,2],[4,2]];return ae
ad=[-50,-40,-30,-20,-10,-5,0,5,10,15,20,25,30,40,50]
def W(s):return[ad[ord(c)-65]for c in s]
J=W('GGGGGGGGOOOOOOOOIIKMMKIIHHILLIHHGGGKKGGGHFEGGEFHHIIDDIIHGGGGGGGG');A=W('ABCCCCBABDGGGGDBCGIJJIGCCHJKKJHCCGJKKJGCCHIJJIHCBDGHHGDBABCCCCBA');z=W('DEEEEEEDEGGGGGGEEGHIIHGEEHHIIHHEEGIIIIGEEIIIIIIEEHGGGGHEDEEEEEED');K=W('GGGGGGGGHIIIIIIHFGGGGGGFFGGGGGGFFGGGGGGFFGGGGGGFFGGGGGGFGGGHHGGG');G=W('DEEFFEEDEGGGGGGEEGHHHHGEFGHHHHGFGGHHHHGFEHHHHHGEEGHGGGGEDEEFFEED');w=W('CBBAABBCCBBAABBCCBBAABBCCBBAABBCDCCBBCCDEDDDDDDEKKGGGGKKKMIGGIMK');v=W('ABCDDCBACDEGGEDCCEKMMKECCEMNNMECCEMNNMECCEKMMKECCCGGGGCCACCCCCCA')
def o(af,ae,x,y,aj):
 if af is not None:
  am=y
  for ak in af:
   ag=False;al=x
   for ah in ak:
    if not ag:al+=ah*aj;ag=True
    else:fill_rect(al,am,ah*aj,aj,ae);al+=ah*aj;ag=False
   am+=aj
def C(ae):
 aj=(210,179,139);ak=(181,137,98);fill_rect(0,0,320,240,(30,30,30));fill_rect(4,4,216,216,(255,255,255));fill_rect(280,5,35,210,(0,200,0))
 for y in range(8):
  for x in range(8):ag=aj if(x+y)%2==0 else ak;fill_rect(22+22*x,22+22*y,22,22,ag)
 al='abcdefgh'
 for i in range(8):draw_string(str(8-i),5,25+22*i);draw_string(al[i],28+22*i,200)
 for y in range(8):
  for x in range(8):ah,af=ae[y*8+x];o(g[ah],(255-af%2*255,255-af%2*255,255-af%2*255),22+22*x,24+22*y,1)
def T(x,y,af,ae):
 ag=[];ah=1 if af==1 else-1
 if y!=int(3.5+3.5*ah):
  if ae[(y+ah)*8+x][0]==0:
   ag.append([(x,y),(x,y+ah)])
   if ae[(y+2*ah)*8+x][0]==0 and(y==1 or y==6):ag.append([(x,y),(x,y+2*ah)])
  for al in [-1,1]:
   aj,ak=(x+al,y+ah)
   if 0<=aj<8 and 0<=ak<8:
    if ae[ak*8+aj][1]==3-af:ag.append([(x,y),(aj,ak)])
 return ag
def D(x,y,af,ae):
 ag=[]
 for (ak,al) in [(1,0),(-1,0),(0,1),(0,-1)]:
  ah,aj=(x,y)
  while True:
   ah+=ak;aj+=al
   if 0<=ah<8 and 0<=aj<8:
    if ae[aj*8+ah][0]==0:ag.append([(x,y),(ah,aj)])
    elif ae[aj*8+ah][1]!=af:ag.append([(x,y),(ah,aj)]);break
    else:break
   else:break
 return ag
def O(x,y,af,ae):
 ag=[];ak=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
 for (al,am) in ak:
  ah,aj=(x+al,y+am)
  if 0<=ah<8 and 0<=aj<8:
   if ae[aj*8+ah][0]==0 or ae[aj*8+ah][1]!=af:ag.append([(x,y),(ah,aj)])
 return ag
def t(x,y,af,ae):
 ag=[]
 for (ak,al) in [(1,1),(-1,1),(1,-1),(-1,-1)]:
  ah,aj=(x,y)
  while True:
   ah+=ak;aj+=al
   if 0<=ah<8 and 0<=aj<8:
    if ae[aj*8+ah][0]==0:ag.append([(x,y),(ah,aj)])
    elif ae[aj*8+ah][1]!=af:ag.append([(x,y),(ah,aj)]);break
    else:break
   else:break
 return ag
def R(x,y,af,ae):return D(x,y,af,ae)+t(x,y,af,ae)
def S(x,y,af,ae):
 ag=[];am=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
 for (ak,al) in am:
  ah,aj=(x+ak,y+al)
  if 0<=ah<8 and 0<=aj<8:
   if ae[ah+aj*8][1]!=af:ag.append([(x,y),(ah,aj)])
 return ag
def h(x,y,ae):
 ag,af=ae[y*8+x]
 if ag==1:return T(x,y,af,ae)
 elif ag==2:return O(x,y,af,ae)
 elif ag==3:return t(x,y,af,ae)
 elif ag==4:return D(x,y,af,ae)
 elif ag==5:return R(x,y,af,ae)
 elif ag==6:return S(x,y,af,ae)
 return[]
def k(ae,af,d,c):
 if (ae+af)%2==0:ag=(181,137,98)
 else:ag=(210,179,139)
 fill_rect(22+22*(ae-d[0]),22+22*(af-d[1]),22,2,ag);fill_rect(22+22*(ae-d[0]),42+22*(af-d[1]),22,2,ag);fill_rect(22+22*(ae-d[0]),22+22*(af-d[1]),2,22,ag);fill_rect(42+22*(ae-d[0]),22+22*(af-d[1]),2,22,ag);fill_rect(22+22*ae,22+22*af,22,2,c);fill_rect(22+22*ae,42+22*af,22,2,c);fill_rect(22+22*ae,22+22*af,2,22,c);fill_rect(42+22*ae,22+22*af,2,22,c)
def q(x,y,am,al,ae,af,ak):
 for ag in h(am,al,ae):
  if (ag[1][0]+ag[1][1])%2==0:aj=(210,179,139)
  else:aj=(181,137,98)
  if ae[ag[1][0]+ag[1][1]*8][0]!=0:fill_rect(22+ag[1][0]*22,22+ag[1][1]*22,22,2,aj);fill_rect(22+ag[1][0]*22,42+ag[1][1]*22,22,2,aj);fill_rect(22+ag[1][0]*22,22+ag[1][1]*22,2,22,aj);fill_rect(42+ag[1][0]*22,22+ag[1][1]*22,2,22,aj)
  else:fill_rect(28+ag[1][0]*22,28+ag[1][1]*22,10,10,aj)
 if ae[x+y*8][1]==ak:
  if af==x+y*8:ah=(0,0,200)
  else:ah=(0,200,0)
  for ag in h(x,y,ae):
   if ae[ag[1][0]+ag[1][1]*8][0]!=0:fill_rect(22+ag[1][0]*22,22+ag[1][1]*22,22,2,ah);fill_rect(22+ag[1][0]*22,42+ag[1][1]*22,22,2,ah);fill_rect(22+ag[1][0]*22,22+ag[1][1]*22,2,22,ah);fill_rect(42+ag[1][0]*22,22+ag[1][1]*22,2,22,ah)
   else:fill_rect(28+ag[1][0]*22,28+ag[1][1]*22,10,10,(100,100,100))
 return(x,y)
def H(x,y):
 if (x+y)%2==0:c=(210,179,139)
 else:c=(181,137,98)
 return c
def n(ae,ah,aj,ak,ag,af):
 if ae[ah+8*aj]==[1,1]and ag==7:p=[5,1]
 elif ae[ah+8*aj]==[1,2]and ag==0:p=[5,2]
 else:p=ae[ah+aj*8]
 fill_rect(22+22*ah,22+22*aj,22,22,H(ah,aj));fill_rect(22+22*ak,22+22*ag,22,22,H(ak,ag));c=255-ae[ah+8*aj][1]%2*255;o(af[p[0]],(c,c,c),22+22*ak,24+22*ag,1);ae[ak+8*ag]=p;ae[ah+8*aj]=[0,0];return ae
def j(ae):
 ag=0;aj=0;af=0;ah=0;al=0;an=0;aq=False;ar=False;ao=-1;ap=-1
 for i in range(64):
  if ae[i]==[1,1]:af+=100;ag+=J[63-i]
  elif ae[i]==[1,2]:ah+=100;aj+=J[i]
  elif ae[i]==[2,1]:af+=320;ag+=A[63-i];al+=1
  elif ae[i]==[2,2]:ah+=320;aj+=A[i];an+=1
  elif ae[i]==[3,1]:af+=330;ag+=z[63-i];al+=1
  elif ae[i]==[3,2]:ah+=330;aj+=z[i];an+=1
  elif ae[i]==[4,1]:af+=500;ag+=K[63-i];al+=1
  elif ae[i]==[4,2]:ah+=500;aj+=K[i];an+=1
  elif ae[i]==[5,1]:af+=900;ag+=G[63-i];aq=True
  elif ae[i]==[5,2]:ah+=900;aj+=G[i];ar=True
  elif ae[i]==[6,1]:ao=i
  elif ae[i]==[6,2]:ap=i
 if aq==False and ar==False or(al<2 and an<2):ak='eg'
 else:ak='mg'
 if ao!=-1:af+=5000;ag+=w[63-ao]if ak=='mg'else v[63-ao]
 if ap!=-1:ah+=5000;aj+=w[ap]if ak=='mg'else v[ap]
 am=ah-af+(aj-ag);return am
def r(ae):fill_rect(290,10,15,200,(0,0,0));fill_rect(290,int(110-ae/10),15,int(200-(100-ae/10)),(255,255,255));fill_rect(290,109,15,2,(255,0,0));fill_rect(222,4,56,40,(255,255,255));draw_string('eval:',224,7);draw_string(str(ae/100),224,25)
def l(ae,af):
 L=[]
 for i in range(64):
  if ae[i][1]==af:
   a=h(i%8,i//8,ae)
   if a!=[]and a!=None:
    for i in range(len(a)):L.append(a[i])
 return L
def E(ae,af):
 (aj,ak),(al,ah)=af
 if ae[aj+8*ak]==[1,1]and ah==7:ae[al+8*ah]=[5,1];ag=[1,1]
 elif ae[aj+8*ak]==[1,2]and ah==0:ae[al+8*ah]=[5,2];ag=[1,2]
 else:ag=ae[al+8*ah];ae[al+8*ah]=ae[aj+8*ak]
 ae[aj+8*ak]=[0,0];return(ag,ae)
def F(ae,af,c):
 (al,am),(ak,aj)=af
 if c==[1,1]and aj==7:ae[am*8+al]=[1,1];ae[aj*8+ak]=[0,0]
 elif c==[1,2]and aj==0:ae[am*8+al]=[1,2];ae[aj*8+ak]=[0,0]
 else:ah,ag=ae[aj*8+ak];ae[am*8+al]=[ah,ag];ae[aj*8+ak]=c
 return ae
def B(ae,ao,am,an,ap):
 if ao==0:return(j(ae),None)
 ah=None
 if ap:
  ar=l(ae,2);ak=-9999
  for af in ar:
   ag,ae=E(ae,af);aj=B(ae,ao-1,am,an,False)[0];ae=F(ae,af,ag)
   if aj>ak:ak=aj;ah=af;am=max(am,aj)
   if an<=am:break
  return(ak,ah)
 else:
  aq=l(ae,1);al=9999
  for af in aq:
   ag,ae=E(ae,af);aj=B(ae,ao-1,am,an,True)[0];ae=F(ae,af,ag)
   if aj<al:al=aj;ah=af;an=min(an,aj)
   if an<=am:break
  return(al,ah)
def f(ag,af):ae=B(ag,af,-9999,9999,False)[1];return ae
def N(ae):
 if [6,1]in ae and[6,2]in ae:return False
 return True
def ac():fill_rect(0,0,320,240,(210,179,139));fill_rect(0,50,320,130,(181,137,98));fill_rect(90,0,130,240,(181,137,98))
def u(x,y,d,c):
 if keydown(0)and x>0:x-=1;d=(-1,0);c=False
 elif keydown(3)and x<7:x+=1;d=(+1,0);c=False
 elif keydown(1)and y>0:y-=1;d=(0,-1);c=False
 elif keydown(2)and y<7:y+=1;d=(0,+1);c=False
 return(x,y,d,c)
def m(ae,ak,al,af,an,am,aj,ah):
 if keydown(4)and ae[ak+al*8][1]==aj:af=ak+al*8;ao=(0,0,200);an,am=q(ak,al,an,am,ae,af,aj);sleep(0.1)
 if af!=ak+al*8:ao=(0,200,0)
 elif af==ak+al*8:ao=(0,0,200)
 if af!=None:
  ag=[(af%8,af//8),(ak,al)]
  if keydown(4)and ag in h(af%8,af//8,ae):n(ae,af%8,af//8,ak,al,g);aj=aj%2+1;C(ae);M(aj);k(ak,al,ah,ao);r(j(ae))
 return(aj,af,ao)
def X(am):
 ae=b();af=None;ai=0;aj=0;al,ak=(0,0);d=(0,0);an=[];c=False;ah=2;C(ae);ag=(0,200,0);M(ah)
 while am=='2_player':
  if c==False:al,ak=q(ai,aj,al,ak,ae,af,ah);r(j(ae));c=True;k(ai,aj,d,ag)
  ai,aj,d,c=u(ai,aj,d,c);ah,af,ag=m(ae,ai,aj,af,al,ak,ah,d);sleep(0.1)
 while am=='1_player':
  if c==False:al,ak=q(ai,aj,al,ak,ae,af,ah);r(j(ae));c=True;k(ai,aj,d,ag)
  ai,aj,d,c=u(ai,aj,d,c);ah,af,ag=m(ae,ai,aj,af,al,ak,ah,d);sleep(0.1)
  if ah==1:
   ao=f(ae,2);n(ae,ao[0][0],ao[0][1],ao[1][0],ao[1][1],g);ah=ah%2+1
   if N(ae)==True:
    sleep(2)
    for i in range(160):fill_rect(i,0,1,240,(255,184,60));fill_rect(319-i,0,1,240,(255,184,60));sleep(0.01)
    sleep(1);am=V(g)
def V(ae):
 af=False;i=0;ac();draw_string('game by LilyTheCatgirl',65,10);draw_string('press OK to play',75,200)
 while af==False:
  fill_rect(90,50,130,130,(210,179,139));o(ae[i],(randint(0,255),randint(0,255),randint(0,255)),90,60,6);i=(i+1)%7;sleep(0.8)
  if keydown(4):af=True
 for i in range(160):fill_rect(i,0,1,240,(255,184,60));fill_rect(319-i,0,1,240,(255,184,60));sleep(0.01)
 sleep(1);ac();fill_rect(90,50,130,130,(210,179,139));fill_rect(105,74,100,30,(0,200,0));fill_rect(105,129,100,30,(255,255,255));draw_string('1 PLAYER',115,80);draw_string('2 PLAYER',115,135);af=False;s='1_player'
 while af==False:
  if keydown(1):fill_rect(105,74,100,30,(0,200,0));fill_rect(105,129,100,30,(255,255,255));draw_string('1 PLAYER',115,80);draw_string('2 PLAYER',115,135);s='1_player'
  elif keydown(2):fill_rect(105,74,100,30,(255,255,255));fill_rect(105,129,100,30,(0,200,0));draw_string('1 PLAYER',115,80);draw_string('2 PLAYER',115,135);s='2_player'
  elif keydown(4):af=True
 X(s)
def M(ae):
 fill_rect(222,46,56,40,(255,255,255));draw_string('turn:',224,49)
 if ae==1:draw_string('black',224,67)
 else:draw_string('white',224,67)
 draw_string('update:',4,4);draw_string('1.2',75,4)
I=V(g)