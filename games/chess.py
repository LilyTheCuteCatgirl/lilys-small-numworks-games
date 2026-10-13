from kandinsky import*;from ion import keydown;from time import sleep
def Y(s):return[[ord(c)-65 for c in ae]for ae in s.split('_')]
aa=Y('JE_IG_HI_HI_HI_HI_IG_JE_A_A_JE_IG_IG_HI_GK_EO_CS');ab=Y('CDCDCDCD_CDCDCDCD_CS_CS_DQ_DQ_EO_EO_FM_FM_FM_FM_FM_FFCF_EFBCBF_DFBEBF_CGBCBBBG_CGBEBG');P=Y('KC_JE_IE_IDCB_HEBD_HI_IG_IG_JE_KC_A_IG_JE_IG_IG_HI_FFCF_DGEG_CFIF');Q=Y('KC_IF_HI_GK_GL_FDBJ_EP_DQ_CS_CHCJ_CFDK_DDDL_IM_HN_GN_EP_DR_DR');Z=Y('KC_JE_EDDCDD_DGBCBG_CS_CS_CECGCE_CDEEED_DCEEEC_DDECED_DEDCDE_EECCCE_FM_GK_GK_FM_EO_CS');U=Y('JE_DDCGCD_CFBGBF_CFBGBF_CFCECF_DDECED_EBEEEB_ECDEDC_EO_FM_FM_GK_GK_GK_FM_DQ_CS_CS');g=[None,aa,Q,P,ab,U,Z]
def b():
 a=(4,2,3,5,6,3,2,4)
 return [[p,1]for p in a+(1,)*8]+[[0,0]for _ in range(32)]+[[p,2]for p in(1,)*8+(4,2,3,6,5,3,2,4)]
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
  for x in range(8):ag=aj if(x+y)%2==0 else ak;fill_rect(22+24*x,8+24*y,24,24,ag)
 al='abcdefgh'
 for i in range(8):draw_string(str(8-i),5,11+24*i);draw_string(al[i],29+24*i,202)
 for y in range(8):
  for x in range(8):ah,af=ae[y*8+x];o(g[ah],(255-af%2*255,255-af%2*255,255-af%2*255),24+24*x,10+24*y,1)
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
def a0(x,y,af,ae,dirs):
 ag=[]
 for ak,al in dirs:
  ah,aj=x,y
  while True:
   ah+=ak;aj+=al
   if 0<=ah<8 and 0<=aj<8:
    if ae[aj*8+ah][0]==0:ag.append([(x,y),(ah,aj)])
    elif ae[aj*8+ah][1]!=af:ag.append([(x,y),(ah,aj)]);break
    else:break
   else:break
 return ag
def D(x,y,af,ae):return a0(x,y,af,ae,((1,0),(-1,0),(0,1),(0,-1)))
def O(x,y,af,ae):
 ag=[];ak=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
 for (al,am) in ak:
  ah,aj=(x+al,y+am)
  if 0<=ah<8 and 0<=aj<8:
   if ae[aj*8+ah][0]==0 or ae[aj*8+ah][1]!=af:ag.append([(x,y),(ah,aj)])
 return ag
def t(x,y,af,ae):return a0(x,y,af,ae,((1,1),(-1,1),(1,-1),(-1,-1)))
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
def a1(x,y,c,t=1):
 p=22+24*x;q=8+24*y
 if t:fill_rect(p,q,24,2,c);fill_rect(p,q+22,24,2,c);fill_rect(p,q,2,24,c);fill_rect(p+22,q,2,24,c)
 else:fill_rect(p+6,q+6,12,12,c)
def k(ae,af,d,c):
 ag=(181,137,98)if(ae+af)%2==0 else(210,179,139)
 a1(ae-d[0],af-d[1],ag);a1(ae,af,c)
def q(x,y,am,al,ae,af,ak):
 for ag in h(am,al,ae):
  i,j=ag[1];aj=(210,179,139)if(i+j)%2==0 else(181,137,98)
  a1(i,j,aj,ae[i+j*8][0]!=0)
 if ae[x+y*8][1]==ak:
  ah=(0,0,200)if af==x+y*8 else(0,200,0)
  for ag in h(x,y,ae):
   i,j=ag[1];a1(i,j,ah if ae[i+j*8][0]else(100,100,100),ae[i+j*8][0]!=0)
 return(x,y)
def H(x,y):
 if (x+y)%2==0:c=(210,179,139)
 else:c=(181,137,98)
 return c
def n(ae,ah,aj,ak,ag,af):
 if ae[ah+8*aj]==[1,1]and ag==7:p=[5,1]
 elif ae[ah+8*aj]==[1,2]and ag==0:p=[5,2]
 else:p=ae[ah+aj*8]
 fill_rect(22+24*ah,8+24*aj,24,24,H(ah,aj));fill_rect(22+24*ak,8+24*ag,24,24,H(ak,ag));c=255-ae[ah+8*aj][1]%2*255;o(af[p[0]],(c,c,c),24+24*ak,10+24*ag,1);ae[ak+8*ag]=p;ae[ah+8*aj]=[0,0];return ae
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
def r(ae):fill_rect(290,10,15,200,(0,0,0));fill_rect(290,int(110-ae/10),15,int(200-(100-ae/10)),(255,255,255));fill_rect(290,109,15,2,(255,0,0))
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
 ah=None;v=-9999 if ap else 9999
 for af in l(ae,2 if ap else 1):
  ag,ae=E(ae,af);aj=B(ae,ao-1,am,an,not ap)[0];ae=F(ae,af,ag)
  if (aj>v if ap else aj<v):
   v=aj;ah=af
   if ap:am=max(am,aj)
   else:an=min(an,aj)
  if an<=am:break
 return(v,ah)
def f(ag,af):ae=B(ag,af,-9999,9999,False)[1];return ae
def N(ae):
 if [6,1]in ae and[6,2]in ae:return False
 return True
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
 while am in ('1_player','2_player'):
  if c==False:al,ak=q(ai,aj,al,ak,ae,af,ah);r(j(ae));c=True;k(ai,aj,d,ag)
  ai,aj,d,c=u(ai,aj,d,c);ah,af,ag=m(ae,ai,aj,af,al,ak,ah,d);sleep(0.1)
  if am=='1_player'and ah==1:
   ao=f(ae,2);n(ae,ao[0][0],ao[0][1],ao[1][0],ao[1][1],g);ah=ah%2+1
   if N(ae):V();return
def V():
 fill_rect(0,0,320,240,(255,255,255));s=1
 draw_string('1 PLAYER',110,95);draw_string('2 PLAYER',110,125)
 while keydown(4):sleep(0.05)
 while not keydown(4):
  draw_string('>'if s==1 else' ',90,95);draw_string('>'if s==2 else' ',90,125)
  if keydown(1):s=1
  elif keydown(2):s=2
  sleep(0.1)
 while keydown(4):sleep(0.05)
 X('1_player'if s==1 else'2_player')
def M(ae):
 fill_rect(222,46,56,40,(255,255,255));draw_string('turn:',224,49)
 if ae==1:draw_string('black',224,67)
 else:draw_string('white',224,67)
V()